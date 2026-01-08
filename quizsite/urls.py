from django.contrib import admin
from django.urls import path
from main.views import welcome, start_quiz, question, result
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
    path('start/', start_quiz, name='start_quiz'),
    path('question/', question, name='question'),
    path('result/', result, name='result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)