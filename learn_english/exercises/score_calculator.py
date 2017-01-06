from . import models


def get_unique_usernames(results):
    usernames = []
    for result in results:
        usernames.append(result.username)
    return list(set(usernames))


def get_correct_amount(username):
    questions = models.FilledOpenQuestion.objects.filter(username=username)
    total_correct = 0
    for question in questions:
        correct_answer = models.OpenQuestion.objects.get(question=question.question)
        if question.answer == correct_answer.answer:
            total_correct += 1
    return total_correct


def get_incorrect_amount(username):
    questions = models.FilledOpenQuestion.objects.filter(username=username)
    total_incorrect = 0
    for question in questions:
        correct_answer = models.OpenQuestion.objects.get(question=question.question)
        if question.answer != correct_answer.answer:
            total_incorrect += 1
    return total_incorrect

