from django.db import models
from django.urls import reverse


class Film(models.Model):
    title = models.CharField(max_length=150)
    poster = models.ImageField(upload_to="media/posters")
    description = models.TextField()
    pub_year = models.PositiveIntegerField()
    genre = models.ManyToManyField("Genre")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("film-detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["pub_year"]


class Genre(models.Model):
    slug = models.SlugField(max_length=55, primary_key=True)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

