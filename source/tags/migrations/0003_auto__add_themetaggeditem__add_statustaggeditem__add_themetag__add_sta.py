# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ThemeTaggedItem'
        db.create_table('tags_themetaggeditem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tags_themetaggeditem_tagged_items', to=orm['contenttypes.ContentType'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tags_themetaggeditem_themetag_items', to=orm['tags.ThemeTag'])),
        ))
        db.send_create_signal('tags', ['ThemeTaggedItem'])

        # Adding model 'StatusTaggedItem'
        db.create_table('tags_statustaggeditem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tags_statustaggeditem_tagged_items', to=orm['contenttypes.ContentType'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tags_statustaggeditem_statustag_items', to=orm['tags.StatusTag'])),
        ))
        db.send_create_signal('tags', ['StatusTaggedItem'])

        # Adding model 'ThemeTag'
        db.create_table('tags_themetag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('tags', ['ThemeTag'])

        # Adding model 'StatusTag'
        db.create_table('tags_statustag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('tags', ['StatusTag'])


    def backwards(self, orm):
        # Deleting model 'ThemeTaggedItem'
        db.delete_table('tags_themetaggeditem')

        # Deleting model 'StatusTaggedItem'
        db.delete_table('tags_statustaggeditem')

        # Deleting model 'ThemeTag'
        db.delete_table('tags_themetag')

        # Deleting model 'StatusTag'
        db.delete_table('tags_statustag')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tags.concepttag': {
            'Meta': {'object_name': 'ConceptTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'tags.concepttaggeditem': {
            'Meta': {'object_name': 'ConceptTaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags_concepttaggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags_concepttaggeditem_concepttag_items'", 'to': "orm['tags.ConceptTag']"})
        },
        'tags.datatag': {
            'Meta': {'object_name': 'DataTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'tags.datataggeditem': {
            'Meta': {'object_name': 'DataTaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags_datataggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags_datataggeditem_datatag_items'", 'to': "orm['tags.DataTag']"})
        },
        'tags.skilltag': {
            'Meta': {'object_name': 'SkillTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'tags.skilltaggeditem': {
            'Meta': {'object_name': 'SkillTaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags_skilltaggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags_skilltaggeditem_skilltag_items'", 'to': "orm['tags.SkillTag']"})
        },
        'tags.statustag': {
            'Meta': {'object_name': 'StatusTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'tags.statustaggeditem': {
            'Meta': {'object_name': 'StatusTaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags_statustaggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags_statustaggeditem_statustag_items'", 'to': "orm['tags.StatusTag']"})
        },
        'tags.technologytag': {
            'Meta': {'object_name': 'TechnologyTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'tags.technologytaggeditem': {
            'Meta': {'object_name': 'TechnologyTaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags_technologytaggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags_technologytaggeditem_techtag_items'", 'to': "orm['tags.TechnologyTag']"})
        },
        'tags.themetag': {
            'Meta': {'object_name': 'ThemeTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'tags.themetaggeditem': {
            'Meta': {'object_name': 'ThemeTaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags_themetaggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags_themetaggeditem_themetag_items'", 'to': "orm['tags.ThemeTag']"})
        }
    }

    complete_apps = ['tags']