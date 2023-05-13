# Generated by Django 4.2 on 2023-04-30 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=100)),
                ('Title', models.CharField(max_length=100)),
                ('copy_count', models.IntegerField()),
                ('year_of_pub', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('brand', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('price', models.FloatField(default=0)),
                ('pic', models.FileField(default=0, upload_to='myapp/static/pic')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
    ]
