# Generated by Django 4.2.4 on 2023-10-27 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AppRapida", "0004_axe_company_envoi_personne_alter_zonify_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bureaux",
            options={"managed": True},
        ),
        migrations.AlterModelOptions(
            name="tarif",
            options={"managed": True},
        ),
        migrations.AlterModelOptions(
            name="zonify",
            options={"managed": True},
        ),
        migrations.AlterModelTable(
            name="tarif",
            table="tarif",
        ),
    ]
