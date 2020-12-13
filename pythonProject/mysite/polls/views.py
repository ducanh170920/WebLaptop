from django.shortcuts import render
from .models import Question
from django.http import HttpResponse
# Create your views here.

def index(request):
    myname = "hahahihi"
    taisan = ["dienthoai", "maytinh", "tivi"]
    context = {"name": myname, "item": taisan}
    return render(request, "polls/index.html", context)
def viewlist(request):
    list_question = Question.objects.all()
    return render(request, "polls/index.html", {"dsquest": list_question, "name": "viet"})
def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/index.html", {"qs": q})
def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    value_of_choice = request.POST['choice']
    # c là câu trả lời dẫn ứng với đáp án đã chọn lấy theo value
    selected_choice = q.choice_set.get(pk=value_of_choice)
    selected_choice.vote = int(selected_choice.vote)
    selected_choice.vote += 1
    selected_choice.save()
    return HttpResponse(selected_choice.vote)