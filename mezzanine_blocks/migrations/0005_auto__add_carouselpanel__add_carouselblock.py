# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CarouselPanel'
        db.create_table('mezzanine_blocks_carouselpanel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('carousel_block', self.gf('django.db.models.fields.related.ForeignKey')(related_name='panels', to=orm['mezzanine_blocks.CarouselBlock'])),
            ('image', self.gf('filebrowser_safe.fields.FileBrowseField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
        ))
        db.send_create_signal('mezzanine_blocks', ['CarouselPanel'])

        # Adding model 'CarouselBlock'
        db.create_table('mezzanine_blocks_carouselblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mezzanine_blocks.BlockCategory'], null=True, blank=True)),
            ('login_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('show_title', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')(blank=True)),
            ('interval', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('panel_indicators', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=200)),
            ('quality', self.gf('django.db.models.fields.IntegerField')(default=80)),
        ))
        db.send_create_signal('mezzanine_blocks', ['CarouselBlock'])


    def backwards(self, orm):
        # Deleting model 'CarouselPanel'
        db.delete_table('mezzanine_blocks_carouselpanel')

        # Deleting model 'CarouselBlock'
        db.delete_table('mezzanine_blocks_carouselblock')


    models = {
        'mezzanine_blocks.block': {
            'Meta': {'object_name': 'Block'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mezzanine_blocks.BlockCategory']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'mezzanine_blocks.blockcategory': {
            'Meta': {'object_name': 'BlockCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': "orm['mezzanine_blocks.BlockCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'mezzanine_blocks.carouselblock': {
            'Meta': {'object_name': 'CarouselBlock'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mezzanine_blocks.BlockCategory']", 'null': 'True', 'blank': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'panel_indicators': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'quality': ('django.db.models.fields.IntegerField', [], {'default': '80'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '200'})
        },
        'mezzanine_blocks.carouselpanel': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'CarouselPanel'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'carousel_block': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'panels'", 'to': "orm['mezzanine_blocks.CarouselBlock']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser_safe.fields.FileBrowseField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'mezzanine_blocks.imageblock': {
            'Meta': {'object_name': 'ImageBlock'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mezzanine_blocks.BlockCategory']", 'null': 'True', 'blank': 'True'}),
            'description': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quality': ('django.db.models.fields.IntegerField', [], {'default': '80'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '200'})
        },
        'mezzanine_blocks.richblock': {
            'Meta': {'object_name': 'RichBlock'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mezzanine_blocks.BlockCategory']", 'null': 'True', 'blank': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['mezzanine_blocks']