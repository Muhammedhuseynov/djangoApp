from django.urls import path
from .views import home, PostDetail,post,PostDelteView
from users.views import register, profile
from django.contrib.auth import views as auth_views
from django.conf import settings
from .views import comments
from django.conf.urls.static import static
urlpatterns = [
    path('', home,name='home'),
    path('register/',register,name='register'),
    path('comments/',comments,name='comment'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('profile',profile,name='profile'),
    path('post/<int:pk>/',PostDetail.as_view(),name='post-detail'),
     path('post/<int:pk>/delete',PostDelteView.as_view(),name='post-delete'),
    path('postuser/',post,name='userpost'),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)