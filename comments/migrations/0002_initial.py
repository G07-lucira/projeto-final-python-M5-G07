<<<<<<< HEAD
# Generated by Django 4.1.2 on 2022-11-03 13:49
=======
# Generated by Django 4.1.2 on 2022-11-03 15:40
>>>>>>> 129318116d8dcc6bd3ce956ed2a067e9457713ab

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
