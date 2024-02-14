import gitlab

from django.conf import settings


def get_gitlab_connection() -> gitlab.client.Gitlab:
    gl = gitlab.Gitlab(
        url=settings.GITLAB_URL,
        private_token=settings.GITLAB_PRIVATE_TOKEN,
        user_agen="leonosaurus",
    )
    gl.auth()
    if settings.DEBUG:
        gl.enable_debug()
    return gl
