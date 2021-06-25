from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from authors.views import PostView,GetView,PostViewBook,GetViewBook, GetViewBookAuthor,DeleteViewAuthor,DeleteViewBook,PutViewAuthor,PutViewBook,PatchViewAuthor,PatchViewBook
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authors/',PostView.as_view(),name='post'),
    path('api/authors_list/',GetView.as_view(),name='get'),
    path('api/books/',PostViewBook.as_view(),name='postbook'),
    path('api/books_list/',GetViewBook.as_view(),name='getbook'),
    path('api/authors/<int:pk>/',GetViewBookAuthor.as_view(),name='getbookauthor'),
    path('api/authors/delete/<int:pk>/',DeleteViewAuthor.as_view(),name='deleteauthor'),
    path('api/books/delete/<int:pk>/',DeleteViewBook.as_view(),name='deletebook'),
    path('api/authors/update/<int:pk>/',PutViewAuthor.as_view(),name='putauthor'),
    path('api/books/update/<int:pk>/',PutViewBook.as_view(),name='putbook'),
    path('api/authors/patch/<int:pk>/',PatchViewAuthor.as_view(),name='patchauthor'),
    path('api/books/patch/<int:pk>/',PatchViewBook.as_view(),name='patchbook'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
]