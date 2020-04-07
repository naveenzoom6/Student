from django.contrib import admin
from app.models import StudentModel


@admin.register(StudentModel)
class MyAdmin(admin.ModelAdmin):
    list_display = ("name","cno","email","timeing","photo1","photo2","t_date")
    list_filter = ('timeing', )


