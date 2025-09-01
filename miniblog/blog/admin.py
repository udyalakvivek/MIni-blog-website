from django.contrib import admin
from .models import blog_post,dasboard_page

# Register your models here.
@admin.register(blog_post)
class blog_postModelAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'short_desc', 'author' , 'category', 'summary_preview']
    readonly_fields = ['summry']
    list_filter = ['author', 'category']

    
    
    def short_desc(self,obj):
        if obj.desc and len(obj.desc) > 75: 
            return (obj.desc[:75]+ '...')
        return obj.desc
    short_desc.short_description = "Description"
    
    
    def summary_preview(self, obj):
        if obj.summry and len(obj.summry)> 50:
            return (obj.summry[:50]+ '...')
        return obj.summry
    summary_preview.short_description = "Summary"

@admin.register(dasboard_page)
class dashboard_data(admin.ModelAdmin):
    list_display = ['id', 'dpImage','created_by','created_at']