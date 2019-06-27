from django.contrib import admin

# Register your models here.
from polls.models import Poll, Choice


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    fields = ["question", "created_by", "pub_date"]
    readonly_fields = ["pub_date"]

admin.site.register(Choice)