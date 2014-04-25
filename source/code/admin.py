from django.contrib import admin

from .models import Code, CodeLink
from source.base.widgets import AdminImageMixin

class CodeLinkInline(admin.StackedInline):
    model = CodeLink
    extra = 1
    fieldsets = (
        ('', {'fields': (('name', 'url'),)}),
    )
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        # More usable width in admin form field for names
        field = super(CodeLinkInline, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'name':
            field.widget.attrs['style'] = 'width: 30em;'
        return field

class CodeAdmin(AdminImageMixin, admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('people', 'organizations',)
    list_filter = ('is_live', 'is_active',)
    search_fields = ('name', 'description',)
    fieldsets = (
        ('', {'fields': (('name', 'slug'), ('is_live', 'is_active', 'seeking_contributors'), 'url', 'source_code', 'documentation', 'tags', 'technology_tags', 'concept_tags', 'data_tags', 'skill_tags', 'screenshot', 'description', 'pros', 'cons', ('repo_last_push', 'repo_forks', 'repo_watchers'), 'repo_master_branch', 'repo_description', 'summary',)}),
        ('Related objects', {'fields': ('people', 'organizations',)}),
    )
    inlines = [CodeLinkInline,]
    readonly_fields = ('tags',)
    
    def save_model(self, request, obj, form, change):
        '''
        Mirror split tagfield contents in primary `tags` model.
        See source.tags.models for further details.
        '''
        technology_tags_list = form.cleaned_data['technology_tags']
        concept_tags_list = form.cleaned_data['concept_tags']
        data_tags_list = form.cleaned_data['data_tags']
        skill_tags_list = form.cleaned_data['skill_tags']
        merged_tags = technology_tags_list + concept_tags_list + data_tags_list + skill_tags_list
        if merged_tags:
            form.cleaned_data['tags'] = merged_tags

        super(CodeAdmin, self).save_model(request, obj, form, change)
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        # More usable heights and widths in admin form fields
        field = super(CodeAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['url','source_code','documentation','tags','technology_tags','concept_tags','data_tags','skill_tags']:
            field.widget.attrs['style'] = 'width: 45em;'
        if db_field.name in ['name','slug']:
            field.widget.attrs['style'] = 'width: 30em;'
        if db_field.name in ['summary','pros','cons']:
            field.widget.attrs['style'] = 'height: 4.5em;'
        return field

admin.site.register(Code, CodeAdmin)
