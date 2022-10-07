# Generated by Django 4.1.1 on 2022-10-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('making_time', models.CharField(max_length=100)),
                ('serves', models.CharField(max_length=100)),
                ('ingredients', models.CharField(max_length=300)),
                ('cost', models.IntegerField()),
                ('num_query', models.IntegerField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'recipe',
            },
        ),
    ]