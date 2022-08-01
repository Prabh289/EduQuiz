# Generated by Django 3.1.7 on 2021-05-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='explanation',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quizmodel',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
