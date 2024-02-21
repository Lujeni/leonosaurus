import gitlab

from django.conf import settings


def get_gitlab_connection() -> gitlab.client.Gitlab:
    gl = gitlab.Gitlab(
        url=settings.GITLAB_URL,
        private_token=settings.GITLAB_PRIVATE_TOKEN,
        user_agent="leonosaurus",
    )
    gl.auth()
    return gl


def get_projects(gl: gitlab.client.Gitlab) -> list:
    return gl.projects.list()
