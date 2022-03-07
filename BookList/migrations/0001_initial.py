from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='WriterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('synopsis', models.TextField()),
                ('release_date', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BookList.genremodel')),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BookList.writermodel')),
            ],
        ),
    ]
