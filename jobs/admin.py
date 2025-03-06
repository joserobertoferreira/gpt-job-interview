from django.contrib import admin

from jobs.models import Job, Skill


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'get_skills', 'created_at', 'updated_at')
    search_fields = ('title', 'level')
    list_filter = ('level', 'skills')

    @staticmethod
    @admin.display(description='Skills')
    def get_skills(obj):
        return ', '.join([skill.skill for skill in obj.skills.all()])


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill',)
    search_fields = ('skill',)
