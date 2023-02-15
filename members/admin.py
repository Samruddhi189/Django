from django.contrib import admin
from .models import Member, Teacher
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "mobile_no", "joined_date")

# Register your models here.
admin.site.register(Member, MemberAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "age", "mobile_no")

admin.site.register(Teacher, TeacherAdmin)
