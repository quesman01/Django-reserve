from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    # list_display = ('name', 'email', 'date', 'time', 'get_guests')
    list_display = ('name', 'email', 'date', 'time')
    list_filter = ('date', 'time')
    search_fields = ('name', 'email')

    # def get_guests(self, obj):
    #     return obj.guests
    # get_guests.short_description = 'Guests'

admin.site.register(Reservation, ReservationAdmin)


