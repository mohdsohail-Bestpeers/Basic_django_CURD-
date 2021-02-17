from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.BlogView, name='BlogView'),
    path('update/<int:pk>/',views.UpdateBlog, name='update'),
    path('delete/<int:pk>/',views.DeleteBlog, name='delete')
]