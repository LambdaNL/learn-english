from . import models, scorecalculator
from django.test import TestCase
from django.test import Client


class AdverbsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        models.OpenQuestion.objects.create(category="A1", question="He ... reads a book (quick):", answer="quickly")
        models.OpenQuestion.objects.create(category="A2", question="We watched ... (attentive):", answer="attentively")
        models.FilledOpenQuestion.objects.create(username="foo", question="He ... reads a book (quick):",
                                                 answer="quickly")
        models.FilledOpenQuestion.objects.create(username="foo", question="We watched ... (attentive):",
                                                 answer="attentively")
        models.FilledOpenQuestion.objects.create(username="bar", question="We watched ... (attentive):",
                                                 answer="attentively")

    def test_store_questions(self):
        """Test relevant models"""
        open_question = models.OpenQuestion.objects.get(question="He ... reads a book (quick):")
        filled_open_question = models.FilledOpenQuestion.objects.get(question="He ... reads a book (quick):")
        self.assertEqual(open_question.question, "He ... reads a book (quick):")
        self.assertNotEqual(open_question.question, "bar")
        self.assertNotEqual(filled_open_question.username, "baz")

    def test_render_questions_A1(self):
        """Test question rendering"""
        response = self.client.get('/adverbs/A1')
        content = response.content
        self.assertTrue("He ... reads a book (quick):" in str(content))

    def test_render_questions_A2(self):
        """Test question rendering"""
        response = self.client.get('/adverbs/A2')
        content = response.content
        self.assertTrue("We watched ... (attentive):" in str(content))

    def test_answer_submission_A1(self):
        """Test submission for answering A1"""
        self.client.post('/adverbs/A1', {'username': 'rare', '1': 'foo', '2': 'bar'})
        query = models.FilledOpenQuestion.objects.filter(username='rare')
        self.assertNotEqual(0, query.count())

    def test_answer_submission_A2(self):
        """Test submission for answering A2"""
        self.client.post('/adverbs/A2', {'username': 'rare', '1': 'foo', '2': 'bar'})
        query = models.FilledOpenQuestion.objects.filter(username='rare')
        self.assertNotEqual(0, query.count())

    def test_get_unique_names(self):
        names = models.FilledOpenQuestion.objects.all()
        unique_names = scorecalculator.get_unique_usernames(names)
        self.assertEquals(2, len(unique_names))

    def test_get_correct_amount(self):
       self.assertEquals(2, scorecalculator.get_correct_amount('foo'))

    def test_get_incorrect_amount(self):
       self.assertEquals(0, scorecalculator.get_incorrect_amount('foo'))