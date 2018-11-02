# Generated by Django 2.1 on 2018-11-02 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_processorvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomVideoGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Enter a brief description of the custom group', max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('videos', models.ManyToManyField(help_text='Select videos to be added to this custom group', to='catalog.ProcessorVideo')),
            ],
        ),
    ]
