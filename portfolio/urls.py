from . import views
from django.urls import path
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('edu',views.education,name='edu'),
    path('exp',views.experience,name='exp'),
    path('skills',views.skills,name='skills'),
    path('project',views.project,name='project'),
    path('blog',views.blog,name='blog'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('qr-code/', views.generate_qr_code, name='generate_qr_code'),
]
