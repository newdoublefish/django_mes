# Generated by Django 2.0.1 on 2018-01-31 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invent', '0002_auto_20180108_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialinventory',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='initialinventory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='inititem',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invent.InitialInventory'),
        ),
        migrations.AlterField(
            model_name='inoutdetail',
            name='material',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_virtual': '0'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Material', verbose_name='material'),
        ),
        migrations.AlterField(
            model_name='inoutdetail',
            name='measure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Measure', verbose_name='measure'),
        ),
        migrations.AlterField(
            model_name='inoutdetail',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Warehouse', verbose_name='warehouse'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.Material', verbose_name='material'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='measure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.Measure', verbose_name='measure'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.Warehouse', verbose_name='warehouse'),
        ),
        migrations.AlterField(
            model_name='stockin',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='stockin',
            name='po',
            field=models.ForeignKey(blank=True, limit_choices_to={'entry_status': '0'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase.PurchaseOrder', verbose_name='purchase order'),
        ),
        migrations.AlterField(
            model_name='stockin',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='stockin',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.Warehouse', verbose_name='warehouse'),
        ),
        migrations.AlterField(
            model_name='stockout',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='stockout',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Project', verbose_name='project'),
        ),
        migrations.AlterField(
            model_name='stockout',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='out user'),
        ),
        migrations.AlterField(
            model_name='stockout',
            name='wo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='selfhelp.WorkOrder', verbose_name='work order'),
        ),
        migrations.AlterField(
            model_name='wareadjust',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='wareadjust',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='out user'),
        ),
        migrations.AlterField(
            model_name='warereturn',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='warereturn',
            name='out',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invent.StockOut', verbose_name='StockOut'),
        ),
        migrations.AlterField(
            model_name='warereturn',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='out user'),
        ),
    ]