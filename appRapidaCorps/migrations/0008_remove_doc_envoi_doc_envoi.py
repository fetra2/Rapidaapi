# Generated by Django 4.2.4 on 2023-11-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appRapidaCorps", "0007_alter_facture_bureau_alter_facture_expediteur"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doc",
            name="envoi",
        ),
        migrations.AddField(
            model_name="doc",
            name="envoi",
            field=models.ManyToManyField(
                related_name="envoi_doc", to="appRapidaCorps.envoi"
            ),
        ),
    ]
