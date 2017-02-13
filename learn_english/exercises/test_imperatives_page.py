from django.test import TestCase
from . import models, score_calculator
from django.test import Client


class ImperativesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        models.OpenQuestion.objects.create(category="A1", question="... in your bed. (sleeping):", answer="Sleep")
        models.OpenQuestion.objects.create(category="A2", question="... your face. (washing):", answer="Wash")
        models.FilledOpenQuestion.objects.create(username="foo", question="... in your bed. (sleeping):", answer="Sleep")
        models.FilledOpenQuestion.objects.create(username="foo", question="... your face. (washing):", answer="Wash")
        models.FilledOpenQuestion.objects.create(username="bar", question="We watched ... (attentive):",
                                                 answer="attentively")

    def test_store_questions(self):
        """Test relevant models"""
        open_question = models.OpenQuestion.objects.get(question="... in your bed. (sleeping):")
        filled_open_question = models.FilledOpenQuestion.objects.get(question="... in your bed. (sleeping):")
        self.assertEqual(open_question.question, "... in your bed. (sleeping):")
        self.assertNotEqual(open_question.question, "bar")
        self.assertNotEqual(filled_open_question.username, "baz")

    def test_render_questions_A1(self):
        """Test question rendering"""
        response = self.client.get('/imperatives/A1')
        content = response.content
        self.assertTrue("... in your bed. (sleeping):" in str(content))

    def test_render_questions_A2(self):
        """Test question rendering"""
        response = self.client.get('/imperatives/A2')
        content = response.content
        self.assertTrue("... your face. (washing):" in str(content))

    def test_answer_submission_A1(self):
        """Test submission for answering A1"""
        self.client.post('/imperatives/A1', {'username': 'rare', '1': 'foo', '2': 'bar'})
        query = models.FilledOpenQuestion.objects.filter(username='rare')
        self.assertNotEqual(0, query.count())

    def test_answer_submission_A2(self):
        """Test submission for answering A2"""
        self.client.post('/imperatives/A2', {'username': 'rare', '1': 'foo', '2': 'bar'})
        query = models.FilledOpenQuestion.objects.filter(username='rare')
        self.assertNotEqual(0, query.count())

    def test_get_unique_names(self):
        names = models.FilledOpenQuestion.objects.all()
        unique_names = score_calculator.get_unique_usernames(names)
        self.assertEquals(2, len(unique_names))

    def test_get_correct_amount(self):
       self.assertEquals(2, score_calculator.get_correct_amount('foo'))

    def test_get_incorrect_amount(self):
       self.assertEquals(0, score_calculator.get_incorrect_amount('foo'))