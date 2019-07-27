# Generated by Django 2.0 on 2019-07-27 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lb1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('author_name', models.CharField(max_length=256)),
                ('publication', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='Addbook',
        ),
        migrations.DeleteModel(
            name='Addstudent',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
