from django.contrib import admin
from .models import Article, Tag, ArticleScope
from django.forms import BaseInlineFormSet, ValidationError


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_category = 0
        categories = []
        for form in self.forms:
            if form.cleaned_data.get('tag'):
                if form.cleaned_data.get('tag').name in categories:
                    raise ValidationError('Категории дублируются')
                else:
                    categories.append(form.cleaned_data.get('tag').name)
            if form.cleaned_data.get('is_main'):
                main_category += 1

        if main_category > 1:
            raise ValidationError('Выберите только 1 основную категорию')
        elif main_category == 0:
            raise ValidationError('Выберите основную категорию')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = RelationshipInlineFormset


@admin.register(Tag)
class ScopeAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
    inlines = [ScopeInline]