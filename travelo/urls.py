from django.contrib import admin
from django.urls import path
from travelservices import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tra', views.tra),
    path('show',views.show),
    path('about', views.about),
    path('show',views.show),
    path('blog', views.blog),
    path('show',views.show),
    path('contact', views.contact),
    path('show',views.show),
    path('contact_process', views.contact_process),
    path('show',views.show),
    path('destination_details', views.destination_details),
    path('show',views.show),
    path('elements', views.elements),
    path('show',views.show),


    path('singleblog',views.singleblog),
    path('show',views.show),
    path('travel_destination', views.travel_destination),
    path('show',views.show),


    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]

