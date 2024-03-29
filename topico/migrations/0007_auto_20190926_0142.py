# Generated by Django 2.1.4 on 2019-09-26 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topico', '0006_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New List', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('finished', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['updated'],
            },
        ),
        migrations.CreateModel(
            name='WordPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('wordEnglish', models.CharField(blank=True, default='', max_length=100)),
                ('wordVietnamese', models.CharField(blank=True, default='', max_length=100)),
                ('exampleEnglish', models.CharField(blank=True, default='', max_length=250)),
                ('exampleVietnamese', models.CharField(blank=True, default='', max_length=250)),
                ('wordList', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='WordPairs', to='topico.WordList')),
            ],
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topico.Question'),
        ),
    ]
