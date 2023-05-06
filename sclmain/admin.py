from django.contrib import admin
from django.forms import inlineformset_factory
from .models import *

# Register your models here.


class MarksInline(admin.TabularInline):
    model = Marks
    extra = 7  # set the number of Marks objects to display (in this case, 7)


class StudentAdmin(admin.ModelAdmin):
    inlines = [MarksInline]


admin.site.register(Student, StudentAdmin)

admin.site.register(ClassRoom)
admin.site.register(Subject)
# admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Marks)
admin.site.register(SchoolDetails)
admin.site.register(ContactDetails)
