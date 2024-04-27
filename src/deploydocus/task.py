from celery import shared_task


@shared_task
def task_report() -> None:
    print("debug")
    return None
