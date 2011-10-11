from django.contrib import admin

class CreatedByAdminModel(admin.ModelAdmin):
    exclude = ('created_by', )

class UpdatedByAdminModel(admin.ModelAdmin):
    exclude = ('updated_by', )

class CreatedUpdatedByAdminModel(admin.ModelAdmin):
    exclude = ('created_by', 'updated_by')
