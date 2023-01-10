# Generated by Django 4.1.4 on 2022-12-19 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0002_alter_category_options"),
        ("experiences", "0002_experience_category_alter_perk_details_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="perk",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.category",
            ),
        ),
    ]
