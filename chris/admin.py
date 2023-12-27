from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Home)

class ProfileInline(admin.TabularInline):
    model = models.Profile
    extra = 1

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]

class SkillsInline(admin.TabularInline):
    model = models.Skills
    extra = 2

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
    ]

admin.site.register(models.Portfolio)