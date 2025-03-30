from django.urls import path, include
from movies_app.api.views import ReviewList, ReviewDetail

urlpatterns = [
    path("review/list/", ReviewList.as_view(), name="review-list"),
    path("review/list/<int:pk>/", ReviewDetail.as_view(), name="review-details"),
]