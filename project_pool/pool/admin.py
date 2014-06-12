from django.contrib import admin
from models import (
    Brand,
    Category,
    Budget,
    Idea
)
import reversion


class BrandAdmin(reversion.VersionAdmin):
    pass


class CategoryAdmin(reversion.VersionAdmin):
    pass


class BudgetAdmin(reversion.VersionAdmin):
    pass


class IdeaAdmin(reversion.VersionAdmin):
    pass


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Idea, IdeaAdmin)
