from django.db import models

class Article(models.Model):
    DEVELOPMENT="dv"
    PERSONAL="ps"
    CATEGORY_CHOICES=(
            (DEVELOPMENT,"development"),
            (PERSONAL,"personal"),
            )
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20)
    content=models.TextField()
    category=models.CharField(max_length=2,
            choices=CATEGORY_CHOICES,
            default=DEVELOPMENT,)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article=models.ForeignKey(
        Article,
        related_name="article_comments",
        on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    content=models.CharField(max_length=200)
    id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.username

class HashTag(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Lotto(models.Model):
    id=models.AutoField(primary_key=True)
    day=models.TextField()
    lotto=models.TextField()

    def __str__(self):
        return self.day
