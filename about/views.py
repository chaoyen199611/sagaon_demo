from django.shortcuts import render


from django.views.generic.base import TemplateView
from .models import Article


class AboutPageView(TemplateView):

    template_name="about.html"

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['article']=Article.objects.get(id=1)
        return context