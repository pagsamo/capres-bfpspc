from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import BreathingApparatus, ExtinguisingAgent, Rank, Personnel, Incident, Employee, AlarmStatusUponArrival, \
    IncidentResponse, Engines, RopeAndLadder, Station
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)


@admin.register(Station)
class StationAdmin(LeafletGeoAdmin):
    list_display = ('Address',)


@admin.register(Engines)
class EnginesAdmin(LeafletGeoAdmin):
    list_display = ('Name', 'Model',)


@admin.register(Rank)
class InvestigatorRankAdmin(LeafletGeoAdmin):
    list_display = ('Code', 'Definition',)


@admin.register(Personnel)
class InvestigatorAdmin(LeafletGeoAdmin):
    list_display = ('Rank', 'LastName', 'FirstName',)
    search_fields = ('Name',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
