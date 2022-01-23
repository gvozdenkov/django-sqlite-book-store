from django.contrib import admin

from . models import Book

# Register your models here.

# спец класс для настройки админки Book + <Admin>. Чтобы поле было только читаемо, например
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author")

# этот модуль добавить в админскую панель
# для настройки вида добавить BookAdmin
admin.site.register(Book, BookAdmin)