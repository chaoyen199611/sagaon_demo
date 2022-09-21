from django.shortcuts import render


from django.views.generic.base import TemplateView
from . models import StationInfo,Weather,TripData

class DemoPageView(TemplateView):

    template_name="demo.html"

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['stations']=StationInfo.objects.all()
        context['weathers']=Weather.objects.all()
        context['tripdatas']=TripData.objects.all()
        return context
