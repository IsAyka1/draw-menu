from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from my_menu import views


urlpatterns = [
    path('menu/menu5', views.another, name='another'),
    path('<path:url>?<str:selected>', views.show_selected, name='select'),
    # path('<path:url>', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
