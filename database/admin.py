from django.contrib import admin
from database.models import GliaUser, GliaCounselor, GliaConversation
# Register your models here.


class GliaUserAdmin(admin.ModelAdmin):
    search_fields = ['username']

admin.site.register(GliaUser,GliaUserAdmin)
admin.site.register(GliaCounselor)
admin.site.register(GliaConversation)