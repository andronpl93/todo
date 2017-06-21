from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from datetime import datetime, timedelta
from .models import Projects,Tasks
from .hlam import log
import logging

# Create your views here.
day=1

@log                            # я знаю про существование login_required, просто захотел сделать свой декоратор
def start(request):

    filt={'day':day}
    tasks=Tasks.objects.filter(status=False).filter(pab_date__gt=datetime.now())   # Статус false означает что задание еще не выполненно
    a=datetime.now()
    filt['today']=len(tasks.filter(pab_date__lt=datetime.date(a+timedelta(days=1))))
    filt['seven']=len(tasks.filter(pab_date__lt=datetime.date(a+timedelta(days=7))))
    filt['all']=len(tasks)

    return render(request,'apka/todo.html',filt)

@log
def projects(request):
    return render(request, 'apka/todo/project.html',{'projects':Projects.objects.all()})

@log
def tasks(request):

    id_project=request.POST.get('id_projects') or None
    if request.POST.get('day'):
        global day
        day=request.POST.get('day')

    tasks=Tasks.objects.filter(status=False)    # Статус false означает что задание еще не выполненно

                                                 # Сортировка находится в ordering
    later=tasks.filter(pab_date__lt=datetime.now())   #Просроченные задания

    tasks = tasks.filter(pab_date__gt=datetime.now())         #не просроченные задания
    if not day:                                                                   #  если day не 0, знач есть фильтр по дням
        tasks = tasks.filter(pab_date__lt=datetime.date(a + timedelta(days=day)))

    if id_project is not None:                                                     # Выборка по конкретному проекту, если он есть
        tasks=tasks.filter(project=id_project)



    return render(request, 'apka/todo/tasks.html', {'Later':later,'Tasks':tasks})

logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s %(levelname)s %(message)s',
)