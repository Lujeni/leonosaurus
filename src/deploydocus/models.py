from django.db import models
from django.utils.encoding import smart_str
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

from deploydocus.enums import MergeMethodChoices, AttributChoices


class GitlabProject(TimeStampedModel):
    path_with_namespace = models.CharField(max_length=3000)
    merge_method = models.CharField(max_length=30, choices=MergeMethodChoices.choices)

    def __str__(self):
        return smart_str(self.path_with_namespace)

    def __unicode__(self):
        return smart_str(self.path_with_namespace)

    class Meta:
        ordering = ["path_with_namespace"]
        verbose_name = _("Gitlab project")
        verbose_name_plural = _("Gitlab projects")


class GitlabRule(TimeStampedModel):
    name = models.CharField(max_length=300)
    attribut = models.CharField(max_length=30, choices=AttributChoices.choices)
    # TODO: we should propose another enum based on attribe choice
    expected = models.CharField(max_length=300)

    def __str__(self):
        return smart_str(self.name)

    def __unicode__(self):
        return smart_str(self.name)

    def is_compliant(self, project: GitlabProject) -> bool:
        if not hasattr(project, self.attribut):
            raise Exception(self.attribut)
        return getattr(project, self.attribut) == self.expected

    class Meta:
        ordering = ["name"]
        verbose_name = _("GitLab Rule")
        verbose_name_plural = _("GitLab Rules")


class Rule(TimeStampedModel):
    ACTIONS = {
        "file_exist": "File exist",
    }
    name = models.CharField(max_length=100)
    action = models.CharField(max_length=300, choices=ACTIONS)
    parameters = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return smart_str(self.name)

    def __unicode__(self):
        return smart_str(self.name)

    class Meta:
        ordering = ["name"]
        verbose_name = _("Rule")
        verbose_name_plural = _("Rules")


class Policy(TimeStampedModel):
    name = models.CharField(max_length=100)
    rules = models.ManyToManyField(Rule, blank=True)
    gitlab_rules = models.ManyToManyField(GitlabRule, blank=True)

    def __str__(self):
        return smart_str(self.name)

    def __unicode__(self):
        return smart_str(self.name)

    class Meta:
        ordering = ["name"]
        verbose_name = _("Policy")
        verbose_name_plural = _("Policies")


class Scope(TimeStampedModel):
    name = models.CharField(max_length=100)
    include = models.CharField(max_length=300, default=".*")
    exclude = models.CharField(max_length=300, blank=True, null=True)
    gitlab_projects = models.ManyToManyField(GitlabProject, blank=True)

    def __str__(self):
        return smart_str(self.name)

    def __unicode__(self):
        return smart_str(self.name)

    class Meta:
        ordering = ["name"]
        verbose_name = _("Scope")
        verbose_name_plural = _("Scopes")


class Report(TimeStampedModel):
    name = models.CharField(max_length=100)
    policies = models.ManyToManyField(Policy)
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)

    def __str__(self):
        return smart_str(self.name)

    def __unicode__(self):
        return smart_str(self.name)

    class Meta:
        ordering = ["name"]
        verbose_name = _("Report")
        verbose_name_plural = _("Reports")

    def check_compliance(self):
        ReportResult.objects.create(report=self)
        for project in self.scope.gitlab_projects.all():
            for policy in self.policies.all():
                for _ in policy.rules.all():
                    continue
                for gitlab_rule in policy.gitlab_rules.all():
                    gitlab_rule.is_compliant(project=project)


class ReportResult(TimeStampedModel):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    def __str__(self):
        return smart_str(self.report)

    def __unicode__(self):
        return smart_str(self.report)

    class Meta:
        ordering = ["report"]
        verbose_name = _("Report result")
        verbose_name_plural = _("Report results")
