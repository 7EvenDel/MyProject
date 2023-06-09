from django.db import models

class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Description')

    def _str_(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'