import logging

logger = logging.getLogger("paperless.auth")


# https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.signals.user_login_failed
def handle_failed_login(sender, credentials, request, **kwargs):
    ip = request.META.get("REMOTE_ADDR")
    if request.META.get("HTTP_X_FORWARDED_FOR"):
        ip = request.META.get("HTTP_X_FORWARDED_FOR").split(",")[0]
    logger.info(
        f"Login failed for user `{credentials['username']}` from IP `{ip}`",
    )
