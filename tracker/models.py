from django.db import models
from django.contrib.auth.models import User
class Application(models.Model):
    STATUS_CHOICES=[("Saved","Saved"),("Applied","Applied"),("Shortlisted","Shortlisted"),("Interview","Interview"),("Offer","Offer"),("Rejected","Rejected")]
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="applications")
    company=models.CharField(max_length=120)
    role=models.CharField(max_length=150)
    location=models.CharField(max_length=120,blank=True)
    job_url=models.URLField(blank=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="Applied")
    applied_date=models.DateField(null=True,blank=True)
    interview_date=models.DateTimeField(null=True,blank=True)
    notes=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.role} at {self.company}"
