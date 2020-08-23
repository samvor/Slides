# Generated by Django 3.1 on 2020-08-23 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0004_auto_20200823_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slides.course'),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slides.level'),
        ),
    ]
