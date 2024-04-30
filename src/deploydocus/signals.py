import logging

from django.db.models import signals

from deploydocus.models import Report
from deploydocus.task import task_report

logger = logging.getLogger(__name__)

def celery_task_report(sender, created, instance, **kwargs):
    task_report.delay()


signals.post_save.connect(celery_task_report, sender=Report)
