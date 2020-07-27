from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Board, Topic, Post

# Create your views here.

# 1
#def home(request):
#    return HttpResponse('Hello World!')
# 2
#def home(request):
#    boards = Board.objects.all()
#    boards_names = list()
#
#    for board in boards:
#        boards_names.append(board.name)
#    print(boards_names)
#    response_html = '<br>'.join(boards_names)
#    
#    return HttpResponse(response_html)
# 3
def home(request):
    boards = Board.objects.all()
    #print(boards)
    return render(request, 'home.html', {'boards': boards})
def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()

        topic = Topic.objects.create(
            subject = subject,
            board = board,
            starter = user
        )

        post = Post.objects.create(
                message = message,
                topic = topic,
                created_by = user
        )

        return redirect('board_topics', pk=board.pk)
    return render(request, 'new_topic.html', {'board': board})
