# Generated by Django 2.0.1 on 2018-01-31 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organ', '0002_auto_20180108_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgunit',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='orgunit',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organ.OrgUnit', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='position',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='position',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organ.Position', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='position',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organ.OrgUnit', verbose_name='org unit'),
        ),
    ]
