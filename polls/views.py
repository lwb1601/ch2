from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from polls.models import Question, Choice
from django.views import generic
# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})
class Index(generic.ListView):
    model = Question
    context_object_name = 'latest_question_list'
    template_name = 'polls/index.html'


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
class Detail(generic.DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'polls/detail.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['select'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))

# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/result.html', {'question': question})

class Result(generic.DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'polls/result.html'





def reset(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    reset_list = question.choice_set.all()
    for i in reset_list:
        i.votes = 0
        i.save()
    return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))

# class Reset(generic.View):
#     model = Question
#     def cal(self, request, pk):
#         question = get_object_or_404(Question, pk=pk)
#         reset_list = question.choice_set.all()
#         for i in reset_list:
#             i.votes = 0
#             i.save()
#         return HttpResponseRedirect(reverse('polls:result', args=(pk,)))


