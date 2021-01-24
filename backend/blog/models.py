from django.db import models
from django.urls import reverse


class Rubric(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = "Рубрика"
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(null=True, blank=True, verbose_name="Текст статьи")
    name_author = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Имя автора"
    )
    published = models.DateTimeField(
        auto_now=True, db_index=True, verbose_name="Опубликовано"
    )
    likes = models.IntegerField(
        null=False, blank=True, default=0, verbose_name="Понравилось"
    )
    rubric = models.ForeignKey(
        Rubric, null=True, on_delete=models.PROTECT, verbose_name="Рубрика", related_name='rubric_name'
    )

    picture = models.ImageField("Изображение", null=False, default="article/default/750x300.png", upload_to="article/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={"slug": self.title})

    class Meta:
        verbose_name_plural = "Статьи"
        verbose_name = "Статья"
        ordering = ["-published"]


class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя")
    content = models.TextField(verbose_name="Комментарий")
    published = models.DateTimeField(
        auto_now=True, db_index=True, verbose_name="Опубликовано"
    )
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name="children"
    )
    article = models.ForeignKey(
        Article,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Статья",
        related_name="comments",
    )

    def __str__(self):
        return self.content[:20] + ".."

    class Meta:
        verbose_name_plural = "Комментарии"
        verbose_name = "Комментарий"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name="Статья",
        related_name="ratings"
    )

    def __str__(self):
        return f"{self.star} - {self.article}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
