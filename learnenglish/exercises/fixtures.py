from learnenglish.exercises import models

models.OpenQuestion.objects.create(category="A1", question="He ... reads a book (quick):", answer="quickly")
models.OpenQuestion.objects.create(category="A2", question="We watched ... (attentive):", answer="attentively")
models.FilledOpenQuestion.objects.create(username="foo", question="He ... reads a book (quick):", answer="quickly")
models.FilledOpenQuestion.objects.create(username="foo", question="We watched ... (attentive):", answer="attentively")
models.FilledOpenQuestion.objects.create(username="bar", question="We watched ... (attentive):", answer="attentively")