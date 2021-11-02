from django.contrib import admin
from .models import Post
from .models import patients
from .models import immunizations
from .models import medicationsallergies
from .models import prescriptions
from .models import chartreports
from .models import appointments
from .models import visits
from .models import recordings
from .models import slots
from .models import appointment_date

admin.site.register(Post)
admin.site.register(patients)
admin.site.register(immunizations)
admin.site.register(medicationsallergies)
admin.site.register(prescriptions)
admin.site.register(chartreports)
admin.site.register(appointments)
admin.site.register(visits)
admin.site.register(recordings)
admin.site.register(slots)
admin.site.register(appointment_date)
