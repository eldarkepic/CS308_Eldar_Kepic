
from django.urls import path
from books import views
from django.urls import path, include


urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>', views.BookDetails.as_view()),
    path('books/', views.AuthorList.as_view()),
    path('books/<int:pk>/', views.AuthorDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
