from django.db import models

# Create your models here.

#index PhotoLbum tables start
class IndexPhotoLbum(models.Model):
    imgnumber=models.IntegerField(primary_key=True)
    imgname=models.CharField(max_length=20,unique=True)
    imgtitle=models.CharField(max_length=50)
    image=models.ImageField(upload_to='indexphotolbum')
    def __unicode__(self):
        return u'%s' %self.imgname
    class Meta:
        db_table='indexphotolbum'

class IndexArticle(models.Model):
    articlenumber=models.IntegerField(primary_key=True)
    articlename=models.CharField(max_length=20,unique=True)
    articletitle=models.CharField(max_length=50)
    articlecontent=models.TextField()
    contentlink=models.CharField(max_length=20)
    def __unicode__(self):
        return u'%s' %self.articlename
    class Meta:
        db_table='indexarticle'

#about BottomPicture start
class AboutVitae(models.Model):
    vitaenumber=models.IntegerField(primary_key=True)
    vitaename=models.CharField(max_length=20,unique=True)
    vitaetitle=models.CharField(max_length=50)
    vitaeleft=models.TextField()
    vitaeright=models.TextField()
    def __unicode__(self):
        return u'%s' %self.vitaename
    class Meta:
        db_table='aboutvitae'

class AboutBottomPicture(models.Model):
    imgnumber=models.IntegerField(primary_key=True)
    imgname=models.CharField(max_length=20,unique=True)
    contentlink=models.CharField(max_length=20)
    images=models.ImageField(upload_to='aboutbottompicture')
    def __unicode__(self):
        return u'%s' %self.imgname
    class Meta:
        db_table='aboutbottompicture'

# tweets TweetsEssay start
class TweetsEssay(models.Model):
    essaynumber=models.IntegerField(primary_key=True)
    essayname=models.CharField(max_length=20,unique=True)
    essaytitle=models.CharField(max_length=50)
    essaycontent=models.TextField()
    essayimages=models.ImageField(upload_to='twwwtsessay')
    imagetitle=models.CharField(max_length=20)
    def __unicode__(self):
        return u'%s' %self.essayname
    class Meta:
        db_table='tweetsessay'