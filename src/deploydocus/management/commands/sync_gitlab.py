import re
from django.core.management.base import BaseCommand

from deploydocus.models import Scope, GitlabProject
from deploydocus.utils import get_projects, get_gitlab_connection


def check_include(includes, path_with_namespace):
    for include_rule in includes:
        if re.match(include_rule, path_with_namespace):
            return True
    return False

class Command(BaseCommand):
    help = "Synchronize GitLab projects with Leonosaurus based on Scope include/exclude"

    def handle(self, *args, **options):
        gl = get_gitlab_connection()
        scope_includes = set(s.include for s in Scope.objects.all())
        scope_excludes = set(s.exclude for s in Scope.objects.all())

        for project in get_projects(gl=gl):
            path_with_namespace = project.path_with_namespace
            if not check_include(includes=scope_includes, path_with_namespace=path_with_namespace):
                continue
            gitlab_project, created = GitlabProject.objects.get_or_create(path_with_namespace=path_with_namespace)
