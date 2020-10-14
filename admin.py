from django.contrib import admin
import projectApp.models as m


admin.site.register(m.Person)
admin.site.register(m.Personset)