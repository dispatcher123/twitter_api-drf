# Generated by Django 3.2.7 on 2021-09-09 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0002_alter_comment_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='profiles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_comment', to='twit.profile'),
        ),
    ]
