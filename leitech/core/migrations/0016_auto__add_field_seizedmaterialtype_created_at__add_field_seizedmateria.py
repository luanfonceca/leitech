# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SeizedMaterialType.created_at'
        db.add_column('seized_material_type', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 7, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SeizedMaterialType.updated_at'
        db.add_column('seized_material_type', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 7, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SeizedMaterialType.created_by'
        db.add_column('seized_material_type', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'core_seizedmaterialtype_created_histories', null=True, to=orm['core.User']),
                      keep_default=False)

        # Adding field 'SeizedMaterialType.updated_by'
        db.add_column('seized_material_type', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'core_seizedmaterialtype_updated_histories', null=True, to=orm['core.User']),
                      keep_default=False)

        # Adding field 'PoliceCar.created_at'
        db.add_column('police_car', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 7, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'PoliceCar.updated_at'
        db.add_column('police_car', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 7, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'PoliceCar.created_by'
        db.add_column('police_car', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'core_policecar_created_histories', null=True, to=orm['core.User']),
                      keep_default=False)

        # Adding field 'PoliceCar.updated_by'
        db.add_column('police_car', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'core_policecar_updated_histories', null=True, to=orm['core.User']),
                      keep_default=False)

        # Adding field 'OccurrenceStatus.created_at'
        db.add_column('occurrence_status', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 7, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'OccurrenceStatus.updated_at'
        db.add_column('occurrence_status', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 7, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'OccurrenceStatus.created_by'
        db.add_column('occurrence_status', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'core_occurrencestatus_created_histories', null=True, to=orm['core.User']),
                      keep_default=False)

        # Adding field 'OccurrenceStatus.updated_by'
        db.add_column('occurrence_status', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'core_occurrencestatus_updated_histories', null=True, to=orm['core.User']),
                      keep_default=False)

        # Adding field 'OccurrenceType.created_at'
        db.add_column('occurrence_type', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 7, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'OccurrenceType.updated_at'
        db.add_column('occurrence_type', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 7, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'OccurrenceType.created_by'
        db.add_column('occurrence_type', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'core_occurrencetype_created_histories', null=True, to=orm['core.User']),
                      keep_default=False)

        # Adding field 'OccurrenceType.updated_by'
        db.add_column('occurrence_type', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'core_occurrencetype_updated_histories', null=True, to=orm['core.User']),
                      keep_default=False)

        # Adding field 'SeizedMaterial.created_at'
        db.add_column('seized_material', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 7, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SeizedMaterial.updated_at'
        db.add_column('seized_material', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 7, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SeizedMaterial.created_by'
        db.add_column('seized_material', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'core_seizedmaterial_created_histories', null=True, to=orm['core.User']),
                      keep_default=False)

        # Adding field 'SeizedMaterial.updated_by'
        db.add_column('seized_material', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'core_seizedmaterial_updated_histories', null=True, to=orm['core.User']),
                      keep_default=False)

        # Adding field 'Police.created_at'
        db.add_column('police', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 7, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Police.updated_at'
        db.add_column('police', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 7, 18, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Police.created_by'
        db.add_column('police', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'core_police_created_histories', null=True, to=orm['core.User']),
                      keep_default=False)

        # Adding field 'Police.updated_by'
        db.add_column('police', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'core_police_updated_histories', null=True, to=orm['core.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SeizedMaterialType.created_at'
        db.delete_column('seized_material_type', 'created_at')

        # Deleting field 'SeizedMaterialType.updated_at'
        db.delete_column('seized_material_type', 'updated_at')

        # Deleting field 'SeizedMaterialType.created_by'
        db.delete_column('seized_material_type', 'created_by_id')

        # Deleting field 'SeizedMaterialType.updated_by'
        db.delete_column('seized_material_type', 'updated_by_id')

        # Deleting field 'PoliceCar.created_at'
        db.delete_column('police_car', 'created_at')

        # Deleting field 'PoliceCar.updated_at'
        db.delete_column('police_car', 'updated_at')

        # Deleting field 'PoliceCar.created_by'
        db.delete_column('police_car', 'created_by_id')

        # Deleting field 'PoliceCar.updated_by'
        db.delete_column('police_car', 'updated_by_id')

        # Deleting field 'OccurrenceStatus.created_at'
        db.delete_column('occurrence_status', 'created_at')

        # Deleting field 'OccurrenceStatus.updated_at'
        db.delete_column('occurrence_status', 'updated_at')

        # Deleting field 'OccurrenceStatus.created_by'
        db.delete_column('occurrence_status', 'created_by_id')

        # Deleting field 'OccurrenceStatus.updated_by'
        db.delete_column('occurrence_status', 'updated_by_id')

        # Deleting field 'OccurrenceType.created_at'
        db.delete_column('occurrence_type', 'created_at')

        # Deleting field 'OccurrenceType.updated_at'
        db.delete_column('occurrence_type', 'updated_at')

        # Deleting field 'OccurrenceType.created_by'
        db.delete_column('occurrence_type', 'created_by_id')

        # Deleting field 'OccurrenceType.updated_by'
        db.delete_column('occurrence_type', 'updated_by_id')

        # Deleting field 'SeizedMaterial.created_at'
        db.delete_column('seized_material', 'created_at')

        # Deleting field 'SeizedMaterial.updated_at'
        db.delete_column('seized_material', 'updated_at')

        # Deleting field 'SeizedMaterial.created_by'
        db.delete_column('seized_material', 'created_by_id')

        # Deleting field 'SeizedMaterial.updated_by'
        db.delete_column('seized_material', 'updated_by_id')

        # Deleting field 'Police.created_at'
        db.delete_column('police', 'created_at')

        # Deleting field 'Police.updated_at'
        db.delete_column('police', 'updated_at')

        # Deleting field 'Police.created_by'
        db.delete_column('police', 'created_by_id')

        # Deleting field 'Police.updated_by'
        db.delete_column('police', 'updated_by_id')


    models = {
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_address_created_histories'", 'null': 'True', 'to': u"orm['core.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_address_updated_histories'", 'null': 'True', 'to': u"orm['core.User']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'})
        },
        u'core.occurrence': {
            'Meta': {'object_name': 'Occurrence', 'db_table': "'occurrence'"},
            'accident_report': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'attended_public': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrence_created_histories'", 'null': 'True', 'to': u"orm['core.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nature': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'police_car': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'occurrences'", 'on_delete': 'models.PROTECT', 'to': u"orm['core.PoliceCar']"}),
            'relevant_information': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'occurrences'", 'on_delete': 'models.PROTECT', 'to': u"orm['core.School']"}),
            'seized_materials': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'occurrences'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['core.SeizedMaterial']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'occurrences'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['core.OccurrenceStatus']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'occurrences'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['core.OccurrenceType']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrence_updated_histories'", 'null': 'True', 'to': u"orm['core.User']"})
        },
        u'core.occurrencestatus': {
            'Meta': {'object_name': 'OccurrenceStatus', 'db_table': "'occurrence_status'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrencestatus_created_histories'", 'null': 'True', 'to': u"orm['core.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrencestatus_updated_histories'", 'null': 'True', 'to': u"orm['core.User']"})
        },
        u'core.occurrencetype': {
            'Meta': {'object_name': 'OccurrenceType', 'db_table': "'occurrence_type'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrencetype_created_histories'", 'null': 'True', 'to': u"orm['core.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrencetype_updated_histories'", 'null': 'True', 'to': u"orm['core.User']"})
        },
        u'core.police': {
            'Meta': {'object_name': 'Police', 'db_table': "'police'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_police_created_histories'", 'null': 'True', 'to': u"orm['core.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'police_car': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'polices'", 'null': 'True', 'to': u"orm['core.PoliceCar']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_police_updated_histories'", 'null': 'True', 'to': u"orm['core.User']"})
        },
        u'core.policecar': {
            'Meta': {'object_name': 'PoliceCar', 'db_table': "'police_car'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_policecar_created_histories'", 'null': 'True', 'to': u"orm['core.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_policecar_updated_histories'", 'null': 'True', 'to': u"orm['core.User']"})
        },
        u'core.school': {
            'Meta': {'object_name': 'School', 'db_table': "'school'"},
            'address': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Address']", 'unique': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_school_created_histories'", 'null': 'True', 'to': u"orm['core.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_school_updated_histories'", 'null': 'True', 'to': u"orm['core.User']"})
        },
        u'core.seizedmaterial': {
            'Meta': {'object_name': 'SeizedMaterial', 'db_table': "'seized_material'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_seizedmaterial_created_histories'", 'null': 'True', 'to': u"orm['core.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'seized_materials'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['core.SeizedMaterialType']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_seizedmaterial_updated_histories'", 'null': 'True', 'to': u"orm['core.User']"})
        },
        u'core.seizedmaterialtype': {
            'Meta': {'object_name': 'SeizedMaterialType', 'db_table': "'seized_material_type'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_seizedmaterialtype_created_histories'", 'null': 'True', 'to': u"orm['core.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_seizedmaterialtype_updated_histories'", 'null': 'True', 'to': u"orm['core.User']"})
        },
        u'core.user': {
            'Meta': {'object_name': 'User', 'db_table': "'user'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['core']