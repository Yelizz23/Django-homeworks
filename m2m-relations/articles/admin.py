from .models import Article, Relationship, Tag

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            for key, value in form.cleaned_data.items():
                if key == 'is_main' and value is True:
                    counter += 1
        if counter > 1:
            raise ValidationError('Основной раздел может быть только один.')

        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    list_display = ('id', 'title', 'text', 'published_at', 'image')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass