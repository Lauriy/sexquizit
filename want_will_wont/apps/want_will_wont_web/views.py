from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext

from want_will_wont.apps.want_will_wont_web.forms import ResponseForm, EmailSignupForm
from want_will_wont.apps.want_will_wont_web.models import AnswerSet, ActivityCategory, Activity

from want_will_wont.apps.want_will_wont_web.analyzer import analyze


def home(request):
    context = {
        'is_home': True
    }
    if request.method == 'POST':
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'E-mail saved. Thanks!')
            form.save()

    return render_to_response('home.html', RequestContext(request, context))


def answer(request, gender, secret2=None):
    if gender == 'male':
        allowed_genders = [Activity.MALE, Activity.BOTH]
    else:
        allowed_genders = [Activity.FEMALE, Activity.BOTH]
    context = {
        'allowed_genders': allowed_genders,
        'categories': ActivityCategory.objects.prefetch_related('activities')
    }
    form = None
    if request.method == 'GET':
        form = ResponseForm(gender=gender)

    elif request.method == 'POST':
        form = ResponseForm(request.POST, gender=gender)
        if form.is_valid():
            answer_set = form.save()
            return redirect(reverse('compare_1', kwargs={'pk1': answer_set.pk}))

    context['form'] = form

    return render_to_response('answer.html', RequestContext(request, context))


def compare(request, pk1=None, pk2=None):
    analyze_results = None
    if pk1 and pk2:
        answer_set_1 = AnswerSet.objects.filter(pk=pk1).prefetch_related('answers').first()
        answer_set_2 = AnswerSet.objects.filter(pk=pk2).prefetch_related('answers').first()
        analyze_results = analyze(answer_set_1, answer_set_2)

    context = {
        'pk1': pk1,
        'pk2': pk2,
        'analyze_results': analyze_results
    }

    return render_to_response('compare.html', RequestContext(request, context))


def about(request):
    context = {
        'is_about': True
    }

    return render_to_response('about.html', RequestContext(request, context))
