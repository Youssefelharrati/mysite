from django.urls import path
from .views import (AboutView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, DraftListView,
                    add_comment, comment_approve, remove_comment, pub_post)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),

    path('about/', AboutView.as_view(), name='about'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('post/new/', PostCreateView.as_view(), name='post_new'),

    path('post/<int:pk>/publish',pub_post , name='post_publish'),

    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_edit'),

    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),

    path('darft/', DraftListView.as_view(), name='draft_list'),

    path('post/<int:pk>/comment', add_comment, name='add_comment'),

    path('comment/<int:pk>/approve', comment_approve, name='comment_approve'),

    path('comment/<int:pk>/remove', remove_comment, name='comment_remove'),

]