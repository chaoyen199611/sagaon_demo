from django.shortcuts import render


from django.views.generic.base import TemplateView


class DemoPageView(TemplateView):

    template_name="demo.html"

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        return context