from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import  Hidrometros
from .forms import HidrometrosForm
import numpy as np


@login_required(login_url='/login/')
def hidrometros_home(request):
	return render(request,"home.html")

@login_required(login_url='/login/')
def hidrometros_create(request):
	form = HidrometrosForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		#print form.cleaned_data.get("title")
		instance.save()
		messages.success(request,"Successfully Created!!")
		return HttpResponseRedirect(instance.get_absolute_url())

	#if request.method == 'POST':
		#print request.POST.get("title")
	#	title = request.POST.get("title")
		#print request.POST.get("content")
	#	content = request.POST.get("content")
	#	Posts.objects.create(title=title,content=content)

	context = {
		"form":form,
	}
	return render(request,"hidrometros_form.html", context)

@login_required(login_url='/login/')
def hidrometros_detail(request, id=None):
	instance = get_object_or_404( Hidrometros,id=id)
	context = {
		#"title":instance.title,
		"instance": instance,
	}
	return render(request,"hidrometros_detail.html", context)

@login_required(login_url='/login/')
def hidrometros_list(request, local=None):	
	queryset =  Hidrometros.objects.filter(local=local).order_by('data')
	values = queryset.values('medicao_inicial','medicao_final')

	consumo = []
	consumo_stats = []
	for i in values:
		if i['medicao_inicial']!=None and i['medicao_final']!=None:
			consumo.append((i['medicao_final'] - i['medicao_inicial']))
			consumo_stats.append((i['medicao_final'] - i['medicao_inicial']))
		else:
			consumo.append("_")

	if consumo_stats!=[]:
		max_consumo = max(consumo_stats)
		min_consumo = min(consumo_stats)		
		consumo =  ",".join(str(i) for i in consumo)
		media_diurno = round(np.mean(consumo_stats))
		media_graph = ",".join(str(media_diurno) for i in range(0,len(consumo_stats)))
		std_diurno = round(np.std(consumo_stats))
		acima_media = round(((max_consumo*100)/media_diurno)-100)
		abaixo_media = round(100-((min_consumo*100)/media_diurno))
	else:
		max_consumo = 0
		min_consumo = 0
		consumo = 0
		media_diurno = 0
		media_graph = 0
		std_diurno = 0
		acima_media = 0
		abaixo_media = 0

	context = {
			"object_list": queryset,
	 		"values": values,
	 		"consumo": consumo,
	 		"max_consumo": max_consumo,
	 		"min_consumo": min_consumo,
	 		"media": media_diurno,
	 		"media_graph": media_graph,
	 		"std": std_diurno,
	 		"acima_media": acima_media,
	 		"abaixo_media": abaixo_media,
	 		"hidrom": local
	 	}
	return render(request,"hidrometros_list.html", context)

@login_required(login_url='/login/')
def hidrometros_update(request, id=None):
	instance = get_object_or_404( Hidrometros,id=id)
	form = HidrometrosForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Item Saved!!")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		#"title":instance.title,
		"instance": instance,
		"form": form
	}
	return render(request,"hidrometros_form.html", context)

@login_required(login_url='/login/')
def hidrometros_delete(request, id=None):
	instance = get_object_or_404( Hidrometros, id=id)
	instance.delete()
	messages.success(request,"Item Deleted")
	return redirect("hidrometros:list")
