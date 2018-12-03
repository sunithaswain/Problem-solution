# Register your models here.
from django.contrib import admin
from .models import Contests,Colleges,Challenges,View_Stats,Submission_Stats

class Contest_model(admin.ModelAdmin):
    list_display= ('contest_id','hacker_id','name')
admin.site.register(Contests, Contest_model)

class College_model(admin.ModelAdmin):
    list_display =('college_id','contest_id')

    # readonly_fields = ('contest_id',)
    # def contest_id(self, obj):
    #     return obj.contest.id
    #search_fields = ['project']
admin.site.register(Colleges, College_model)

class challege_model(admin.ModelAdmin):
    list_display=('college_id','challenges_id')
    # = ['Department']
admin.site.register(Challenges,challege_model)

class View_model(admin.ModelAdmin):
    list_display=('challenges_id','total_views','total_uniqueviews')
    #search_fields = ['project_name']
admin.site.register(View_Stats,View_model)

class Submission_model(admin.ModelAdmin):
    list_display=('challenges_id','total_submission','total_accept_submission')
    #search_fields = ['project_name']
admin.site.register(Submission_Stats,Submission_model) 
