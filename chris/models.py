from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings1 = models.CharField(max_length=10)
    greetings2 = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
class About(models.Model):
    heading = models.CharField( max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/', height_field=None, width_field=None, max_length=None)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.career
    
class Profile(models.Model):
    about = models.ForeignKey("About", on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)



    #Skills Section
class Category(models.Model):
    name = models.CharField(max_length=50)
    updated = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

class Skills(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/', height_field=None, width_field=None, max_length=None)
    link = models.URLField(max_length=200)

    def __str__(self) -> str:
        return f'portfolio {self.id}'