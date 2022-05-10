# Generated by Django 4.0.4 on 2022-05-10 16:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c22968e7-fea2-433b-a2bc-87df297a60e1'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='parent',
            name='id',
            field=models.UUIDField(default=uuid.UUID('21825b98-45e4-493c-bdf9-35e25ad9eba4'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3d685abe-008b-4bb6-bbbd-6764298b23f6'), editable=False, primary_key=True, serialize=False),
        ),
    ]
