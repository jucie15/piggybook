from django.contrib import admin
from cast.models import *

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    max_num = 1
    min_num = 1

@admin.register(Contents)
class ContentsAdmin(admin.ModelAdmin):
    model = Contents
    inlines = [
        CommentInline,
    ]
    actions = ['delete_empty_contents']

    def delete_empty_contents(self, request, queryset):
        Contents.delete_empty_contents(queryset)
        self.message_user(request, "짤린 동영상 컨텐츠 삭제 성공.")
    delete_empty_contents.short_description = "짤린 동영상 컨텐츠를 삭제합니다."

class PledgeInline(admin.TabularInline):
    model = Pledge

@admin.register(Congressman)
class CongressmanAdmin(admin.ModelAdmin):
    model = Congressman
    search_fields = ('name', 'party', 'constituency')
    list_display = ['id', 'name', 'party', 'constituency', 'updated_at']
    inlines = [
        PledgeInline,
        CommentInline,
    ]
    list_display_links = ('id','name','party','constituency',)

@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    model = Pledge
    search_fields = ('title',)
    list_display = ['id', 'title', ]
    inlines = [
        CommentInline,
    ]

class ReCommentInline(admin.StackedInline):
    model = ReComment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    inlines = [
        ReCommentInline,
    ]

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    model = Favorite

@admin.register(ContentsEmotion)
class ContentsEmotionAdmin(admin.ModelAdmin):
    model = ContentsEmotion

@admin.register(CongressmanEmotion)
class CongressmanEmotionAdmin(admin.ModelAdmin):
    model = CongressmanEmotion

@admin.register(PledgeEmotion)
class PledgeEmotionAdmin(admin.ModelAdmin):
    model = PledgeEmotion
    search_fields = ('pledge__id', 'pledge__title', 'name')

@admin.register(CommentEmotion)
class CommentEmotionAdmin(admin.ModelAdmin):
    model = CommentEmotion

# admin.site.register(Contents)
# admin.site.register(Congressman)
# admin.site.register(Pledge)
# admin.site.register(ContentsEmotion)
# admin.site.register(PledgeEmotion)
# admin.site.register(CongressmanEmotion)
# admin.site.register(Comment)
# admin.site.register(CommentEmotion)
# admin.site.register(ReComment)
