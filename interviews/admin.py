from django.contrib import admin

from interviews.models import Chat, Message


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('title', 'job', 'completed', 'created_at', 'updated_at')
    inlines = (MessageInline,)
