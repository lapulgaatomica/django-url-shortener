import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .models import Url

class HomePageView(TemplateView):
    template_name = 'home.html'

class CreateUrlView(CreateView):
    model = Url
    template_name = 'createurl.html'
    fields = ['url']

def saveUrl(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        short_form = str(uuid.uuid4())[:5]
        new_url = Url(url=url, short_form=short_form)
        new_url.save()
        return render(request, 'home.html', {'short_form': short_form})

def visit(request, pk):
    url_object = Url.objects.get(short_form=pk)
    return redirect('https://'+url_object.url)
