#引入redirect重定向模块
from django.shortcuts import render,redirect
#导入数据模型ArticlePost
from .models import ArticlePost
# Create your views here.
#引入HttpResponse
from django.http import HttpResponse
#引入刚才定义的ArticlePostForm表单类
from .forms import ArticlePostForm
#引入User模型
from django.contrib.auth.models import User
#引入markdown模块
import markdown

from django.contrib.auth.decorators import login_required
#视图函数
def article_list(request):
	#return HttpResponse("Hello World!")
	#取出所有博客文章
	articles = ArticlePost.objects.all()
	#需要传递给模板（templates）的对象
	context = {'articles':articles}
    #render函数：载入模板，并返回context对象
	return render(request,'article/list.html',context)


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    context = { 'article': article }
    return render(request, 'article/detail.html', context)
@login_required(login_url='/userprofile/login/')
def article_create(request):
	if request.method == "POST":
		article_post_form = ArticlePostForm(data=request.POST)
		if article_post_form.is_valid():
			new_article = article_post_form.save(commit=False)
			new_article.author = User.objects.get(id=request.user.id)
			new_article.save()
			return redirect("article:article_list")
		else:
			return HttpResponse("表单内容有误，请重新填写。")
	else:
		article_post_form = ArticlePostForm()
		context = {'article_post_form': article_post_form }
		return render(request,'article/create.html',context)

def article_delete(request,id):
	#根据id获取需要删除的文章
	article = ArticlePost.objects.get(id=id)
	#调用.delete（）方法删除文章
	article.delete()
	#完成删除后返回文章列表
	return redirect("article:article_list")
	
	#g更新文章
def article_update(request,id):
    #获取需要更改的具体文章对象
    article = ArticlePost.objects.get(id=id)
    #判断用户是否为POST提交表单数据
    if request.method == "POST":
    	#将提交的数据赋给表单实例
    	article_post_form = ArticlePostForm(data=request.POST)
    	#判断提交的数据是否满足模型的要求
    	if article_post_form.is_valid():
    		#保存新写入的title,body数据并保存
    		article.title=request.POST['title']
    		article.body = request.POST['body']
    		article.save()
    		#完成后返回到修改后的文章中，需传入文章的id
    		return redirect("article:article_detail",id=id)
    	else:
    		#如果数据不合法，返回错误信息
    		return HttpResponse("表单内容有误，请重新填写。")
    #如果用户GET请求获取数据
    else:
    	#创建表单类实例
    	article_post_form = ArticlePostForm();
    	#赋值上下文，将article文章对象也传递进去，以便提取旧的内容
    	context = {'article':article,'article_post_form':article_post_form}
    	#将响应返回到模板中
    	return render(request,'article/update.html',context)
    	
			
