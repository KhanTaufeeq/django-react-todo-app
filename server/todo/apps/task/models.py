from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Task(models.Model):

    title = models.CharField('Title', max_length = 50, blank = False, null = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'task')
    body = models.TextField('Body', max_length = 500, blank = True, null = True) 
    created_at = models.DateTimeField('Created', default = timezone.now)
    updated_at = models.DateTimeField('Updated', default = timezone.now)

    def __str__(self):
        return self.title
    

# why do we link an entire User object as a foreign key instead of just user_id ?

# Linking the User object as a foreign key gives you access to the full User instance, provides powerful ORM capabilities, and maintains data integrity.
# Storing just the user_id would require manual SQL handling, make code more complex, and lose Django’s built-in relationship management features.