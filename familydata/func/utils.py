from django.contrib import messages
from django.shortcuts import render, redirect
from familydata.models import *
from django import forms


class ModelGetFormsForm(forms.ModelForm):
    class Meta:
        model = Family
        exclude = ['date_of_birth']
        widgets = {'posittion': forms.RadioSelect}


def get_forms(request):
    if request.method == "POST":
        form = ModelGetFormsForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('/family_list')

    else:
        form = ModelGetFormsForm()
    return render(request, 'forms.html', {'form': form})

def delete_form(request, pk):
    family = Family.objects.get(id=pk)
    if request.method == "POST":
        family.delete()
        return redirect('/')
    else:
        form = ModelGetFormsForm(instance=family)
    return render(request, 'get_form_delete.html', {'form': form})

def get_form_edit(request, pk):
    family = Family.objects.get(id=pk)
    if request.method == "POST":
        form = ModelGetFormsForm(request.POST, instance=family)
        if form.is_valid():
            instance = form.save()
            return redirect('/family_list')
    else:
        form = ModelGetFormsForm(instance=family)
    return render(request, 'get_form_edit.html', {'form': form})
