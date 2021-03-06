# Generated by Django 2.0.1 on 2018-01-31 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20180108_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departure',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.Employee', verbose_name='employee'),
        ),
        migrations.AlterField(
            model_name='employeesalaryitem',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Employee', verbose_name='employee'),
        ),
        migrations.AlterField(
            model_name='employeesalaryitem',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Entry', verbose_name='employee entry'),
        ),
        migrations.AlterField(
            model_name='employeesalaryitem',
            name='salary_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.SalaryItem', verbose_name='salary item'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='guider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.Employee', verbose_name='guider'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organ.Position', verbose_name='designate position'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.Employee', verbose_name='employee'),
        ),
    ]
