# Generated by Django 2.2.4 on 2019-10-08 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20191008_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, default='padrao.jpg', upload_to=''),
        ),
    ]
