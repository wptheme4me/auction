import imp
from django.contrib import admin
from .models import Category, AuctionListing, User, Comment, Bid
from import_export.admin import ImportExportModelAdmin

# test
class BidsList(admin.ModelAdmin):
    list_display = ('auctionListing', 'bidValue', 'user')

@admin.register(AuctionListing)
class AuctionListingAdmin(ImportExportModelAdmin):
    list_display = ('name', 'serialNumber', 'startBid', 'active')
    pass
# test end


# Register your models here.
admin.site.register(User)
admin.site.register(Category)
# admin.site.register(AuctionListing, Serials)
admin.site.register(Bid, BidsList)
# admin.site.register(Comment)