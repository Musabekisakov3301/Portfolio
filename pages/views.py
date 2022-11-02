from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView,TemplateView

'''class PagesListView(ListView):
    queryset = 'first'
    template_name = 'pages/pages_list.html'''

def PagesListView(request):
    
    icons = Skils.objects.all()
    summarys = Summary.objects.all()
    contacts = Contact.objects.all()
    animations = Animation.objects.all()
    photos = Photo.objects.all()

    
    context = {
        'icons': icons,
        'summarys':summarys,
        'contacts':contacts,
        'animations':animations,
        'photos':photos, 
        
    }
    
    return render(request, 'pages/pages_list.html', context)

    
class PagesDetailView(DetailView):
    queryset = 'firsts'
    template_name = 'pages/pages_detail.html'

class LangingPageView(TemplateView):
    template_name = 'pages/landing_page.html'