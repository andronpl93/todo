from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from datetime import datetime, timedelta
from .models import Projects,Tasks
from apka.hlam import log
import logging
from django.core import serializers

# Create your views here.
day=1

@log                            # я знаю про существование login_required, просто захотел сделать свой декоратор
def start(request,archive=False):
    global day
    day=1
    filt={'day':day,'Projects':Projects.objects.filter(auth=request.user)}
    filt['archive']=archive
    return render(request,'apka/todo.html',filt)


def projects(request,archive=False):
    pr=[]
    for i in Projects.objects.filter(auth=request.user):
        pr.append({})
        pr[-1]['id']=i.id
        pr[-1]['img']=i.img
        pr[-1]['name']=i.name
        pr[-1]['taskCount']=i.tasks_set.filter(status=archive).count()  #не делать p.tasks_set.count в шаблоне,так как нужен этот фильтр
    return render(request, 'apka/todo/project.html',{'projects':pr,'archive':archive})


def tasks(request,archive=False):
    # Сортировка находится в ordering
    id_project=request.POST.get('id_projects') or None
    if request.POST.get('day'):
        global day
        day=int(request.POST.get('day'))

    tasks = Tasks.objects.filter(project__auth=request.user).filter(status=archive)  # Статус false означает что задание еще не выполненно

    f=tasks.filter(pub_date__gt=datetime.now())

    if id_project is not None:                                                     # Выборка по конкретному проекту, если он есть
        tasks=tasks.filter(project=id_project)
    else:
        if day:
            tasks = tasks.filter(pub_date__lt=datetime.date(datetime.now()+timedelta(days=day)))

    later=tasks.filter(pub_date__lt=datetime.now())   #Просроченные задания
    tasks = tasks.filter(pub_date__gt=datetime.now())         #не просроченные задания
    #обновление количества для фильтров  Обновление находится здеть, так как каждое изменение количества записей будет открывать этот метод
    filt={}
    a=datetime.now()
    filt['today']=len(f.filter(pub_date__lt=datetime.date(a+timedelta(days=1))))
    filt['seven']=len(f.filter(pub_date__lt=datetime.date(a+timedelta(days=7))))
    filt['all']=len(f)
    return render(request, 'apka/todo/tasks.html', {'Later':later,'Tasks':tasks,'filt':filt,'archive':archive})

@log
def identificator(request,archive=False):
    id_tasks = request.POST.get('id')
    sta = request.POST.get('status')
    sta = sta!='True' and True or False
    t=Tasks.objects.get(id=int(id_tasks), project__auth=request.user)   # исключение обрабатывать не буду
    t.status=sta
    t.save()
    return HttpResponse(sta)
@log
def add_edit(request,archive=False):
    a=request.POST.get
    p=Projects.objects.get(id=int(a('project')),auth=request.user)
    dt=datetime.strptime(a('pub_date')+' ','%Y-%m-%d %H:%M ')
    if a('id_tasks'):
        t=Tasks.objects.get(id=int(a('id_tasks')), project__auth=request.user)
        t.name=a('name')
        t.pub_date=dt
        t.prior=a('priority')
        t.project=p
    else:
        t=Tasks(name=a('name'),pub_date=dt,status=False,prior=a('priority'),project=p)
    t.save()
    return HttpResponse('1')

@log
def del_task(request,archive=False):

    t=Tasks.objects.get(id=int(request.POST.get('id_task')), project__auth=request.user).delete();
    return HttpResponse('1')


@log
def add_pr(request,archive=False):
    a=request.POST.get
    logging.debug(a('id_project'))
    if a('id_project'):
        p=Projects.objects.get(id=int(a('id_project')), auth=request.user)
        p.name=a('name')
        p.img=a('img')
    else:
        p=Projects(name=a('name'),img=a('img'),auth=request.user)
    p.save()
    return HttpResponse('1')

@log
def del_pr(request,archive=False):
    p=Projects.objects.get(id=int(request.POST.get('id_pr')),auth=request.user);
    if p.tasks_set.filter(status=False).count():
        return HttpResponse('0')
    p.delete()
    return HttpResponse('1')


def upd_select(request,archive=False):
    p=Projects.objects.filter(auth=request.user)
    return HttpResponse(serializers.serialize('json', list(p), fields=('name','id')))


logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s %(levelname)s %(message)s',
)