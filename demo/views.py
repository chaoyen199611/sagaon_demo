from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from . models import StationInfo,Weather,TripData


class DemoPageView(TemplateView):

    template_name="demo.html"

    def get(self,request,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        date=self.request.GET.get('time')
        if date==None:
             date='2020-08-20 02:00:00'
        
        
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            newtrip=TripData.objects.all().filter(time=str(date)).order_by('station_id')
            trip = serializers.serialize('json',newtrip)
            return JsonResponse(trip,safe=False)
        else:
            print(str(date))
            context['weathers']=Weather.objects.all()
            # context['tripdatas']=TripData.objects.raw('select * from trip_data order by row_number() over (partition by station_id order by `id`), station_id;')
            context['tripdatas']=TripData.objects.all().filter(time=str(date)).order_by('station_id')

            context['stations']=StationInfo.objects.all()

            # date=self.request.GET.get('key1')
            # print(date)
            return self.render_to_response(context)

    # def get(self, *args, **kwargs):
    #     date=self.request.GET.get('key1')
    #     print(date)
    #     trip = TripData.objects.all().filter(time=date).order_by('station_id')
    #     qs_json = serializers.serialize('json', trip)
    #     return JsonResponse(qs_json,safe=False)
