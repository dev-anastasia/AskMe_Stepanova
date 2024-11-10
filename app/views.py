from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

QUESTIONS = [
    {
        'id': i,
        'title': f'Some question №{i}',
        'text': f'Question text №{i}'
    } for i in range(1, 30)
]

HOT_QUESTIONS = [
    {
        'id': i,
        'title': f'Hot question №{i}',
        'text': f'Hot question text №{i}'
    } for i in range(1, 30)
]

ANSWERS = [
    {
        'id': i,
        'title': f'Answer №{i}',
        'text': f'Answer text №{i}'
    } for i in range(1, 15)
]

default_page = 1
items_per_page = 5

def index(request):
    page_num = request.GET.get('page', default_page)
    paginator = Paginator(QUESTIONS, items_per_page)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(default_page)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'page_obj': page_obj})


def question(request, question_id):
    page_num = request.GET.get('page', default_page)
    paginator = Paginator(ANSWERS, items_per_page)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(default_page)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'one_question.html', {'item': QUESTIONS[question_id - 1], 'page_obj': page_obj})


def tag(request):
    page_num = request.GET.get('page', default_page)
    paginator = Paginator(QUESTIONS, items_per_page)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(default_page)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'tag.html', {'page_obj': page_obj})


def hot(request):
    page_num = request.GET.get('page', default_page)
    paginator = Paginator(HOT_QUESTIONS, items_per_page)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(default_page)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'hot.html', {'page_obj': page_obj})


def settings(request):
    return render(request, 'settings.html')


def ask(request):
    return render(request, 'ask.html')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')

