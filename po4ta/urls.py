
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', AppointmentView.as_view(), name='news-list'),
]
