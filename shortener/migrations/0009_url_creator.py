# Generated by Django 3.1.6 on 2021-02-13 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shortener', '0008_remove_url_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='creator',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
            preserve_default=False,
        ),
    ]