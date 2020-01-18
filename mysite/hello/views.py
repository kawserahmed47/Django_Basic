from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name="index.html"
    def get_context_data(self, *args, **kwargs):
        response = super().get_context_data(**kwargs)
        response['name'] = "Kawser Ahmed"
        response['country'] = "BD"
        list= [1,2,3,4]
        response['lists']= list
        return response

class AboutView(TemplateView):
    template_name= "about.html"