import json
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.sessions.middleware import SessionMiddleware


def add_middleware_to_request(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request


def add_middleware_to_response(response, middleware_class):
    middleware = middleware_class()
    middleware.process_request(response)
    return response


class ViewsTests(TestCase):

    def setUp(self):
        self.response = self.client.get("/adverbs/")
        self.data = {
            "cdsfmiddlewaretoken": "foo",
            "username": "foo",
            "question_1": "foo",
            "question_2": "foo",
            "question_3": "foo",
            "question_4": "foo",
            "question_5": "foo"
        }

    def test_adverbs_response(self):
        self.assertEquals(self.response.status_code, 200)

    def test_adverbs_menu(self):
        self.assertContains(self.response, "A1")
        self.assertContains(self.response, "A2")
        self.assertContains(self.response, "B1")
        self.assertContains(self.response, "B2")
        self.assertContains(self.response, "C1")

    def test_valid_A1_submission(self):
        form_submission = self.client.post("/adverbs/A1/", self.data)
        # data = json.loads(form_submission.content)
        self.assertEquals(form_submission.status_code, 201)
