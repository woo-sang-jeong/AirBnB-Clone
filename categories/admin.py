from django.contrib import admin
from .models import Category

# CategoryAdmin class를 통해 category 모델을 컨트롤하고 싶다는 뜻이다.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "kind",
    )

    list_filter = ("kind",)
