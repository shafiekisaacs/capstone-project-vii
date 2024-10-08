from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice


def index(request):
    """
    Renders a view to display a list of the latest questions.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML page displaying the latest questions.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/poll.html', context)

def detail(request, question_id):
    """
    Renders a view to display the details of a specific question.

    Args:
        request: The HTTP request object.
        question_id: The ID of the question to display.

    Returns:
        A rendered HTML page displaying the question details.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """
    Renders a view to display the results of a specific question.

    Args:
        request: The HTTP request object.
        question_id: The ID of the question to display results for.

    Returns:
        A rendered HTML page displaying the question results.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    """
    Handles user voting on a specific question by updating the vote count.

    Args:
        request: The HTTP request object.
        question_id: The ID of the question being voted on.

    Returns:
        An HTTP redirect to the results page for the voted question.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
        )




