from django.urls import path

from app.views import ArtCreateApiView, ArtGetApiView

urlpatterns = [
    path('articles/create/', ArtCreateApiView.as_view()),
    path('articles/', ArtGetApiView.as_view())
]
