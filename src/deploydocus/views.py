from django.views.generic import TemplateView, DetailView, ListView

from deploydocus.models import Report


class AboutView(TemplateView):
    template_name = "about.html"


class IndexView(ListView):
    template_name = "index.html"
    context_object_name = "reports_list"

    def get_queryset(self):
        return Report.objects.all()


class ReportDetailView(DetailView):
    model = Report
    template_name = "report.html"
