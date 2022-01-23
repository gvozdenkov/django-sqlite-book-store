from django.db import models
from django.urls import reverse         #for get_absolut_url()
from django.utils.text import slugify   #for def save()
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# создаём свой класс Book, который наследуется от джанго класса medels.Model
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=
        [MinValueValidator(1),
        MaxValueValidator(5)
        ])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)       #Harry Potter -> harry-potter

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("book-detail-page", args=[self.slug])
    
    # def save(self, *args, **kwargs) -> None:
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)