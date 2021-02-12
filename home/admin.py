from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import BreathingApparatus, ExtinguisingAgent, Rank, Personnel, Incident, Employee, AlarmStatusUponArrival, \
    IncidentResponse, Engines, RopeAndLadder, Station
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class IncidentResource(resources.ModelResource):

    class Meta:
        model = Incident


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)


@admin.register(Station)
class StationAdmin(LeafletGeoAdmin):
    list_display = ('Address',)





@admin.register(ExtinguisingAgent)
class ExtinguisingAgentAdmin(LeafletGeoAdmin):
    list_display = ('Type',)


@admin.register(Engines)
class EnginesAdmin(LeafletGeoAdmin):
    list_display = ('Name', 'Model',)


@admin.register(BreathingApparatus)
class BreathingApparatusForm(LeafletGeoAdmin):
    list_display = ('BreathingApparatusType',)


@admin.register(IncidentResponse)
class IncidentResponseAdmin(LeafletGeoAdmin):
    list_display = ('Incident', 'Engine',)


@admin.register(AlarmStatusUponArrival)
class AlarmStatusUponArrivalAdmin(LeafletGeoAdmin):
    list_display = ('Incident', 'StatusUponArrival', 'StatusUponArrivalRemarks')


@admin.register(Rank)
class InvestigatorRankAdmin(LeafletGeoAdmin):
    list_display = ('Code', 'Definition',)


@admin.register(Personnel)
class InvestigatorAdmin(LeafletGeoAdmin):
    list_display = ('Rank', 'LastName', 'FirstName',)
    search_fields = ('Name',)


class RopeAndLadderInline(admin.TabularInline):
    model = RopeAndLadder


@admin.register(Incident)
class IncidentAdmin(ImportExportModelAdmin):
    list_display = ('DateAlarmReceived', 'OwnerName', 'Barangay',)
    # exclude = ('TotalFatalities','Approved',)
    search_fields = ('Barangay__Name', 'OwnerName',)
    inlines = [
        RopeAndLadderInline,
    ]
    filter = ('Barangay',)
    list_filter = ('Approved', 'Barangay',)
    resource_class = IncidentResource



admin.site.unregister(User)
admin.site.register(User, UserAdmin)
