from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Article, Rubric, Comment, Rating
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, renderers, permissions
from .service import get_client_ip
from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsSuperUser

from .serializers import (
    ArticleSerialazer,
    RubricListSerialazer,
    CommentSerializer,
    CommentCreateSerializer,
    CreateRatingSerializer,
    RatingDetailSerializer,
    LikeCreateSerializer,
    CreateUpdateArticleSerialazer,
)

from .service import PaginationArticles


class ArticleModelViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    pagination_class = PaginationArticles

    def get_queryset(self):
        articles = Article.objects.filter().annotate(
            rating_user=models.Count("ratings",
                                     filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        ).order_by('-published')

        return articles

    @action(detail=False, pagination_class=PaginationArticles)
    def by_rubric(self, request, pk=None):
        queryset = Article.objects.filter(rubric__pk=pk).annotate(
            rating_user=models.Count("ratings",
                                     filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        ).order_by('-published')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateUpdateArticleSerialazer
        return ArticleSerialazer

    def get_permissions(self):
        permission_classes = [permissions.AllowAny]  # default permission
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        elif self.action in ['destroy', 'create']:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class RubricModelViewSet(viewsets.ModelViewSet):
    serializer_class = RubricListSerialazer
    queryset = Rubric.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentCreateViewSet(viewsets.ModelViewSet):
    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.all()

    def get_permissions(self):
        permission_classes = [permissions.IsAdminUser]
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class RatingModelViewSet(viewsets.ModelViewSet):
    serializer_class = RatingDetailSerializer
    queryset = Rating.objects.all()

    def get(self, pk):
        rating = Rating.objects.filter(article__name=pk)
        return rating


class AddStarRatingViewSet(viewsets.ModelViewSet):
    """Добавление рейтинга фильму"""
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


class ArticleLikeCreateView(viewsets.ModelViewSet):
    serializer_class = LikeCreateSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, *args, **kwargs):
        id_article = request.data["id_article"]
        if id_article.isdigit():
            id_article = int(id_article)
            currently_count = Article.objects.get(pk=id_article).likes
            Article.objects.filter(pk=id_article).update(likes=currently_count + 1)
            return Response({"voices": Article.objects.get(pk=id_article).likes})
        else:
            return Response("error: incorrect id")
