# Generated by Django 4.2.4 on 2023-11-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appRapidaCorps", "0008_remove_doc_envoi_doc_envoi"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facture",
            name="type_paiement",
            field=models.IntegerField(
                choices=[(0, "0 depot"), (1, "1 collect")],
                db_column="type_paiement",
                default=0,
            ),
        ),
    ]