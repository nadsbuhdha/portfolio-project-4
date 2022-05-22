""" apps """

from django.apps import AppConfig


class ReviewConfig(AppConfig):
    """ review app configuration """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'review'
