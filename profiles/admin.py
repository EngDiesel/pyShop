from django.contrib import admin
from .models import profile, userStripe


# Register your models here.
class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = profile


admin.site.register(profile, profileAdmin)

class userStripeAdmin(admin.ModelAdmin):
    class meta:
        model = userStripe


admin.site.register(userStripe, userStripeAdmin)