from django.contrib import admin
from learn_dj.models import Article, UserMessage, TextNew, LedMod_GTR2416, ArticleBox, PhotoView

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'text', 'code')

class UserMessageAdmin(admin.ModelAdmin):
	list_display = ('user_name', 'public_message', 'comment', 'email', 'admin_answer', 'date_of_note')

class TextNewAdmin(admin.ModelAdmin):
	list_display = ('name', 'text', 'image', 'link', 'date')

class LedMod_GTR2416Admin(admin.ModelAdmin):
	list_display = ('numb', 'sub_title', 'text', 'image', 'link')

class ArticleBoxAdmin(admin.ModelAdmin):
	list_display = ('title', 'sub_title', 'image', 'text')

class PhotoViewAdmin(admin.ModelAdmin):
	list_display = ('name', 'text_1', 'image_1')


admin.site.register(Article, ArticleAdmin)
admin.site.register(UserMessage, UserMessageAdmin)
admin.site.register(TextNew, TextNewAdmin)
admin.site.register(LedMod_GTR2416, LedMod_GTR2416Admin)
admin.site.register(ArticleBox, ArticleBoxAdmin)
admin.site.register(PhotoView, PhotoViewAdmin)
