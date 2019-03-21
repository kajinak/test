

# Create your views here.
from familydata.func.quadric_eq import Coefficient, get_dis, get_eq_root
from django.shortcuts import render, redirect
from django import forms
from familydata.models import Family, FamilyApply
from django.contrib import messages
from django.template import RequestContext


def home(request):
    return render(request, 'index.html')


def family_list(request):
    family_list = Family.objects.all()
    return render(request, "family_list.html", {'family_list': family_list})


def news(request):
    return render(request, "news.html")


def detail(request, a):
    context = {}
    family_list = Family.objects.get(id=a)
    context['family'] = family_list
    return render(request, 'detail.html', context)


class QuadraticForm(forms.Form):
    a = forms.CharField(max_length=10)
    b = forms.CharField(max_length=10)
    c = forms.CharField(max_length=10)


def quadric(request):
    form = QuadraticForm()
    context = {'error': False}
    context['form'] = form
    for name_value in ['a', 'b', 'c']:
        coefficient = Coefficient(name_value, request.GET.get(name_value, ''))
        if coefficient.is_valid():
            context[name_value] = coefficient.value_int
        else:
            context['error'] = True
            context[name_value + '_error'] = coefficient.error_message
            context[name_value] = coefficient.value
    if not context['error']:
        a = context['a']
        b = context['b']
        c = context['c']
        d = get_dis(a, b, c)
        if d < 0:
            result_message = "Дискриминант меньше нуля, у уравнения нет действительных корней."
        elif d == 0:
            x = get_eq_root(a, b, d)
            result_message = "Дискриминант равен нулю, квадратное уравнение имеет один корень x1=x2={}".format(x)
        else:
            x1 = get_eq_root(a, b, d)
            x2 = get_eq_root(a, b, d, order=2)
            result_message = "Дискриминант больше нуля, квадратное уравнение имеет два корня x1={}, x2={}".format(x1, x2)
        context.update({'d': d, 'result_massage': result_message})
    return render(request, 'quadric.html', context)


class GetFormsForm(forms.Form):
    name = forms.CharField(max_length=20, help_text='Your name')
    email = forms.EmailField(required=False)
    package = forms.ChoiceField(choices=(('main','Main'),
                                         ('half', 'Half'),
                                         ('simple', 'Simple')),
                                widget=forms.RadioSelect)
    news_subscribe = forms.BooleanField()


class ModelGetFormsForm(forms.ModelForm):
    class Meta:
        model = FamilyApply
        exclude = ['date_apply', 'is_active', 'comment']
        widgets = {'package': forms.RadioSelect}
        labels = {'email': 'Mail'}


def get_forms(request):
    if request.method == "POST":
        form = ModelGetFormsForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Saved!")
            return redirect('/forms')

    else:
        form = ModelGetFormsForm()
    return render(request, 'forms.html', {'form': form})
