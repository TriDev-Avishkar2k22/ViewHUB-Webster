# Generated by Django 4.0.3 on 2022-10-28 15:24

from django.db import migrations, models
import home.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_upload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='Timestamp',
            field=models.DateTimeField(blank=True, default='now'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(upload_to='', validators=[home.validators.fileSize]),
        ),
    ]
