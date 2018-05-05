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

class IndexArticleAdmin(admin.ModelAdmin):
    list_display = ['articlenumber', 'articlename', 'articletitle', 'articlecontent','contentlink']
    list_filter = ['articlenumber']
    search_fields = ['articlename']
    list_per_page = 10
    fieldsets = [
        ('头条信息', {'fields': ['articlenumber','articlename']}),
        ('头条标题', {'fields': ['articletitle']}),
        ('头条内容', {'fields': ['articlecontent','contentlink']}),
    ]


admin.site.register(IndexArticle,IndexArticleAdmin)
admin.site.register(IndexPhotoLbum,IndexPhotoLbumAdmin)



#about BottomPictureAdmin start
class AboutVitaeAdmin(admin.ModelAdmin):
    list_display = ['vitaenumber', 'vitaename', 'vitaetitle', 'vitaeleft','vitaeright']
    list_filter = ['vitaenumber']
    search_fields = ['vitaename']
    list_per_page = 1
    fieldsets = [
        ('简历信息', {'fields': ['vitaenumber', 'vitaename']}),
        ('简历标题', {'fields': ['vitaetitle']}),
        ('简历内容', {'fields': ['vitaeleft','vitaeright']}),
    ]

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

admin.site.register(AboutVitae)
admin.site.register(AboutBottomPicture,AboutBottomPictureAdmin)



#tweets TweetsEssayAdmin start
class TweetsEssayAdmin(admin.ModelAdmin):
    list_display = ['essaynumber','essayname','essaytitle','essaycontent','essayimages','imagetitle']
    list_filter = ['essaynumber']
    search_fields = ['essayname']
    list_per_page = 10
    fieldsets = [
        ('文章信息', {'fields': ['essaynumber', 'essayname']}),
        ('文章内容', {'fields': ['essaytitle','essaycontent']}),
        ('文章图片', {'fields': ['essayimages','imagetitle']}),
    ]
admin.site.register(TweetsEssay,TweetsEssayAdmin)