# Generated by Django 3.1.7 on 2021-05-17 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BidCrawling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchsubject', models.CharField(blank=True, db_column='searchSubject', max_length=500, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('writer', models.TextField(blank=True, null=True)),
                ('translator', models.TextField(blank=True, null=True)),
                ('painter', models.TextField(blank=True, null=True)),
                ('publisher', models.TextField(blank=True, null=True)),
                ('publishdate', models.CharField(blank=True, db_column='publishDate', max_length=50, null=True)),
                ('intro', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('authorintro', models.TextField(blank=True, db_column='authorIntro', null=True)),
                ('categorytop', models.TextField(blank=True, db_column='categoryTop', null=True)),
                ('categorymiddle', models.TextField(blank=True, db_column='categoryMiddle', null=True)),
                ('categorybottom', models.TextField(blank=True, db_column='categoryBottom', null=True)),
                ('isbn', models.TextField(blank=True, db_column='ISBN', null=True)),
                ('bid', models.IntegerField(blank=True, null=True)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bid_crawling',
                'managed': False,
            },
        ),
    ]
