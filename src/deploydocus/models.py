from django.db import models
from django.utils.encoding import smart_str
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


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
    rules = models.ManyToManyField(Rule)

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
    include = models.CharField(max_length=300, default="*")
    exlude = models.CharField(max_length=300, blank=True, null=True)

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


class ReportResult(TimeStampedModel):
    STATUS = {
        "pending": "Pending",
        "running": "Running",
        "success": "Success",
    }
    status = models.CharField(max_length=300, choices=STATUS)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    def __str__(self):
        return smart_str(self.status, self.report)

    def __unicode__(self):
        return smart_str(self.status, self.report)

    class Meta:
        ordering = ["status"]
        verbose_name = _("Report result")
        verbose_name_plural = _("Report results")


class GitlabProject(TimeStampedModel):
    path_with_namespace = models.CharField(max_length=3000)

    def __str__(self):
        return smart_str(self.path_with_namespace)

    def __unicode__(self):
        return smart_str(self.path_with_namespace)

    class Meta:
        ordering = ["path_with_namespace"]
        verbose_name = _("Gitlab project")
        verbose_name_plural = _("Gitlab projects")
