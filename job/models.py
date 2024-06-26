from django.db import models
JOB_TYPE=(
    ('Full Time','Part Time'),
    ('Part Time','Full Time'),
)

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=0)
    salary=models.IntegerField(default=10)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey('category',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class category(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name