import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class UUIDMixin(models.Model):
    """Mixin for models with uuid"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    """Mixin for models with created_at and updated_at DateTimefields."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DatedMixin(models.Model):
    """Mixin to display 'Created on 2023-06-26' like names."""

    def __str__(self) -> str:
        created_str = self.created.strftime("%Y-%m-%d")
        return _("Created on: ") + created_str

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    def __str__(self) -> str:
        return self.name

    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"), blank=True, null=True)

    class Meta:
        db_table = 'content"."genre'
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")


class Person(UUIDMixin, TimeStampedMixin):
    def __str__(self) -> str:
        return self.full_name

    full_name = models.CharField(_("full_name"), max_length=255)
    image_url = models.URLField(_("image_url"), blank=True, null=True)

    class Meta:
        db_table = 'content"."person'
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")


class Filmwork(UUIDMixin, TimeStampedMixin):
    def __str__(self) -> str:
        return self.title

    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"), blank=True)
    creation_date = models.DateField(_("creation_date"), blank=True)
    rating = models.FloatField(
        _("rating"), validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    image_url = models.URLField(_("image_url"), blank=True, null=True)
    trailer_url = models.URLField(_("trailer_url"), blank=True)

    genres = models.ManyToManyField(Genre, through="GenreFilmwork")
    persons = models.ManyToManyField(Person, through="PersonFilmwork")

    class Meta:
        db_table = 'content"."film_work'
        verbose_name = _("Filmwork")
        verbose_name_plural = _("Filmworks")


class GenreFilmwork(UUIDMixin, DatedMixin):
    film_work = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    genre = models.ForeignKey(
        "Genre", on_delete=models.CASCADE, verbose_name=_("Genre")
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'content"."genre_film_work'
        verbose_name = _("GenreFilmwork")
        verbose_name_plural = _("GenreFilmworks")
        constraints = [
            models.UniqueConstraint(
                fields=["genre", "film_work"],
                name="genre_film_work_idx",
            ),
        ]


class PersonFilmwork(UUIDMixin, DatedMixin):
    film_work = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    person = models.ForeignKey(
        "Person", on_delete=models.CASCADE, verbose_name=_("Person")
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'content"."person_film_work'
        verbose_name = _("PersonFilmwork")
        verbose_name_plural = _("PersonFilmworks")
        constraints = [
            models.UniqueConstraint(
                fields=["film_work", "person"],
                name="film_work_person_idx",
            ),
        ]
