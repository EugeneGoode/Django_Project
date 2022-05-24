from Django.urls import path
from .views import *

app_name = 'application'
urlpatterns = [
    path('', boards, name ='boards'),
    path('<str:path>/', board, name = 'board'),
    path('thread/<int:path>/', thread, name = 'thread')
]

