from django.test import TestCase
from learn_english.exercises.templates.exercises import models, score_calculator
from django.test import Client


class NounsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        models.OpenQuestion.objects.create(category="A1", question_1="I don't have much ... . (work)", answer="work")
        models.OpenQuestion.objects.create(category="A2", question_2="Mandy is a pretty ... . (girl)", answer="girl")
        models.FilledOpenQuestion.objects.create(username="foo", question_1="He ... reads a book (quick):",
                                                 answer="quickly")
        models.FilledOpenQuestion.objects.create(username="foo", question_2="Mandy is a pretty ... . (girl)",
                                                 answer="girl")
        models.FilledOpenQuestion.objects.create(username="bar", question_2="Mandy is a pretty ... . (girl)",
                                                 answer="girl")

    def test_store_questions(self):
        """Test relevant models"""
        open_question = models.OpenQuestion.objects.get(question_1="I don't have much ... . (work)")
        filled_open_question = models.FilledOpenQuestion.objects.get(question_1="I don't have much ... . (work)")
        self.assertEqual(open_question.question, "I don't have much ... . (work)")
        self.assertNotEqual(open_question.question, "bar")
        self.assertNotEqual(filled_open_question.username, "wilfred")

    def test_render_questions_A1(self):
        """Test question rendering"""
        response = self.client.get('/nouns/A1')
        content = response.content
        self.assertTrue("I don't have much ... . (work)" in str(content))

    def test_render_questions_A2(self):
        """Test question rendering"""
        response = self.client.get('/adverbs/A2')
        content = response.content
        self.assertTrue("Mandy is a pretty ... . (girl)" in str(content))

    def test_answer_submission_A1(self):
        """Test submission for answering A1"""
        self.client.post('/adverbs/A1', {'username': 'fun', '1': 'foo', '2': 'bar'})
        query = models.FilledOpenQuestion.objects.filter(username='fun')
        self.assertNotEqual(0, query.count())

    def test_answer_submission_A2(self):
        """Test submission for answering A2"""
        self.client.post('/adverbs/A2', {'username': 'a_subm', '1': 'foo', '2': 'bar'})
        query = models.FilledOpenQuestion.objects.filter(username='a_subm')
        self.assertNotEqual(0, query.count())

    def test_get_unique_names(self):
        names = models.FilledOpenQuestion.objects.all()
        unique_names = score_calculator.get_unique_usernames(names)
        self.assertEquals(2, len(unique_names))

    def test_get_correct_amount(self):
       self.assertEquals(2, score_calculator.get_correct_amount('foo'))

    def test_get_incorrect_amount(self):
       self.assertEquals(0, score_calculator.get_incorrect_amount('foo'))