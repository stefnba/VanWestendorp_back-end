from django.contrib import admin

from .models import Input_Answer, Input_User, Question, Question_Type, Project, Input_Title, VW_Input_Type

admin.site.register(Input_Answer)
admin.site.register(Project)
admin.site.register(Input_Title)
admin.site.register(Question)
admin.site.register(Question_Type)
admin.site.register(Input_User)
admin.site.register(VW_Input_Type)

