from django.db import models

class Article(models.Model):
    article_title = models.CharField('Название статьи',max_length=128)
    article_text = models.TextField("Текст статьи")
    def __str__(self):
        return self.article_title