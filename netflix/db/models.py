from django.db import models


class PublishStateOptions(models.TextChoices):
        # Constant = DB_value , USER_DISPLAY_VA
        # UNLISTED = 'UN','Unlisted'
        PUBLISH = 'PU','Published'
        DRAFT = 'DR','Draft'