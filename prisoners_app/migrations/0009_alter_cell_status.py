# Generated by Django 4.0.4 on 2022-05-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prisoners_app', '0008_cell_max_inmates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cell',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Empty'), ('2', 'Visible'), ('3', 'Full')], default='Empty', max_length=10),
        ),
    ]
