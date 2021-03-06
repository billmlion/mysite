from django.db import models
from django.db import connection,models

class UserProfileManager(models.Manager):
    def getUserProfile(self,name):
      cursor = connection.cursor()
      cursor.execute("select username,website,nickname from auth_user,books_publisher,books_info where books_publisher.id = auth_user.id and books_info.id = auth_user.id")
      return [row for row in cursor.fetchone()]

class BooksLogManager(models.Manager):
    """docstring for UserLogManager"""
    def getUserProfile(self,name):
      cursor = connection.cursor()
      cursor.execute("select username,log_info from auth_user,books_log where auth_user.id = books_log.id")
      return [row for row in cursor.fetchone()]
                    
class CCLogManager(models.Manager):
    """docstring for UserLogManager"""
    def getUserProfile(self,name):
      cursor = connection.cursor()
      cursor.execute("select username,log_info from auth_user,cc_log where auth_user.id = cc_log.id")
      return [row for row in cursor.fetchone()]    

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __unicode__(self):
      return self.name

class Author(models.Model):
    "author models is beginning..."
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    def __unicode__(self):
      return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    # num_page = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
      return self.title

class UserProfile(models.Model):
    nickname = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    website = models.CharField(max_length=200)
    objects = UserProfileManager()
    objects = models.Manager()
    upf_objects = UserProfileManager()
    bl_objects = BooksLogManager()
    ccl_objects = CCLogManager()


class Article(models.Model):
    headline = models.CharField(max_length=200, null=True, blank=True,
      help_text="Use puns liberally")
    content = models.TextField()

