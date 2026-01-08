from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='questions/', null=True, blank=True)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.IntegerField()  # 1 для option1, 2 для option2 и т.д. (правильный ответ, который считается "геем")

    def __str__(self):
        return self.text