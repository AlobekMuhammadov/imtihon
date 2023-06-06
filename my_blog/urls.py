
from django.contrib import admin
from django.urls import path
from maqolapp.views import *
from userapp.views import *
from userapp.views import RegisterTwoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('blog/', BlogView.as_view(),name='blog'),
    # path('blog/<int:pk>/', BittaBlog),
    path('register2/', RegisterTwoView.as_view(),name='register2'),
    path('register/', RegisterView.as_view(),name='register'),
]
