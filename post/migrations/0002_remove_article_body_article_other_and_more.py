# Generated by Django 4.2.5 on 2023-10-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='body',
        ),
        migrations.AddField(
            model_name='article',
            name='other',
            field=models.ImageField(default='', upload_to='post'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
