# Generated by Django 5.1.2 on 2025-03-10 10:12

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='benefits',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Phúc lợi'),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Mô tả công việc'),
        ),
        migrations.AlterField(
            model_name='job',
            name='requirements',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Yêu cầu công việc'),
        ),
        migrations.AlterField(
            model_name='job',
            name='rights',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Quyền lợi'),
        ),
    ]
