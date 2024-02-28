from django.core.management.base import BaseCommand, CommandError

from deploydocus.models import Report


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("report_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        for report_id in options["report_ids"]:
            try:
                report = Report.objects.get(pk=report_id)
            except Report.DoesNotExist:
                raise CommandError(f"Report {report_id} does not exist")

            for project in report.scope.gitlab_projects.all():
                print(f"on {project}")
                for policy in report.policies.all():
                    for rule in policy.rules.all():
                        print(f"we need to check rule {rule}")
                    for gitlab_rule in policy.gitlab_rules.all():
                        print(f"we need to check rule {gitlab_rule}")
                        print(gitlab_rule.is_compliant(project=project))
