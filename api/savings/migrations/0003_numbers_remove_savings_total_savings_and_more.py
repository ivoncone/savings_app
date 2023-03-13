# Generated by Django 4.1.7 on 2023-03-12 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0002_days_alter_savings_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeros', models.IntegerField(null=True, unique=True)),
            ],
            options={
                'db_table': 'numbers',
            },
        ),
        migrations.RemoveField(
            model_name='savings',
            name='total_savings',
        ),
        migrations.RemoveField(
            model_name='savings',
            name='numbers',
        ),
        migrations.AddField(
            model_name='savings',
            name='numbers',
            field=models.ManyToManyField(to='savings.numbers'),
        ),
    ]