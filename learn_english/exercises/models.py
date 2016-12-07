from django.db import models
import django_tables2 as tables


"""
Dit creëert een database table zonder SQL
"""

class Questionnaire(models.Model):
    username = models.CharField(max_length=20)
    level = models.CharField(max_length=2)
    question_1 = models.CharField(max_length=100)
    question_2 = models.CharField(max_length=100)
    question_3 = models.CharField(max_length=100)
    question_4 = models.CharField(max_length=100)
    question_5 = models.CharField(max_length=100)

class QuestionnaireTable(tables.Table):
    class Meta:
        model = Questionnaire



class User(models.Model):
	idUser = models.AutoField(primary_key=True)
	username = models.CharField(max_length=20)





class AdverbA1(models.Model):
	idAdverbA1 = models.AutoField(primary_key=True)
	question1 = models.CharField(max_length=30)
	question2 = models.CharField(max_length=30)
	question3 = models.CharField(max_length=30)
	question4 = models.CharField(max_length=30)
	question5 = models.CharField(max_length=30)

class AdverbA2(models.Model):
	idAdverbA2 = models.AutoField(primary_key=True)
	question1 = models.CharField(max_length=30)
	question2 = models.CharField(max_length=30)
	question3 = models.CharField(max_length=30)
	question4 = models.CharField(max_length=30)
	question5 = models.CharField(max_length=30)

class AdverbB1(models.Model):
	idAdverbB1 = models.AutoField(primary_key=True)
	question1 = models.CharField(max_length=30)
	question2 = models.CharField(max_length=30)
	question3 = models.CharField(max_length=30)
	question4 = models.CharField(max_length=30)
	question5 = models.CharField(max_length=30)
	
class AdverbB2(models.Model):
	idAdverbB2 = models.AutoField(primary_key=True)
	question1 = models.CharField(max_length=30)
	question2 = models.CharField(max_length=30)
	question3 = models.CharField(max_length=30)
	question4 = models.CharField(max_length=30)
	question5 = models.CharField(max_length=30)
	
class AdverbC1(models.Model):
	idAdverbC1 = models.AutoField(primary_key=True)
	question1 = models.CharField(max_length=30)
	question2 = models.CharField(max_length=30)
	question3 = models.CharField(max_length=30)
	question4 = models.CharField(max_length=30)
	question5 = models.CharField(max_length=30)
	

#makkelijk beginnen met simpel invullen
class GerundA1(models.Model):
	idGerundA1 = models.AutoField(primary_key=True)
	question1 = models.CharField(max_length=30)
	question2 = models.CharField(max_length=30)
	question3 = models.CharField(max_length=30)
	question4 = models.CharField(max_length=30)
	question5 = models.CharField(max_length=30)

#open invullen met multiple choice
#http://www.englisch-hilfen.de/en/exercises/structures/gerund_prepositions2.htm
class GerundA2(models.Model):
	idGerundA2 = models.AutoField(primary_key=True)
	#about for of on to up
	question1choices = (
		('about', 'about'),
		('for', 'for'),
		('of', 'of'),
		('on', 'on'),
		('to', 'to'),
		('up', 'up')
	)
	question1choice = models.CharField(max_length=30)
	question2 = models.CharField(max_length=30)
	question3 = models.CharField(max_length=30)
	question4 = models.CharField(max_length=30)
	question5 = models.CharField(max_length=30)

class GerundB1(models.Model):
	idGerundB1 = models.AutoField(primary_key=True)
	question1 = models.CharField(max_length=30)
	question2 = models.CharField(max_length=30)
	question3 = models.CharField(max_length=30)
	question4 = models.CharField(max_length=30)
	question5 = models.CharField(max_length=30)

class GerundB2(models.Model):
	idGerundB2 = models.AutoField(primary_key=True)
	question1 = models.CharField(max_length=30)
	question2 = models.CharField(max_length=30)
	question3 = models.CharField(max_length=30)
	question4 = models.CharField(max_length=30)
	question5 = models.CharField(max_length=30)

class GerundC1(models.Model):
	idGerundC1 = models.AutoField(primary_key=True)
	question1 = models.CharField(max_length=30)
	question2 = models.CharField(max_length=30)
	question3 = models.CharField(max_length=30)
	question4 = models.CharField(max_length=30)
	question5 = models.CharField(max_length=30)

class Adverb(models.Model):
	idAdverb = models.AutoField(primary_key=True)
	fk_idAdverbA1 = models.ForeignKey(AdverbA1, on_delete=models.CASCADE)
	fk_idAdverbA2 = models.ForeignKey(AdverbA2, on_delete=models.CASCADE)
	fk_idAdverbB1 = models.ForeignKey(AdverbB1, on_delete=models.CASCADE)
	fk_idAdverbB2 = models.ForeignKey(AdverbB2, on_delete=models.CASCADE)
	fk_idAdverbC1 = models.ForeignKey(AdverbC1, on_delete=models.CASCADE)
	
class Gerund(models.Model):
	idGerund = models.AutoField(primary_key=True)
	fk_idGerundA1 = models.ForeignKey(GerundA1, on_delete=models.CASCADE)
	fk_idGerundA2 = models.ForeignKey(GerundA2, on_delete=models.CASCADE)
	fk_idGerundB1 = models.ForeignKey(GerundB1, on_delete=models.CASCADE)
	fk_idGerundB2 = models.ForeignKey(GerundB2, on_delete=models.CASCADE)
	fk_idGerundC1 = models.ForeignKey(GerundC1, on_delete=models.CASCADE)

class Test(models.Model):
	idTest = models.AutoField(primary_key=True)
	fk_idUser = models.ForeignKey(User, on_delete=models.CASCADE)
	fk_idGerund = models.ForeignKey(Gerund, on_delete=models.CASCADE)
	#fk_idAdverb = models.ForeignKey(Adverb, on_delete=models.CASCADE)