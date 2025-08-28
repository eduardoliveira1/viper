from company import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('dashboard/', views.company_dashboard, name='company_dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # {% if company %}
    #     <div class="company-dashboard">
    #         <a href="{% url 'company_dashboard' %}" class="btn">
    #             <i class="fa fa-building"></i> Your Company
    #         </a>
    #     </div>
    # {% endif %} 