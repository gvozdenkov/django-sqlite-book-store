from tabnanny import verbose
from django.db import models
from django.forms import model_to_dict
from django.urls import reverse         #for get_absolut_url()
from django.utils.text import slugify   #for def save()
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self) -> str:
        return f"{self.name}, {self.code}"

class Adress(models.Model):
    street = models.CharField(max_length=80)
    post_code = models.CharField(max_length=5)
    city = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.street}, {self.post_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.OneToOneField(Adress, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name()

# создаём свой класс Book, который наследуется от джанго класса medels.Model
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=
        [MinValueValidator(1),
        MaxValueValidator(5)
        ])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)       #Harry Potter -> harry-potter
    published_countries = models.ManyToManyField(Country)

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("book-detail-page", args=[self.slug])
    
    # def save(self, *args, **kwargs) -> None:
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)