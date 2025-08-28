from user import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from user import profile_urls

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signUp, name='signup'),
    path('profile/', include('user.profile_urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)