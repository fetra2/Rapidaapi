# Generated by Django 4.2.4 on 2023-10-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appRapidaCorps", "0005_alter_facture_type_paiement"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facture",
            name="type_paiement",
            field=models.IntegerField(
                choices=[(0, "0 depot"), (1, "1 collect")],
                db_column="type_paiement",
                default=0,
                max_length=50,
            ),
        ),
    ]