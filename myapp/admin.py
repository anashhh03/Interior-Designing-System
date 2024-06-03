from django.contrib import admin
from .models import login_table,STATE_TABLE,CITY_TABLE,detail_table,designs,bidding,FEEDBACK_TABLE,complain_TABLE

# Register your models here.
class displaylogin(admin.ModelAdmin):
    list_display = ['name','email','password','phone_no','city_id','state_id','role']
admin.site.register(login_table,displaylogin)

class displaystate(admin.ModelAdmin):
    list_display = ['state_name']
admin.site.register(STATE_TABLE,displaystate)

class displaycity(admin.ModelAdmin):
    list_display = ['city_name','state_id']
admin.site.register(CITY_TABLE,displaycity)

class displayinterior(admin.ModelAdmin):
    list_display = ['login_id','i_desc','i_experience']
admin.site.register(detail_table,displayinterior)


class workdetails(admin.ModelAdmin):
    list_display = ["login_id","category","Design_Description","d_photo"]
admin.site.register(designs,workdetails)


class request_table(admin.ModelAdmin):
    list_display = ["d_id","login_id","approx_budget","b_status","show_interest_button","payment_done","rejected"]
admin.site.register(bidding,request_table)


class Feedback_Table(admin.ModelAdmin):
    list_display = ["name","email","subject","COMMENT"]
admin.site.register(FEEDBACK_TABLE,Feedback_Table)


class complain(admin.ModelAdmin):
    list_display = ["login_id","i_ID","Type","Description"]
admin.site.register(complain_TABLE,complain)


