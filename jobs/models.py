from django.db import models


class Skill(models.Model):
    skill = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.skill


class Job(models.Model):
    LEVEL_CHOICES = (
        ('JR', 'Junior'),
        ('PL', 'Pleno'),
        ('SR', 'Senior'),
    )
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    requirements = models.TextField(blank=True, null=False)
    responsibilities = models.TextField(blank=True, null=False)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='JR')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    skills = models.ManyToManyField(Skill, related_name='jobs')

    def __str__(self):
        return self.title
