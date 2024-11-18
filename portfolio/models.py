from django.db import models

# Create your models here.
class Education(models.Model):
    time_period = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    cgpa = models.CharField(max_length=50)
    def __str__(self):
        return self.institution

class Experience(models.Model):
    time_period = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    point_1 = models.CharField(max_length=100)
    point_2 = models.CharField(max_length=100)
    point_3 = models.CharField(max_length=100)
    point_4 = models.CharField(max_length=100)
    def __str__(self):
        return self.company
class ProjectDetails(models.Model):
    p_name=models.CharField(max_length=255)
    p_desc=models.TextField()
    p_link=models.CharField(max_length=255)
    p_image=models.ImageField(upload_to="project_images")
    def __str__(self):
        return self.p_name

class BlogData(models.Model):
    b_title=models.CharField(max_length=255)
    b_desc=models.TextField()
    b_link=models.CharField(max_length=255)
    b_image=models.ImageField(upload_to="blog_images/")
    def __str__(self):
        return self.b_title