#ÒýÈëpath
from django.urls import path
#引入views.py
from . import views
#ÕýÔÚ²¿ÊðµÄÓ¦ÓÃµÄÃû³Æ
app_name = 'article'

#Ä¿Ç°»¹Ã»ÓÐurls
urlpatterns = [
	#path函数将url映射到视图
	path('article-list/',views.article_list,name='article_list'),
	#文章详情
	path('article-detail/<int:id>/',views.article_detail,name='article_detail'),
	path('article-create/', views.article_create, name='article_create'),
	path('article-detail/<int:id>/',views.article_delete,name='article_delete'),
    path('article-update/<int:id>/',views.article_update,name='article_update'),
]