from django.contrib import admin

from deploydocus.models import Rule, Policy, Scope, Report, ReportResult, GitlabProject


class RuleAdmin(admin.ModelAdmin):
    pass


class PolicyAdmin(admin.ModelAdmin):
    pass


class ScopeAdmin(admin.ModelAdmin):
    pass


class ReportAdmin(admin.ModelAdmin):
    pass


class ReportResultAdmin(admin.ModelAdmin):
    pass


class GitlabProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Scope, ScopeAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(ReportResult, ReportResultAdmin)
admin.site.register(GitlabProject, GitlabProjectAdmin)
