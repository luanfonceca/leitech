# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table('user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name('user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name('user_user_permissions'))


        # Changing field 'SeizedMaterialType.updated_by'
        db.alter_column('seized_material_type', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'SeizedMaterialType.created_by'
        db.alter_column('seized_material_type', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'PoliceCar.updated_by'
        db.alter_column('police_car', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'PoliceCar.created_by'
        db.alter_column('police_car', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'OccurrenceStatus.updated_by'
        db.alter_column('occurrence_status', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'OccurrenceStatus.created_by'
        db.alter_column('occurrence_status', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'AttendedPublic.updated_by'
        db.alter_column('attended_public', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'AttendedPublic.created_by'
        db.alter_column('attended_public', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'OccurrenceType.updated_by'
        db.alter_column('occurrence_type', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'OccurrenceType.created_by'
        db.alter_column('occurrence_type', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'SeizedMaterial.created_by'
        db.alter_column('seized_material', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'SeizedMaterial.updated_by'
        db.alter_column('seized_material', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'Police.created_by'
        db.alter_column('police', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'Police.updated_by'
        db.alter_column('police', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'Occurrence.updated_by'
        db.alter_column('occurrence', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'Occurrence.created_by'
        db.alter_column('occurrence', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'School.created_by'
        db.alter_column('school', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'School.updated_by'
        db.alter_column('school', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'Address.updated_by'
        db.alter_column('address', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'Address.created_by'
        db.alter_column('address', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'OccurrenceSeizedMaterial.updated_by'
        db.alter_column('occurrence_seized_material', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

        # Changing field 'OccurrenceSeizedMaterial.created_by'
        db.alter_column('occurrence_seized_material', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['accounts.User']))

    def backwards(self, orm):
        # Adding model 'User'
        db.create_table('user', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'core_user_updated_histories', null=True, to=orm['core.User'], blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'core_user_created_histories', null=True, to=orm['core.User'], blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_manager', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255, unique=True, db_index=True)),
        ))
        db.send_create_signal(u'core', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name('user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'core.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name('user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'core.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])


        # Changing field 'SeizedMaterialType.updated_by'
        db.alter_column('seized_material_type', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'SeizedMaterialType.created_by'
        db.alter_column('seized_material_type', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'PoliceCar.updated_by'
        db.alter_column('police_car', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'PoliceCar.created_by'
        db.alter_column('police_car', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'OccurrenceStatus.updated_by'
        db.alter_column('occurrence_status', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'OccurrenceStatus.created_by'
        db.alter_column('occurrence_status', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'AttendedPublic.updated_by'
        db.alter_column('attended_public', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'AttendedPublic.created_by'
        db.alter_column('attended_public', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'OccurrenceType.updated_by'
        db.alter_column('occurrence_type', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'OccurrenceType.created_by'
        db.alter_column('occurrence_type', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'SeizedMaterial.created_by'
        db.alter_column('seized_material', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'SeizedMaterial.updated_by'
        db.alter_column('seized_material', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'Police.created_by'
        db.alter_column('police', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'Police.updated_by'
        db.alter_column('police', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'Occurrence.updated_by'
        db.alter_column('occurrence', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'Occurrence.created_by'
        db.alter_column('occurrence', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'School.created_by'
        db.alter_column('school', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'School.updated_by'
        db.alter_column('school', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'Address.updated_by'
        db.alter_column('address', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'Address.created_by'
        db.alter_column('address', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'OccurrenceSeizedMaterial.updated_by'
        db.alter_column('occurrence_seized_material', 'updated_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

        # Changing field 'OccurrenceSeizedMaterial.created_by'
        db.alter_column('occurrence_seized_material', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))

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
            'seized_materials': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'occurrences'", 'to': u"orm['core.SeizedMaterial']", 'through': u"orm['core.OccurrenceSeizedMaterial']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'occurrences'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['core.OccurrenceStatus']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'occurrences'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['core.OccurrenceType']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrence_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
        },
        u'core.occurrenceseizedmaterial': {
            'Meta': {'object_name': 'OccurrenceSeizedMaterial', 'db_table': "'occurrence_seized_material'"},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrenceseizedmaterial_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occurrence': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'occurrence_seized_material'", 'to': u"orm['core.Occurrence']"}),
            'seized_material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'occurrence_seized_material'", 'to': u"orm['core.SeizedMaterial']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_occurrenceseizedmaterial_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
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
        u'core.police': {
            'Meta': {'object_name': 'Police', 'db_table': "'police'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_police_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'police_car': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'polices'", 'null': 'True', 'to': u"orm['core.PoliceCar']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_police_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
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
        u'core.seizedmaterial': {
            'Meta': {'object_name': 'SeizedMaterial', 'db_table': "'seized_material'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_seizedmaterial_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'seized_materials'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['core.SeizedMaterialType']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_seizedmaterial_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
        },
        u'core.seizedmaterialtype': {
            'Meta': {'object_name': 'SeizedMaterialType', 'db_table': "'seized_material_type'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_seizedmaterialtype_created_histories'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'core_seizedmaterialtype_updated_histories'", 'null': 'True', 'to': u"orm['accounts.User']"})
        }
    }

    complete_apps = ['core']