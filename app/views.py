from django.shortcuts import render

QUESTIONS = [
    {
        'title': f'Some question! {i}',
        'id': i,
        'text': f'Some text! {i}'
    } for i in range(1, 30)
]

ANSWERS = [
    {
        'title': f'Some answer! {i}',
        'id': i,
        'text': f'Some text! {i}'
    } for i in range(1, 20)
]


def index(request):
    return render(request, 'index.html', {'questions': QUESTIONS})


def question(request):
    return render(request, 'question.html', {'answers': ANSWERS})
