import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import AnonymousUser
from .models import Url

from .models import Url

class HomePageView(TemplateView):
    template_name = 'home.html'

class CreateUrlView(CreateView):
    model = Url
    template_name = 'createurl.html'
    fields = ['url']

class MyUrlView(LoginRequiredMixin, ListView):
    context_object_name = 'my_urls'
    # queryset = Url.objects.filter(creator=request.user)
    template_name = 'myurls.html'
    login_url = 'account_login'
    def get_queryset(self):
        return Url.objects.filter(creator=self.request.user)


def saveUrl(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url.startswith('https://'):
            url = url.lstrip('https://')
        elif url.startswith('http://'):
            url = url.lstrip('http://')

        short_form = str(uuid.uuid4())[:5]
        new_url = Url(url=url,
         short_form=short_form,
         creator=None if isinstance(request.user, AnonymousUser) else request.user
        )
        new_url.save()
        return render(request, 'home.html', {'short_form': short_form})

def visit(request, pk):
    url_object = Url.objects.get(short_form=pk)
    return redirect('https://'+url_object.url)
