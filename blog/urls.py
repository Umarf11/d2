from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register("blogs", views.BlogView, basename="blog")
# router.register("comments", views.CommentView, basename="comment")


urlpatterns = [
    path('blogs/', views.BlogView.as_view()),
    path('comments/', views.CommentView.as_view()),

    # path("", include(router.urls)),
]
