# Generated by Django 5.1.4 on 2025-01-02 11:51

import autoslug.fields
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business_name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, null=True, populate_from='business_name')),
                ('inn_identification_number', models.CharField(max_length=50)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('business_description', models.TextField()),
                ('business_address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=255)),
                ('bank_bic_number', models.IntegerField()),
                ('bank_account_number', models.CharField(max_length=50)),
                ('bank_routing_number', models.CharField(max_length=50)),
                ('is_approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
