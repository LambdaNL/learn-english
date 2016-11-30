from .models import Questionnaire

def get_unique_usernames(results):
    usernames = []
    for result in results:
        usernames += result.username
    return set(usernames)


def calculate_scores(unique_users):

    for user in unique_users:
        user_results = Questionnaire.objects.filter(username=user)
        total_score = 0
        for user_result in user_results:
            if user_result.level == "A1":
                total_score += evaluate_A1(user_result)
            if user_result.level == "A2":
                total_score += evaluate_A2(user_result)
            if user_result.level == "B1":
                total_score += evaluate_B1(user_result)
            if user_result.level == "B2":
                total_score += evaluate_B2(user_result)
            if user_result.level == "C1":
                total_score += evaluate_C1(user_result)


def evaluate_A1(answers):
    score = 0
    if answers.question_1 == "quickly":
        score += 1
    if answers.question_2 == "pretty":
        score += 1
    if answers.question_3 == "terribly":
        score += 1
    if answers.question_4 == "good":
        score += 1
    if answers.question_5 == "easily":
        score += 1
    return score


def evaluate_A2(answers):
    score = 0
    if answers.question_1 == "quickly":
        score += 1
    if answers.question_2 == "pretty":
        score += 1
    if answers.question_3 == "terribly":
        score += 1
    if answers.question_4 == "good":
        score += 1
    if answers.question_5 == "easily":
        score += 1
    return score


def evaluate_B1(answers):
    score = 0
    if answers.question_1 == "quickly":
        score += 1
    if answers.question_2 == "pretty":
        score += 1
    if answers.question_3 == "terribly":
        score += 1
    if answers.question_4 == "good":
        score += 1
    if answers.question_5 == "easily":
        score += 1
    return score


def evaluate_B2(answers):
    score = 0
    if answers.question_1 == "quickly":
        score += 1
    if answers.question_2 == "pretty":
        score += 1
    if answers.question_3 == "terribly":
        score += 1
    if answers.question_4 == "good":
        score += 1
    if answers.question_5 == "easily":
        score += 1
    return score


def evaluate_C1(answers):
    score = 0
    if answers.question_1 == "quickly":
        score += 1
    if answers.question_2 == "pretty":
        score += 1
    if answers.question_3 == "terribly":
        score += 1
    if answers.question_4 == "good":
        score += 1
    if answers.question_5 == "easily":
        score += 1
    return score