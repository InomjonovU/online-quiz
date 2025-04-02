from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    class_number = models.IntegerField(default=0)
    image = models.ImageField(upload_to='quiz_images/', null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    answer = models.CharField(max_length=1, choices=[
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ])

    def __str__(self):
        return self.text

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['-id']