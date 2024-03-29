# Generated by Django 2.2.7 on 2019-11-24 20:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20191124_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='notes.Category'),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.UUIDField(default=uuid.UUID('be8b1d7b-46b0-4d77-92e8-e11c3189120d'), editable=False, primary_key=True, serialize=False),
        ),
    ]
