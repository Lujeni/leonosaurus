from django.contrib import admin
from django.db import transaction
from functools import partial

from deploydocus.task import task_report
from deploydocus.models import (
    Rule,
    Policy,
    Scope,
    Report,
    ReportResult,
    GitlabProject,
    GitlabRule,
)


class RuleAdmin(admin.ModelAdmin):
    pass


class GitlabRuleAdmin(admin.ModelAdmin):
    pass


class PolicyAdmin(admin.ModelAdmin):
    pass


class ScopeAdmin(admin.ModelAdmin):
    pass


class ReportAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        transaction.on_commit(partial(task_report))
        return super().save_model(request, obj, form, change)


class ReportResultAdmin(admin.ModelAdmin):
    pass


class GitlabProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Scope, ScopeAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register(GitlabRule, RuleAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(ReportResult, ReportResultAdmin)
admin.site.register(GitlabProject, GitlabProjectAdmin)
