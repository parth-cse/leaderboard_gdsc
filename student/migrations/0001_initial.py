# Generated by Django 4.2.6 on 2023-11-18 15:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('tier', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('completed_gen_ai', models.BooleanField(default=True)),
                ('pathwaycompleted', models.BooleanField(default=False)),
                ('dateofCompletion', models.DateField()),
                ('eligible_for_certificate', models.BooleanField(default=True)),
                ('sized_entered', models.BooleanField(default=False)),
                ('size', models.CharField(blank=True, max_length=1, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('Tier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tier', to='student.tier')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
