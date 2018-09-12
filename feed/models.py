from django.db import models

class Article(models.Model):
    DEVELOPMENT="dv"
    PERSONAL="ps"
    CATEGORY_CHOICES=(
            (DEVELOPMENT,"development"),
            (PERSONAL,"personal"),
            )
    title=models.CharField(max_length=20)
    content=models.TextField()
    category=models.CharField(max_length=2,
            choices=CATEGORY_CHOICES,
            default=DEVELOPMENT,)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    content=models.CharField(max_length=200)

    def __str__(self):
        return self.article, self.username

class HashTag(models.Model):
    name=models.CharField(max_length=20)
