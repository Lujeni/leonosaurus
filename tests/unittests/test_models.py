import pytest

from deploydocus.factories import GitlabProjectFactory, GitlabRuleFactory


@pytest.mark.django_db
def test_gitlab_rule_is_compliant():
    project = GitlabProjectFactory()
    rule = GitlabRuleFactory()
    assert rule.is_compliant(project=project)


@pytest.mark.django_db
def test_gitlab_rule_is_compliant_bad():
    project = GitlabProjectFactory()
    rule = GitlabRuleFactory(expected="ff")
    assert not rule.is_compliant(project=project)


@pytest.mark.django_db
def test_gitlab_rule_is_compliant_not_implemented():
    project = GitlabProjectFactory()
    rule = GitlabRuleFactory(attribut="unknown")
    with pytest.raises(Exception):
        assert rule.is_compliant(project=project)
