from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
from django.core import serializers
from django.views.generic.base import TemplateView
from . models import StationInfo,Weather,TripData

class DemoPageView(TemplateView):

    template_name="demo.html"

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        
        context['weathers']=Weather.objects.all()
        context['tripdatas']=TripData.objects.all().filter(time='2020-08-20 01:30:00').order_by('station_id')
        context['stations']=StationInfo.objects.all()

        # date=self.request.GET.get('key1')
        # print(date)
        return context

    # def get(self, *args, **kwargs):
    #     date=self.request.GET.get('key1')
    #     print(date)
    #     trip = TripData.objects.all().filter(time=date).order_by('station_id')
    #     qs_json = serializers.serialize('json', trip)
    #     return JsonResponse(qs_json,safe=False)
