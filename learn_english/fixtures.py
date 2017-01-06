from exercises.models import OpenQuestion

OpenQuestion.objects.create(category='A1', question='a1', answer='foo')
OpenQuestion.objects.create(category='A1', question='a1', answer='foo')
OpenQuestion.objects.create(category='B1', question='b1', answer='foo')
OpenQuestion.objects.create(category='B2', question='b2', answer='foo')
OpenQuestion.objects.create(category='C1', question='c1', answer='foo')
