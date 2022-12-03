# Generated by Django 3.1.14 on 2022-11-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('images', models.ImageField(upload_to='upload/category/')),
            ],
        ),
    ]