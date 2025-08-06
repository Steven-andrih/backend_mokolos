from django.urls import path
from .views import CommentView, GetHistoryCommentHolydayView, GetHistoryCommentPermissionView

urlpatterns = [
    path('', CommentView.as_view(), name='comment_api'),
    path('commentHolyday/<int:pk>/', GetHistoryCommentHolydayView.as_view(), name='history_comment_holyday'),
    path('commentPermission/<int:pk>/', GetHistoryCommentPermissionView.as_view(), name='history_comment_permission'),

]
