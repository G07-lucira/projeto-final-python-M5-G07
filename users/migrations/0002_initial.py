# Generated by Django 4.1.2 on 2022-11-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users_animes", "0001_initial"),
        ("users", "0001_initial"),
        ("animes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="animes",
            field=models.ManyToManyField(
                related_name="users",
                through="users_animes.UserAnimes",
                to="animes.anime",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
