# Generated by Django 4.2.5 on 2023-10-13 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0004_rename_distname_branch_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccountApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('account_type', models.CharField(max_length=50)),
                ('materials_required', models.BooleanField()),
            ],
        ),
    ]
