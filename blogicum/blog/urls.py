from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'posts/create/',
        views.create_post,
        name='create_post'
    ),
    path(
        'posts/<int:pk>/edit/',
        views.PostUpdateView.as_view(),
        name='edit_post'
    ),
    path(
        'posts/<int:pk>/delete/',
        views.delete_post,
        name='delete_post'
    ),
    path(
        'posts/<int:pk>/',
        views.post_detail,
        name='post_detail'
    ),

    path(
        'edit_profile/',
        views.ProfileEditView.as_view(),
        name='edit_profile'
    ),
    path(
        'posts/<int:id>/comment/',
        views.add_comment,
        name='add_comment'
    ),
    path(
        'posts/<int:post_id>/edit_comment/<int:comment_id>/',
        views.edit_comment,
        name='edit_comment'
    ),
    path(
        'posts/<int:post_id>/delete_comment/<int:comment_id>/',
        views.delete_comment,
        name='delete_comment'
    ),

    path('profile/<str:username>/', views.profile, name='profile'),
    path(
        'category/<slug:category_slug>/',
        views.category_posts,
        name='category_posts'
    ),
    path(
        'auth/registration',
        view=views.RegisterUser.as_view(),
        name='registration'
    )

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
