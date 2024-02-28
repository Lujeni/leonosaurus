import factory


class GitlabProjectFactory(factory.django.DjangoModelFactory):
    merge_method = "merge"

    class Meta:
        model = 'deploydocus.GitlabProject'


class GitlabRuleFactory(factory.django.DjangoModelFactory):
    attribut = "merge_method"
    expected = "merge"

    class Meta:
        model = 'deploydocus.GitlabRule'
