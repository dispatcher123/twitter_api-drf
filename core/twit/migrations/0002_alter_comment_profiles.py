# Generated by Django 3.2.7 on 2021-09-09 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='profiles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twit.profile'),
        ),
    ]
