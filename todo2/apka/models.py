from django.db import models
from django.contrib.auth.models import User

class Projects(models.Model):
    name = models.CharField('Название',max_length=100)
    description = models.TextField('Подробное описание',blank = True, max_length=500)
    img = models.IntegerField('Спрайт. Из одмена не использовать',default=15)
    auth = models.ForeignKey(User, on_delete=models.CASCADE )
    class Meta:
            verbose_name = u'Проект'
            verbose_name_plural = u'Проекты'

class  Tasks(models.Model):
    name = models.CharField('Краткое описание',max_length=100)
    desctiption = models.TextField('Информация полезная для задачи(напр. телефоны, адреса, список продуктов)',blank = True, max_length=500)
    date = models.DateTimeField('Время до которого нужно выполнить задачу')
    status = models.BooleanField('Статус. Из одмена не использовать', default=False)
    project = models.ForeignKey(Projects,on_delete=models.CASCADE)
    class Meta:
        verbose_name = u'Задание'
        verbose_name_plural = u'Задания'

# Create your models here.
