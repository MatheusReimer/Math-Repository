# Generated by Django 2.2.4 on 2019-10-08 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190929_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(default='padrao.jpg', upload_to=''),
        ),
    ]