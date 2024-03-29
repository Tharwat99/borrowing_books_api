# Generated by Django 4.2.7 on 2024-02-19 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'footers',
                'db_table': 'books',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='BorrowRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrower_name', models.CharField(max_length=100)),
                ('borrow_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
            options={
                'verbose_name': 'borrow record',
                'verbose_name_plural': 'borrow records',
                'db_table': 'borrow_records',
                'ordering': ['-borrow_date'],
            },
        ),
    ]
