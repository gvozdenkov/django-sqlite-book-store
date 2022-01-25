from django.contrib import admin

from . models import Adress, Author, Book, Country

# Register your models here.

# спец класс для настройки админки Book + <Admin>. Чтобы поле было только читаемо, например
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author")

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "adress")



# этот модуль добавить в админскую панель
# для настройки вида добавить BookAdmin
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Adress)
admin.site.register(Country)
