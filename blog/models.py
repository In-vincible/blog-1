
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Category(models.Model):
	name = models.CharField(u'Category', max_length=64)

	class Meta:
		ordering = ['-id']


	def __str__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return ('category',(), {'pk': self.pk})


class Post(models.Model):
    title = models.CharField(u"title", max_length=128)
    author = models.ForeignKey(User)
    content = models.TextField(u"content")
    pub_date = models.DateTimeField(auto_now_add=True)
    po_type = models.ForeignKey(Category, verbose_name=u'Category', blank=True, null=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'pk': self.pk})
        # return reverse('post',(), {'pk':self.pk})

class About(models.Model):
	title = models.CharField(u"title", max_length=20, default="About me")
	content =  models.TextField(u"content")
	pub_date = models.DateTimeField(auto_now_add=True)




		