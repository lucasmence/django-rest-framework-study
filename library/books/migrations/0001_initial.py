# Generated by Django 4.2.2 on 2023-06-14 18:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('idBook', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('releaseYear', models.IntegerField()),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
