# Generated by Django 3.1.3 on 2020-12-20 15:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20201124_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
    ]
