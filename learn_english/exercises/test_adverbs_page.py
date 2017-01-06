from django.test import TestCase
from . import models
from django.test import Client


class AdverbsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        models.OpenQuestion.objects.create(category="A1", question="He ... reads a book (quick):", answer="quickly")
        models.FilledOpenQuestion.objects.create(username="foo", question="He ... reads a book (quick):", answer="quickly")

    def test_store_questions(self):
        """Test relevant models"""
        open_question = models.OpenQuestion.objects.get(question="He ... reads a book (quick):")
        filled_open_question = models.FilledOpenQuestion.objects.get(question="He ... reads a book (quick):")
        self.assertEqual(open_question.question, "He ... reads a book (quick):")
        self.assertNotEqual(open_question.question, "bar")
        self.assertNotEqual(filled_open_question.username, "baz")

    def test_render_questions(self):
        """Test question rendering"""
        response = self.client.get('/adverbs/A1')
        content = response.content
        self.assertTrue("He ... reads a book (quick):" in str(content))

    def test_answer_submission(self):
        """Test submission of answers"""
        self.client.post('/adverbs/A1', {'username': 'rare', '1': 'foo', '2': 'bar'})
        query = models.FilledOpenQuestion.objects.filter(username='rare')
        self.assertNotEqual(0, query.count())





