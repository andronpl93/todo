from django.db import models
from django.contrib.auth.models import User

class Projects(models.Model):
    name = models.CharField('Название',max_length=300)
    img = models.IntegerField('Спрайт. Из одмена не использовать',default=15)
    auth = models.ForeignKey(User, on_delete=models.CASCADE )
    def __str__(self):
        return str(self.name)
    class Meta:
            verbose_name = u'Проект'
            verbose_name_plural = u'Проекты'

class  Tasks(models.Model):
    name = models.TextField('Краткое описание')
    pab_date = models.DateTimeField('Время до которого нужно выполнить задачу')
    status = models.BooleanField('Статус. Из одмена не использовать', default=False)
    prior = models.CharField('Приоритет',choices=(('a','Tall'),('b','Middle'),('c','Bottom')),max_length=1,blank=True,default='a')
    project = models.ForeignKey(Projects,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = u'Задание'
        verbose_name_plural = u'Задания'
        ordering=['prior']

# Create your models here.
