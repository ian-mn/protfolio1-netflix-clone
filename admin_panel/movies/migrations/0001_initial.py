# Generated by Django 4.2.2 on 2023-08-28 00:51

import uuid

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.RunSQL("create schema content;"),
        migrations.CreateModel(
            name="Filmwork",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                (
                    "creation_date",
                    models.DateField(blank=True, verbose_name="creation_date"),
                ),
                (
                    "rating",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ],
                        verbose_name="rating",
                    ),
                ),
                (
                    "image_url",
                    models.URLField(blank=True, null=True, verbose_name="image_url"),
                ),
                (
                    "trailer_url",
                    models.URLField(blank=True, verbose_name="trailer_url"),
                ),
            ],
            options={
                "verbose_name": "Filmwork",
                "verbose_name_plural": "Filmworks",
                "db_table": 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
            ],
            options={
                "verbose_name": "Genre",
                "verbose_name_plural": "Genres",
                "db_table": 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "full_name",
                    models.CharField(max_length=255, verbose_name="full_name"),
                ),
                (
                    "image_url",
                    models.URLField(blank=True, null=True, verbose_name="image_url"),
                ),
            ],
            options={
                "verbose_name": "Person",
                "verbose_name_plural": "Persons",
                "db_table": 'content"."person',
            },
        ),
        migrations.CreateModel(
            name="PersonFilmwork",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "film_work",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.filmwork",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.person",
                        verbose_name="Person",
                    ),
                ),
            ],
            options={
                "verbose_name": "PersonFilmwork",
                "verbose_name_plural": "PersonFilmworks",
                "db_table": 'content"."person_film_work',
            },
        ),
        migrations.CreateModel(
            name="GenreFilmwork",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "film_work",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.filmwork",
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.genre",
                        verbose_name="Genre",
                    ),
                ),
            ],
            options={
                "verbose_name": "GenreFilmwork",
                "verbose_name_plural": "GenreFilmworks",
                "db_table": 'content"."genre_film_work',
            },
        ),
        migrations.AddField(
            model_name="filmwork",
            name="genres",
            field=models.ManyToManyField(
                through="movies.GenreFilmwork", to="movies.genre"
            ),
        ),
        migrations.AddField(
            model_name="filmwork",
            name="persons",
            field=models.ManyToManyField(
                through="movies.PersonFilmwork", to="movies.person"
            ),
        ),
        migrations.AddConstraint(
            model_name="personfilmwork",
            constraint=models.UniqueConstraint(
                fields=("film_work", "person"), name="film_work_person_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="genrefilmwork",
            constraint=models.UniqueConstraint(
                fields=("genre", "film_work"), name="genre_film_work_idx"
            ),
        ),
    ]
