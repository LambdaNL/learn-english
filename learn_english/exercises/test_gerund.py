from django.test import TestCase
from . import models
from django.test import Client

#Alle antwoorden worden al lowercase opgeslagen

class GerundTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        models.OpenQuestion.objects.create(category="CC" , question="This is a test question rush b", answer="cyka")
		models.OpenQuestion.objects.create(category="CC" , question="This is also a test question", answer="noway")
		models.FilledOpenQuestion.objects.create(category="CC", question="This is a test question rush b", answer="cyka")
		models.FilledOpenQuestion.objects.create(username="ct", question="This is also a test question", answer="watu")
		
    def test_store_questions(self):
        """Test relevant models"""
		test_question = models.OpenQuestion.objects.get(question="This is a test question rush b")
        filled_test_question = models.FilledOpenQuestion.objects.get(question="This is a test question rush b")
        self.assertEqual(test_question.question, "This is a test question rush b")
        self.assertNotEqual(test_question.question, "bar")
        self.assertNotEqual(filled_test_question.username, "CT")

    def test_render_questions_A1(self):
        """Test question rendering"""
        response = self.client.get('/gerund/A1')
        content = response.content
        self.assertTrue("My friend is good ... playing volleyball." in str(content))

    def test_answer_submission_A1(self):
        """Test submission of answers A1"""
        self.client.post('/gerund/A1', {'username': 'rare', '1': 'foo', '2': 'bar'})
        query = models.FilledOpenQuestion.objects.filter(username='rare')
        self.assertNotEqual(0, query.count())


