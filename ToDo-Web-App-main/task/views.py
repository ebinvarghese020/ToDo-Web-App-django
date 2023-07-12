from django.shortcuts import render, redirect
from .models import Task
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    upcomming = []
    completed = []
    expired = []

    tasks = Task.objects.filter(user_id=request.user.id)
    for i in tasks:
        try:
            time1 = str(i.deadline)[:19]
            deadline = datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")
            print(f" Deadline for project : {deadline}")

            time2 = timezone.now()
            time2 = str(time2.replace(tzinfo=timezone.utc).astimezone(tz=None))[:19]
            now = datetime.strptime(time2, "%Y-%m-%d %H:%M:%S")
            print(f" Datetime now : {now}")

            if i.completed:
                print("task completed")
                completed.append(i)
            

            elif deadline<now:
                print("time expired_____")
                print(f"time expired to do the task : {i.title} ***********")
                expired.append(i)
            else:
                print(f"There is still time to do the task : {i.title} ---------")
                upcomming.append(i)
        except Exception as e:
            print(e)
    
    # print(len(upcomming), len(completed), len(expired))

    now_date_time = str(datetime.now())[:16].replace(' ', 'T')
    print(now_date_time,"-------------------")
    return render(request, 'index.html', {'upcomming':upcomming, 'completed':completed, 'expired':expired, 'now':now_date_time})

@login_required
def create_new_task(request):
    title = request.POST['title']
    description = request.POST['desc']
    deadline = request.POST['deadline']
    print(title)
    print(description)
    print(deadline)

    new_task = Task(title=title, desc=description, deadline=deadline, user_id=request.user.id, published=datetime.now())
    new_task.save()

    return redirect('/')

@login_required
def mark_as_complete(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('/')

@login_required
def mark_as_incomplete(request, id):
    task = Task.objects.get(id=id)
    task.completed = False
    task.save()
    return redirect('/')

@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')

@login_required
def edit_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['desc']
        timelimit = request.POST['deadline']

        task.title = title
        task.desc = description
        task.deadline = timelimit
        task.save()

        return redirect('/')


    
    # print(task.desc)
    # print(task.deadline)
    deadline = str(task.deadline)[:16]
    # print(deadline, type(deadline))
    deadline= deadline.replace(' ', 'T')

    
    return render(request, 'taskedit.html', {'task':task, 'deadline':deadline})

