from django.db import models
#导入内建的user模型
from django.contrib.auth.models import User
#timezone用于处理时间相关事物
from django.utils import timezone
# Create your models here.

class ArticlePost(models.Model):

	#文章作者，参数on_delete用于指定数据删除的方式，避免两个关联表的数据不一致
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	#文章标题，models.CharField为字符串字段，用于保存较短的字符串，例如标题
	title = models.CharField(max_length=100)
	#文章正文，保存大量文本用TextField
	body = models.TextField()
	#文章创建时间，括号内参数意思是创建数据时将默认写入当前时间
	created = models.DateTimeField(default=timezone.now)
	#文章更新时间，每次数据更新时自动写入当前时间
	updated = models.DateTimeField(auto_now=True)
 
	#内部类class meta用于给model定义元数据
	class Meta:
		#ordering 指定模型返回的数据的排列顺序
		#'-created'表明数据应该以倒叙排列
		ordering = ('-created',)

	#函数 __str__定义调用对象的 str方法时的返回值内容
	def __str__(self):
		#return self.title 将文章标题返回
		return self.title
#在python中缩进很重要，只用Table不用空格