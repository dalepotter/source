from django.contrib import admin

from .models import TechnologyTag, TechnologyTaggedItem, ConceptTag, ConceptTaggedItem, DataTag, DataTaggedItem, SkillTag, SkillTaggedItem, ThemeTag, ThemeTaggedItem, StatusTag, StatusTaggedItem


class TechnologyTaggedItemInline(admin.StackedInline):
    model = TechnologyTaggedItem

class TechnologyTagAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [
        TechnologyTaggedItemInline
    ]

class ConceptTaggedItemInline(admin.StackedInline):
    model = ConceptTaggedItem

class ConceptTagAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [
        ConceptTaggedItemInline
    ]

class DataTaggedItemInline(admin.StackedInline):
    model = DataTaggedItem

class DataTagAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [
        DataTaggedItemInline
    ]

class SkillTaggedItemInline(admin.StackedInline):
    model = SkillTaggedItem

class SkillTagAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [
        SkillTaggedItemInline
    ]

class ThemeTaggedItemInline(admin.StackedInline):
    model = ThemeTaggedItem

class ThemeTagAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [
        ThemeTaggedItemInline
    ]

class StatusTaggedItemInline(admin.StackedInline):
    model = StatusTaggedItem

class StatusTagAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [
        StatusTaggedItemInline
    ]


admin.site.register(TechnologyTag, TechnologyTagAdmin)
admin.site.register(ConceptTag, ConceptTagAdmin)
admin.site.register(DataTag, DataTagAdmin)
admin.site.register(SkillTag, SkillTagAdmin)
admin.site.register(ThemeTag, ThemeTagAdmin)
admin.site.register(StatusTag, StatusTagAdmin)
