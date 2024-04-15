from django.contrib import admin
from core.models import Post, Gallery, FriendRequest, Friend, Comment, ReplyComment, Notification, Group, GroupPost, Page, PagePost, ChatMessage


# add many images in the post
class GalleryAdminTab(admin.TabularInline):
    model = Gallery


class FriendRequestAdmin(admin.ModelAdmin):
    list_editable = ['status']
    list_display = ['sender', 'receiver', 'status']


class FriendAdmin(admin.ModelAdmin):
    list_display = ['user', 'friend']


class CommentTabAdmin(admin.TabularInline):
    model = Comment

class ReplyCommentTabAdmin(admin.TabularInline):
    model = ReplyComment


class GroupPostTabAdmin(admin.TabularInline):
    model = GroupPost

class PagePostTabAdmin(admin.TabularInline):
    model = PagePost




class NotificationAamin(admin.ModelAdmin):
    list_display = ['user', 'sender', 'post', 'comment', 'notification_type', 'is_read']


class PostAdmin(admin.ModelAdmin):
    # allow add many images in the post
    inlines = [GalleryAdminTab]
    list_editable = ['active']
    list_display = ['thumbnail', 'user', 'title', 'visibility', 'active']
    prepopulated_fields = {'slug': ('title', )}


class GalleryAdmin(admin.ModelAdmin):
    list_editable = ['active']
    list_display = ['thumbnail', 'post', 'active']


class CommentAdmin(admin.ModelAdmin):
    inlines = [ReplyCommentTabAdmin]
    list_display = ['user', 'post', 'comment', 'active']


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'active']


class GroupAdmin(admin.ModelAdmin):
    # inlines = [GroupPostTabAdmin]
    list_editable = ['user', 'name', 'visibility']
    list_display = ['thumbnail', 'user', 'name', 'visibility']
    prepopulated_fields = {"slug": ("name", )}

class PageAdmin(admin.ModelAdmin):
    # inlines = [PagePostTabAdmin]
    list_editable = ['user', 'name', 'visibility']
    list_display = ['thumbnail', 'user', 'name', 'visibility']
    prepopulated_fields = {"slug": ("name", )}
    

class ChatMessageAdmin(admin.ModelAdmin):
    list_editable = ['message']
    list_display = ['sender', 'reciever', 'message', 'is_read']


admin.site.register(Post, PostAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ReplyComment, ReplyAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)
admin.site.register(Notification, NotificationAamin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(GroupPost)
admin.site.register(PagePost)
admin.site.register(ChatMessage, ChatMessageAdmin)
