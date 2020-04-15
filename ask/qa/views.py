from django.contrib.auth import login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Question

def test(request):
    return HttpResponse('OK')




def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 100
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page) # Page
    except PageNotAnInteger:
        #page = paginator.page(1)
        raise Http404
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    page.page_range = paginator.page_range
    return page


def question_list_all(request):
    questions = Question.objects.all()
    page, paginator = paginate(request, questions)
    paginator.baseurl = reverse('index') + '/?page='

    return render(request, 'index.html', {
        'questions':    page.object_list,
        'page':         page,
        'paginator':    paginator,
    })


def new(request):
    questions = Question.objects.new()
    page = paginate(request, questions)
    page.baseurl = '/?page='
    return render(request, 'index.html', {
        'questions':  page.object_list,
        'page':       page,
    })


def popular(request):
    questions = Question.objects.popular()
    page = paginate(request, questions)
    page.baseurl = '/popular/?page='
    return render(request, 'index.html', {
        'questions':  page.object_list,
        'page':       page,
    })

