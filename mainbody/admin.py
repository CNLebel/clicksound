#coding:utf-8
from django.contrib import admin
from mainbody.models import *
# Register your models here.

#index PhotoLbumAdmin start
class IndexPhotoLbumAdmin(admin.ModelAdmin):
    list_display = ['imgnumber','imgname','imgtitle','image']
    list_filter = ['imgnumber']
    search_fields = ['imgname']
    list_per_page = 4
    fieldsets = [
        ('图片信息', {'fields': ['imgnumber', 'imgname']}),
        ('图片标题', {'fields': ['imgtitle']}),
        ('图片', {'fields': ['image']}),
    ]
admin.site.register(IndexPhotoLbum,IndexPhotoLbumAdmin)

#about BottomPictureAdmin start
class AboutBottomPictureAdmin(admin.ModelAdmin):
    list_display = ['imgnumber','imgname','contentlink','images']
    list_filter = ['imgnumber']
    search_fields = ['imgname']
    list_per_page = 4
    fieldsets = [
        ('图片信息', {'fields': ['imgnumber', 'imgname']}),
        ('内容链接', {'fields': ['contentlink']}),
        ('图片', {'fields': ['images']}),
    ]
admin.site.register(AboutBottomPicture,AboutBottomPictureAdmin)