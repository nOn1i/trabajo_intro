from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path('', views.feed, name='feed'),
	path('profile/', views.profile, name='profile'),
	path('profile/<str:username>/', views.profile, name='profile'),
	path('register/', views.register, name='register'),
	path('login/', LoginView.as_view(template_name='Pruebas/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='Pruebas/logout.html'), name='logout'),
	path('post/', views.post, name='post'),

	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
