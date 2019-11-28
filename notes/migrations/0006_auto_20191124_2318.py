# Generated by Django 2.2.7 on 2019-11-24 20:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20191124_2314'),
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
            field=models.UUIDField(default=uuid.UUID('00e5ae11-6e07-4d20-a7c4-067363d3be51'), editable=False, primary_key=True, serialize=False),
        ),
    ]
