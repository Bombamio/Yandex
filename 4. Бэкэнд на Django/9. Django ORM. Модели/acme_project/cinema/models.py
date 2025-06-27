# cinema/models.py
from django.db import models

class OriginalTitle(models.Model):
    title = models.CharField(max_length=128)

class VideoProduct(models.Model):
    title = models.CharField(max_length=128)
    # Описываем поле, ссылающееся на модель OriginalTitle:
    original_title = models.OneToOneField(
        # На какую модель ссылаемся
        OriginalTitle,
        # Поведение при удалении:
        # если оригинальное имя будет удалено,
        # то и сам фильм будет удалён. 
        on_delete=models.CASCADE
    )
