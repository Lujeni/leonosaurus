from django.forms import ModelForm

from deploydocus.models import Report


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ["name", "policies", "scope"]
