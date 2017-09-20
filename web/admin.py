from django.contrib import admin

# Register your models here.
from .models import Names

from .models import Cars
from .models import Cars_lines

from .models import Duties

from .models import Maintenance


class NamesAdmin(admin.ModelAdmin):
    list_display = ('name','age')
    search_fields = ('name', 'age')
class CarsAdmin(admin.ModelAdmin):
    list_display = ('car_name','number','Cooler')
    search_fields = ('car_name','number','Cooler')

class Cars_linesAdmin(admin.ModelAdmin):
    list_display = ('name','car_name','place','number_of_Employees')
    search_fields = ('name','car_name','place','number_of_Employees')

class DutiesAdmin(admin.ModelAdmin):
    list_display = ('name','car','type','place','Counter','date','time')
    search_fields = ('name','car','type','place','Counter','date','time')
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('name','car','type_of_problem','case','possibility_of_fix','date','time')
    search_fields = ('name','car','type_of_problem','case','possibility_of_fix','date','time')
admin.site.register(Names, NamesAdmin)
admin.site.register(Cars, CarsAdmin)
admin.site.register(Cars_lines, Cars_linesAdmin)
admin.site.register(Duties, DutiesAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)