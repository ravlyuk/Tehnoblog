from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import api

article = api.ArticleModelViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

article_detail = api.ArticleModelViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
    'put': 'update',
    'path': 'partial_update',
})

article_like = api.ArticleLikeCreateView.as_view({
    'post': 'like',
})

rubric_detail = api.ArticleModelViewSet.as_view({
    'get': 'by_rubric',
})

urlpatterns = format_suffix_patterns([
    path('article/', article, name="article"),
    path('article/<int:pk>/', article_detail, name="article_detail"),
    path('comment/', api.CommentCreateViewSet.as_view({'post': 'create'})),
    path('comment/<int:pk>/', api.CommentViewSet.as_view({'get': 'retrieve'})),
    path('rubric/', api.RubricModelViewSet.as_view({'get': 'list'})),
    path('rubric/<int:pk>/', rubric_detail),
    path('rating/', api.AddStarRatingViewSet.as_view({'post': 'create'})),
    path('rating/<int:pk>/', api.RatingModelViewSet.as_view({'get': 'list'})),
    path('like/', article_like, name="article_like"),
])
