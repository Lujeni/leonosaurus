from django.db import models

class MergeMethodChoices(models.TextChoices):
    FF = "ff"
    MERGE = "merge"
    REBASE_MERGE = "rebase_merge"


class AttributChoices(models.TextChoices):
    merge_method = "merge_method"


