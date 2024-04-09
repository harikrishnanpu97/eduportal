from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.name



class Registration(models.Model):
    s_name = models.CharField(max_length=255)
    s_phone = models.CharField(max_length=255)
    s_email = models.EmailField()
    dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
