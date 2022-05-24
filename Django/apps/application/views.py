from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Board, Thread, Comment


def boards(request):
    return render(request, 'application/list.html')


def board(request, path):
    search = request.GET.get('search')
    a = Board.objects.get(board_path = path)
    page = request.GET.get('page')
    if search is None:
        latest_threads = list(Thread.objects.filter(board = a).order_by('-pub_date'))
        p = Paginator(latest_threads, 5)
        latest_threads = p.get_page(page)
        return render(request, 'application/board.html', {'Board': a, 'Threads': latest_threads})
    else:
        latest_threads = []
        searches = search.split(" ")
        for s in searches:
            search_list = Thread.objects.filter(
                board = a and
                (Q(thread_title__icontains = s) |
                 Q(thread_text__icontains = s) |
                 Q(thread_title__icontains = s.upper()) |
                 Q(thread_text__icontains = s.upper()) |
                 Q(thread_title__icontains = s.lower()) |
                 Q(thread_text__icontains = s.lower()) |
                 Q(thread_title__icontains = s.capitalize()) |
                 Q(thread_text__icontains = s.capitalize())
                 )
            )
            for i in search_list:
                latest_threads.append(i)
        latest_threads = list(set(latest_threads))
        for i in range(len(latest_threads) - 1):
            for j in range(len(latest_threads) - 1 - i):
                if latest_threads[j].__getattribute__('pub_date') < latest_threads[j+1].__getattribute__('pub_date'):
                    latest_threads[j], latest_threads[j+1] = latest_threads[j+1], latest_threads[j]
        p = Paginator(latest_threads, 5)
        latest_threads = p.get_page(page)
        return render(request, 'application/board.html', {'Board': a, 'Threads': latest_threads, 'Search': search})

def thread(request, path):
    a = Thread.objects.get(id = path)
    latest_comments = list(Comment.objects.filter(thread = a).order_by('-pub_date'))
    p = Paginator(latest_comments, 20)
    page = request.GET.get('page')
    latest_comments = p.get_page(page)
    return render(request, 'application/thread.html', {'Thread': a, 'Comments': latest_comments, 'id': a.thread_id})
