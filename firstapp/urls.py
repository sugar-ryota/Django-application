from django.urls import path
from . import views

app_name = 'firstapp'

urlpatterns = [
#     path('hello', views.index, name='index'),  #firstapp/helloにアクセスするとviews.pyのindexが呼ばれる
#     path('page/<str:user_name>', views.user_page, name='user_name'),  # page/taroみたいな感じ user_nameは引数(views.pyのuser_name関数参照)
#     path('number_page/<str:user_name>/<int:number>', views.number_page, name='number_name'),
    path('', views.index, name='index'),
    path('home',views.home,name='home')
]