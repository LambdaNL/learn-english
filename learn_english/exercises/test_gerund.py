import json
from django.test import *
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.sessions.middleware import SessionMiddleware
from .models import *

def add_middleware_to_request(request, middleware_class):
	middleware = middleware_class()
	middleware.process_request(request)
	return request


def add_middleware_to_response(response, middleware_class):
	middleware = middleware_class()
	middleware.process_request(response)
	return response

c = Client()
class GerundTests(TestCase):
	def setUp(self):
		self.response = c.get('/gerund')
		print("RESPONSE PRINT HALLOOOOOOOOOOOOOOO"+self.response)
		self.correctdata = {
			"cdsfmiddlewaretoken": "foo",
			"username": "foobar",
			"question_1": "at",
			"question_2": "about",
			"question_3": "of",
			"question_4": "like",
			"question_5": "to"
		}
		self.falsedata = {
			"cdsfmiddlewaretoken": "foo",
			"username": "foobar",
			"question_1": "foo",
			"question_2": "foo",
			"question_3": "foo",
			"question_4": "foo",
			"question_5": "foo"
		}

	def test_gerund_response(self):
		self.assertEquals(self.response.status_code, 200)

	def test_gerund_menu(self):
		self.assertContains(self.response, "A1")
		# self.assertContains(self.response, "A2")
		# self.assertContains(self.response, "B1")
		# self.assertContains(self.response, "B2")
		# self.assertContains(self.response, "C1")

	def test_valid_A1_submission(self):
		form_submission = c.post("/gerund/A1/", self.correctdata)
		# data = json.loads(form_submission.content)
		self.assertEquals(form_submission.status_code, 201)
        
	def test_invalid_A1_submission(self):
		form_submission = c.post("/gerund/A1/", self.falsedata)
		self.assertEquals(form_submission.status_code, 201)