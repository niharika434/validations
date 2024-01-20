# Generated by Django 4.2.6 on 2023-12-16 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sal', models.IntegerField()),
                ('hire_date', models.DateField()),
                ('dept_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]