from django.contrib import admin

from .models import TechnologyTag, TechnologyTaggedItem, ConceptTag, ConceptTaggedItem, DataTag, DataTaggedItem, SkillTag, SkillTaggedItem


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


admin.site.register(TechnologyTag, TechnologyTagAdmin)
admin.site.register(ConceptTag, ConceptTagAdmin)
admin.site.register(DataTag, DataTagAdmin)
admin.site.register(SkillTag, SkillTagAdmin)
