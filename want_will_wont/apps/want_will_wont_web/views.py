from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from want_will_wont.apps.want_will_wont_web.models import AnswerSet, ActivityCategory


def home(request):
    context = {}

    return render_to_response('home.html', RequestContext(request, context))


def answer(request):
    context = {}
    if request.method == 'GET':
        context['activity_categories'] = ActivityCategory.objects.prefetch_related('activities')

    return render_to_response('answer.html', RequestContext(request, context))


def compare(request, secret1=None, secret2=None):
    answer_set_1 = None
    if secret1:
        answer_set_1 = get_object_or_404(AnswerSet, secret=secret1)
    context = {
        'secret1': secret1,
        'secret2': secret2,
        'answer_set_1': answer_set_1
    }

    return render_to_response('compare.html', RequestContext(request, context))


def about(request):
    context = {
        'is_about': True
    }

    return render_to_response('about.html', RequestContext(request, context))
