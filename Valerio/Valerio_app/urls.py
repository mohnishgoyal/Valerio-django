from django.urls import path
from Valerio_app import views

app_name = 'Valerio_app'

urlpatterns = [
    path('pages/app/', views.app, name="app"),
    path('pages/blog/', views.blog, name="blog"),
    path('pages/contact/', views.contact, name="contact"),
    path('pages/partners/', views.partners, name="partners"),
    path('pages/privacy/', views.privacy, name="privacy"),
    path('pages/team/', views.team, name="team"),
    path('pages/termsofuse/', views.termsofuse, name="termsofuse"),
]
