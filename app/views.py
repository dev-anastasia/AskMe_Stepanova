from django.shortcuts import render

QUESTIONS = [
    {
        'title': f'Some question! {i}',
        'id': i,
        'text': f'Question text {i}'
    } for i in range(15)
]

HOT_QUESTIONS = [
    {
        'id': i,
        'title': f'Hot question! {i}',
        'text': f'Question text {i}'
    } for i in range(15)
]

ANSWERS = [
    {
        'id': i,
        'title': f'Some answer! {i}',
        'text': f'Answer text {i}'
    } for i in range(15)
]

def index(request):
    return render(request, 'index.html', {'questions': QUESTIONS})


def question(request, question_id):
    return render(request, 'one_question.html', {'answers': ANSWERS, 'item': QUESTIONS[question_id]})


def tag(request):
    return render(request, 'tag.html', {'questions': QUESTIONS})


def hot(request):
    return render(request, 'hot.html', {'hot_questions': HOT_QUESTIONS})


def settings(request):
    return render(request, 'settings.html')


def ask(request):
    return render(request, 'ask.html')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')

