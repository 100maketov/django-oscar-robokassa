# -*- coding: utf-8 -*-
from south.v2 import DataMigration

class Migration(DataMigration):

    depends_on = (
        ('payment', '0003_auto__chg_field_sourcetype_code__add_unique_sourcetype_code'),
    )

    def forwards(self, orm):
        orm['payment.SourceType'].objects.get_or_create(code='robokassa', defaults=dict(name=u'Робокасса'))

    def backwards(self, orm):
        pass

    models = {
        u'robokassa.successnotification': {
            'InvId': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'Meta': {'object_name': 'SuccessNotification'},
            'OutSum': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'payment.sourcetype': {
            'Meta': {'object_name': 'SourceType'},
            'code': ('oscar.models.fields.autoslugfield.AutoSlugField', [],
                     {'allow_duplicates': 'False', 'max_length': '128', 'separator': "u'-'", 'blank': 'True',
                      'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['robokassa']
    symmetrical = True
