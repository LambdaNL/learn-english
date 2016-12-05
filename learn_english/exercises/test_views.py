from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory
from .views import adverbs


def add_middleware_to_request(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request


def add_middleware_to_response(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request


class SavoryIceCreamTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_cheese_flavors(self):
        request = self.factory.get('/adverbs/A1')
        request.user = AnonymousUser()
        # Annotate the request object with a session
        request = add_middleware_to_request(request, SessionMiddleware)
        request.session.save()
        # process and test the request
        response = adverbs(request, "A1")
        self.assertContains(response, "bleah!")
