from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist

from deploydocus.models import Report


@shared_task
def task_report(report_id: int) -> None:
    try:
        report = Report.objects.get(id=report_id)
        report.check_compliance()
    except ObjectDoesNotExist:
        return None
