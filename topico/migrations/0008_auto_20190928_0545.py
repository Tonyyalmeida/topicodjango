# Generated by Django 2.1.4 on 2019-09-28 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topico', '0007_auto_20190926_0142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wordlist',
            options={},
        ),
        migrations.RemoveField(
            model_name='wordlist',
            name='finished',
        ),
        migrations.RemoveField(
            model_name='wordlist',
            name='name',
        ),
        migrations.AddField(
            model_name='wordlist',
            name='isTodo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='wordlist',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='topico.Question'),
        ),
    ]
