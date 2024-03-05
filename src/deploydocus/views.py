from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "about.html"

class IndexView(TemplateView):
    template_name = "index.html"
