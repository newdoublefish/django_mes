# Generated by Django 2.0 on 2018-01-08 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departure',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Employee', verbose_name='employee'),
        ),
        migrations.AlterField(
            model_name='employeesalaryitem',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Employee', verbose_name='employee'),
        ),
        migrations.AlterField(
            model_name='employeesalaryitem',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr.Entry', verbose_name='employee entry'),
        ),
        migrations.AlterField(
            model_name='employeesalaryitem',
            name='salary_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr.SalaryItem', verbose_name='salary item'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='guider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Employee', verbose_name='guider'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organ.Position', verbose_name='designate position'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.Employee', verbose_name='employee'),
        ),
    ]
