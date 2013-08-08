# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SeizedMaterialType'
        db.create_table('seized_material_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'materials_seizedmaterialtype_created_histories', null=True, to=orm['accounts.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'materials_seizedmaterialtype_updated_histories', null=True, to=orm['accounts.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'materials', ['SeizedMaterialType'])

        # Adding model 'SeizedMaterial'
        db.create_table('seized_material', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'materials_seizedmaterial_created_histories', null=True, to=orm['accounts.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'materials_seizedmaterial_updated_histories', null=True, to=orm['accounts.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='seized_materials', null=True, on_delete=models.PROTECT, to=orm['materials.SeizedMaterialType'])),
        ))
        db.send_create_signal(u'materials', ['SeizedMaterial'])

        # Adding model 'OccurrenceSeizedMaterial'
        db.create_table('occurrence_seized_material', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'materials_occurrenceseizedmaterial_created_histories', null=True, to=orm['accounts.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'materials_occurrenceseizedmaterial_updated_histories', null=True, to=orm['accounts.User'])),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('occurrence', self.gf('django.db.models.fields.related.ForeignKey')(related_name='occurrence_seized_material', to=orm['core.Occurrence'])),
            ('seized_material', self.gf('django.db.models.fields.related.ForeignKey')(related_name='occurrence_seized_material', to=orm['materials.SeizedMaterial'])),
        ))
        db.send_create_signal(u'materials', ['OccurrenceSeizedMaterial'])


    def backwards(self, orm):
        # Deleting model 'SeizedMaterialType'
        db.delete_table('seized_material_type')

        # Deleting model 'SeizedMaterial'
        db.delete_table('seized_material')

        # Deleting model 'OccurrenceSeizedMaterial'
        db.delete_table('occurrence_seized_material')


    models = {
        u'accounts.user': {
            'Meta': {'object_name': 'User', 'db_table': "'user'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'accounts_user_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_manager': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'accounts_user_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.address': {
            'Meta': {'object_name': 'Address', 'db_table': "'address'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'complement': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_address_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_address_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'})
        },
        u'core.attendedpublic': {
            'Meta': {'object_name': 'AttendedPublic', 'db_table': "'attended_public'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_attendedpublic_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_attendedpublic_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
        },
        u'core.occurrence': {
            'Meta': {'object_name': 'Occurrence', 'db_table': "'occurrence'"},
            'accident_report': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'attended_public': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'occurrences'", 'on_delete': 'models.PROTECT', 'to': u"orm['core.AttendedPublic']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrence_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nature': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'police_car': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'occurrences'", 'on_delete': 'models.PROTECT', 'to': u"orm['core.PoliceCar']"}),
            'relevant_information': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'occurrences'", 'on_delete': 'models.PROTECT', 'to': u"orm['core.School']"}),
            'seized_materials': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'occurrences'", 'to': u"orm['materials.SeizedMaterial']", 'through': u"orm['materials.OccurrenceSeizedMaterial']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'occurrences'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['core.OccurrenceStatus']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'occurrences'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['core.OccurrenceType']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrence_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
        },
        u'core.occurrencestatus': {
            'Meta': {'object_name': 'OccurrenceStatus', 'db_table': "'occurrence_status'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrencestatus_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrencestatus_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
        },
        u'core.occurrencetype': {
            'Meta': {'object_name': 'OccurrenceType', 'db_table': "'occurrence_type'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrencetype_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrencetype_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
        },
        u'core.policecar': {
            'Meta': {'object_name': 'PoliceCar', 'db_table': "'police_car'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_policecar_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_policecar_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
        },
        u'core.school': {
            'Meta': {'object_name': 'School', 'db_table': "'school'"},
            'address': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Address']", 'unique': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_school_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_school_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
        },
        u'materials.occurrenceseizedmaterial': {
            'Meta': {'object_name': 'OccurrenceSeizedMaterial', 'db_table': "'occurrence_seized_material'"},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'materials_occurrenceseizedmaterial_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occurrence': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'occurrence_seized_material'", 'to': u"orm['core.Occurrence']"}),
            'seized_material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'occurrence_seized_material'", 'to': u"orm['materials.SeizedMaterial']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'materials_occurrenceseizedmaterial_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
        },
        u'materials.seizedmaterial': {
            'Meta': {'object_name': 'SeizedMaterial', 'db_table': "'seized_material'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'materials_seizedmaterial_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'seized_materials'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['materials.SeizedMaterialType']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'materials_seizedmaterial_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
        },
        u'materials.seizedmaterialtype': {
            'Meta': {'object_name': 'SeizedMaterialType', 'db_table': "'seized_material_type'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'materials_seizedmaterialtype_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'materials_seizedmaterialtype_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
        }
    }

    complete_apps = ['materials']