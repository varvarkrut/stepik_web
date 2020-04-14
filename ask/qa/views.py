from django.http import Http404
from django.shortcuts import render
from .models import Question
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


@require_GET
def new(request):
    questions = Question.objects.new()
    page = paginate(request, questions)
    page.baseurl = '/?page='
    return render(request, 'index.html', {
        'questions':  page.object_list,
        'page':       page,
    })
