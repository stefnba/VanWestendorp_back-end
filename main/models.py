from django.db import models

from django.core.validators import MaxValueValidator


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    hash_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)

class Question_Type(models.Model):
    name = models.CharField(max_length=255)
    name_short = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)

class Question(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    type = models.ForeignKey(Question_Type, on_delete=models.CASCADE)
    rank = models.IntegerField()
    category = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    input_suffix = models.CharField(max_length=3, blank=True, null=True)
    input_prefix = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        ordering = ['project', 'rank']

    def __str__(self):
        return '{}: {}'.format(self.project, self.question)


class Input_Title(models.Model):
    question = models.ForeignKey(Question, related_name='input_title', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    order = models.IntegerField()
    is_writeable = models.BooleanField(default=True)
    is_prefilled = models.IntegerField(blank=True, null=True)
    decimal_scale = models.IntegerField(default=0, validators=[MaxValueValidator(4)])

    class Meta:
        ordering = ['question', 'order']

    def __str__(self):
        return '{}: {}: {}'.format(self.question.project, self.question.question, self.title)

class Input_Answer(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    input_title = models.ForeignKey(Input_Title, on_delete=models.CASCADE)
    input = models.DecimalField(max_digits=20, decimal_places=6)
    
    def __str__(self):
        return '{}: {}'.format(self.input_title, self.input)

class Input_User(models.Model):
    answer = models.ManyToManyField(Input_Answer, related_name='fav')
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {} @ {}'.format(self.project, self.name, self.created_at)