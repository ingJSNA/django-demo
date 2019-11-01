from django.contrib import admin

# Register your models here.
from college.models import Student, Score, Professor

admin.site.register(Student)
admin.site.register(Score)
admin.site.register(Professor)