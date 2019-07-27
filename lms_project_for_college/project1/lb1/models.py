from django.db import models
from django.urls import reverse_lazy



class Book(models.Model):
    name = models.CharField(max_length=256)
    author_name = models.CharField(max_length=256)
    publication = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('home1')


class Student(models.Model):
    book = models.ForeignKey(Book, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    semester = models.CharField(max_length=256)
    student_id = models.PositiveIntegerField()
    father_name = models.CharField(max_length=256)
    mobile_no = models.PositiveIntegerField()
    aadhar = models.PositiveIntegerField()
    address = models.CharField(max_length=256)
    Pin_code = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('home1')
