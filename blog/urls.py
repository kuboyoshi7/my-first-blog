from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

# <int:pk> – この部分はトリッキーです。これはDjangoは整数の値を期待し、その値がpkという名前の変数で
# ビューに渡されることを意味しています。
# / – それからURLの最後に再び / が必要です。
# つまり、ブラウザにhttp://127.0.0.1:8000/post/5/を入力すると、Djangoはpost_detailというビューを
# 探していると理解します。そしてpkが5という情報をそのビューに転送します
# https://tutorial.djangogirls.org/ja/extend_your_application/
