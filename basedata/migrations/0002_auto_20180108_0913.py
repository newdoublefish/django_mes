# Generated by Django 2.0 on 2018-01-08 09:13

import basedata.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basedata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Partner', verbose_name='partner'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='trade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Trade', verbose_name='trade'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Category', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='category',
            name='trade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Trade', verbose_name='trade'),
        ),
        migrations.AlterField(
            model_name='dataimport',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'app_label__in': ['basedata', 'organ', 'auth']}, on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType', verbose_name='content type'),
        ),
        migrations.AlterField(
            model_name='document',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='education',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Employee', verbose_name='employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organ.Position', verbose_name='position'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='expenseaccount',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='expenseaccount',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.ExpenseAccount', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='extraparam',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Material', verbose_name='material'),
        ),
        migrations.AlterField(
            model_name='family',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Employee', verbose_name='employee'),
        ),
        migrations.AlterField(
            model_name='material',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Brand', verbose_name='brand'),
        ),
        migrations.AlterField(
            model_name='material',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='material',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='material',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Warehouse', verbose_name='warehouse'),
        ),
        migrations.AlterField(
            model_name='materialparam',
            name='param_name',
            field=models.ForeignKey(blank=basedata.models.Trade, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.TechnicalParameterName'),
        ),
        migrations.AlterField(
            model_name='materialparam',
            name='param_value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.TechnicalParameterValue'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='project',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='project',
            name='partner',
            field=models.ForeignKey(blank=True, limit_choices_to={'partner_type': 'C'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Partner', verbose_name='partner'),
        ),
        migrations.AlterField(
            model_name='technicalparametername',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Category', verbose_name='material category'),
        ),
        migrations.AlterField(
            model_name='technicalparametervalue',
            name='tech_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.TechnicalParameterName', verbose_name='technical name'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Trade', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='valuelist',
            name='locked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='locked by'),
        ),
        migrations.AlterField(
            model_name='valuelist',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='syscfg.Module', verbose_name='module'),
        ),
        migrations.AlterField(
            model_name='valuelistitem',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.ValueList', verbose_name='list group'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Employee', verbose_name='employee'),
        ),
    ]
