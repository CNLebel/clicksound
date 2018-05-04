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


#about BottomPicture start
class AboutBottomPicture(models.Model):
    imgnumber=models.IntegerField(primary_key=True)
    imgname=models.CharField(max_length=20,unique=True)
    contentlink=models.CharField(max_length=20)
    images=models.ImageField(upload_to='aboutbottompicture')
    def __unicode__(self):
        return u'%s' %self.imgname
    class Meta:
        db_table='aboutbottompicture'