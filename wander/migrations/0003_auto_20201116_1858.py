# Generated by Django 3.1.3 on 2020-11-16 15:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wander', '0002_auto_20201116_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='PosterEvent',
            fields=[
                ('places_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wander.places')),
                ('date_event_start', models.DateField(default=django.utils.timezone.now)),
                ('date_event_end', models.DateField(default=None, null=True)),
                ('name_event', models.CharField(default='add_name_event', max_length=30)),
                ('ended', models.BooleanField(default=False)),
            ],
            bases=('wander.places',),
        ),
        migrations.DeleteModel(
            name='Poster',
        ),
    ]
