from django.contrib import admin

from .models import Article, Rubric, Comment, Rating, RatingStar


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "name_author",
        "published",
        "rubric",
    )

    list_display_links = ("title", "content")
    search_fields = ("title", "content")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "article", "ip")


admin.site.register(Rubric)
admin.site.register(Comment)
admin.site.register(RatingStar)

admin.site.site_title = "Tehnoblog"
admin.site.site_header = "Tehnoblog"
