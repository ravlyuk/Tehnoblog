from rest_framework import serializers
from .models import Article, Comment, Rubric, Rating


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class FilterCommentListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class CommentCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Comment
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """Вывод отзывов"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = (
            'id',
            'name',
            'content',
            'published',
            'article',
            'children',
        )


class RatingDetailSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""

    class Meta:
        model = Rating
        fields = '__all__'


class ArticleSerialazer(serializers.ModelSerializer):
    """ Статьи """
    comments = CommentSerializer(many=True)
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
            'name_author',
            'rubric',
            'published',
            'likes',
            'rating_user',
            'middle_star',
            'picture',
            'comments',
        )


class CreateUpdateArticleSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
            'name_author',
            'rubric',
            'published',
            'picture',
        )


class RubricListSerialazer(serializers.ModelSerializer):
    """ Рубрики """

    class Meta:
        model = Rubric
        fields = ('id', 'name',)


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""

    class Meta:
        model = Rating
        fields = ("star", "article")

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            article=validated_data.get('article', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating


class LikeCreateSerializer(serializers.ModelSerializer):
    id_article = serializers.Field(source="has_expired", )

    class Meta:
        model = Article
        fields = ("id_article",)
