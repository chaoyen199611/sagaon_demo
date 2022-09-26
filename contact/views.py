from django.shortcuts import render
from django.views.generic.base import TemplateView

class ContactPageView(TemplateView):

    template_name= "contact.html"

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        return context
