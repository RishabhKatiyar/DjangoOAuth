from django.contrib import admin
from .models import Assignment, GradedAssignment, Choice, Question

admin.site.register(Assignment)
admin.site.register(GradedAssignment)
admin.site.register(Choice)
admin.site.register(Question)
