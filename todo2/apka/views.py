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

    filt={'day':day,'Projects':Projects.objects.all()}
    tasks=Tasks.objects.filter(status=False).filter(pub_date__gt=datetime.now())   # Статус false означает что задание еще не выполненно
    a=datetime.now()

    return render(request,'apka/todo.html',filt)


def projects(request):
    return render(request, 'apka/todo/project.html',{'projects':Projects.objects.all()})


def tasks(request):

    id_project=request.POST.get('id_projects') or None
    if request.POST.get('day'):
        global day
        day=int(request.POST.get('day'))

    if id_project is not None:                                                     # Выборка по конкретному проекту, если он есть
        tasks=Tasks.objects.filter(project=id_project)
    else:
        tasks = Tasks.objects.filter(status=False)  # Статус false означает что задание еще не выполненно

                                         # Сортировка находится в ordering
    later=tasks.filter(pub_date__lt=datetime.now())   #Просроченные задания
    tasks = tasks.filter(pub_date__gt=datetime.now())         #не просроченные задания
    if day:                                                                   #  если day не 0, знач есть фильтр по дням
        tasks = tasks.filter(pub_date__lt=datetime.date(datetime.now()+timedelta(days=day)))

    return render(request, 'apka/todo/tasks.html', {'Later':later,'Tasks':tasks})

@log
def identificator(request):
    id_tasks = request.POST.get('id')
    sta = request.POST.get('status')
    sta = sta!='True' and True or False
    t=Tasks.objects.get(id=int(id_tasks))   # исключение обрабатывать не буду
    t.status=sta
    t.save()
    return HttpResponse(sta)



logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s %(levelname)s %(message)s',
)