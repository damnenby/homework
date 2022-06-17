from django.shortcuts import render
from .models import Article, Status, Author, Comment
from django.db.models import Q
# Create your views here.


def index(request):
    return render(request, 'index.html')


def view_comments(request):
    result = []
    comments = Comment.objects.all().order_by('-id')[:5]
    for i in range(0,5):
        result.append(comments[i].text)

    return render(request, 'comments.html', {
        "result": result,
    })

def view_comments_start_middle_finish(request):
    res = []
    comments = Comment.objects.all().order_by('id')[6:11]
    for i in range(0,5):
        res.append(comments[i].text)

    return render(request, 'task2.html', {
        "res": res,
    })

def change_comments_start_middle_finish(request):
    res1 = []
    comments = Comment.objects.filter(Q(text__contains='Start') | Q(text__contains='Finish') | Q(text__contains='Middle'))

    #Обновляем
    Comment.objects.filter(Q(text__contains='Start') | Q(text__contains='Finish') | Q(text__contains='Middle')).update(
        text='updated')

    new_comments = Comment.objects.filter(text__contains='updated')
    for i in list(new_comments):
        res1.append([i.text, i])


    return render(request, 'task3.html', {
        "res1": res1,
    })

def delete_k_objects(request):
    res2 = []

    comments = Comment.objects.filter(text__contains='k').exclude(text__contains='c')

    comments.delete()

    new_comments = Comment.objects.filter(Q(text__contains='k') & Q(text__contains='c'))
    for i in list(new_comments):
        res2.append([i.text, i])


    return render(request, 'task5.html', {
        "res2": res2
    })

def get_last_two_objects(request):
    res3 = []

    author = list(Author.objects.order_by('name'))[-1]

    articles = Article.objects.filter(author=author).order_by('-created_at')[:2]

    for i in list (articles):
        res3.append(f'Article created at{i.created_at}')

    return render(request, 'task6.html', {
        "res3": res3
    })