from django.shortcuts import render, redirect
from . import forms
from .models import Lists
# Create your views here.

def lists(request):
	lists = Lists.objects.all()
	return render(request,'lists.html',{'lists':lists})

def create(request):
	form =  forms.Create(request.POST or None)
	msg = ''
	if form.is_valid():
		cd = form.cleaned_data
		Lists.objects.create(username=cd['username'],email=cd['email'])
		msg = 'Data is Created'
		return redirect('lists')
	ctx = {'form':form,'msg':msg}
	return render(request,'create.html',ctx)

