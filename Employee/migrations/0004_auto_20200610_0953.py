# Generated by Django 2.2.5 on 2020-06-10 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_auto_20200531_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='gender',
            field=models.TextField(choices=[(0, '男性'), (1, '女性')], default=0),
        ),
    ]
