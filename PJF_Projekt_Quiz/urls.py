from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda req: redirect('/quizzes/')),
    path('admin/', admin.site.urls),
    path('quizzes/', include('quizzes.urls'))
]
