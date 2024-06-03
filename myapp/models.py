from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class STATE_TABLE(models.Model):
    state_name = models.CharField(max_length=25)
    def __str__(self):
        return self.state_name

class CITY_TABLE(models.Model):
    city_name = models.CharField(max_length=25)
    state_id = models.ForeignKey(STATE_TABLE, on_delete=models.CASCADE)
    def __str__(self):
        return self.city_name

class login_table(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    password=models.TextField(max_length=8)
    phone_no=models.BigIntegerField()
    city_id = models.ForeignKey(CITY_TABLE, on_delete=models.CASCADE)
    state_id = models.ForeignKey(STATE_TABLE, on_delete=models.CASCADE)
    ROLE = (
        ("Designer", "Designer"),
        ("User", "User")
    )
    role = models.CharField(max_length=10, choices=ROLE)

    def __str__(self):
        return self.name

class detail_table(models.Model):
    login_id = models.ForeignKey(login_table, on_delete=models.CASCADE)
    i_desc=models.CharField(max_length=300)
    i_experience = models.IntegerField(max_length=10)


    def __str__(self):
        return self.login_id.name

class designs(models.Model):
    login_id = models.ForeignKey(login_table, on_delete=models.CASCADE, default="")
    category=models.CharField(max_length=20)
    Design_Description=models.TextField()

    dimage = models.ImageField(upload_to='photos', null=True)
    def d_photo(self):
        return mark_safe('<img src="{}" width="100"/'.format(self.dimage.url))

    d_photo.allow_tags = True

    def __str__(self):
        return self.category


class bidding(models.Model):
    d_id = models.ForeignKey(designs, on_delete=models.CASCADE, default="")
    login_id = models.ForeignKey(login_table, on_delete=models.CASCADE, default="")
    approx_budget = models.CharField(max_length=35)
    STATUS = (
        ("0", "unapproved"),
        ("1", "approved"),
        ("2", "rejected")
    )
    b_status = models.CharField(max_length=50, choices=STATUS)
    show_interest_button = models.BooleanField(default=True)
    PSTATUS = (
        ("pending", "pending"),
        ("done", "done"),
        ("offline", "offline")
    )
    p_status = models.CharField(max_length=50, choices=PSTATUS, default="pending")
    payment_done = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)



class FEEDBACK_TABLE(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    subject = models.CharField(max_length=300, default="")
    COMMENT = models.CharField(max_length=300, default="")

class complain_TABLE(models.Model):
    login_id = models.ForeignKey(login_table, on_delete=models.CASCADE, default="")
    i_ID = models.ForeignKey(detail_table, on_delete=models.CASCADE, default="")
    Type = models.CharField(max_length=3)
    Description = models.CharField(max_length=300, default="")

