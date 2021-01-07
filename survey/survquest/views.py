from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Survey
from .forms import SurveyForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def surv_list(request):
    #surveys = Survey.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    surveys = Survey.objects.order_by('published_date')
    print(surveys)
    return render(request, 'survquest/surv_list.html', {'surveys': surveys})

@login_required
def surv_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    return render(request, 'survquest/surv_detail.html', {'survey': survey})

@login_required
def surv_new(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.author = request.user
            survey.published_date = timezone.now()
            survey.save()
            return redirect('surv_detail', pk = survey.pk)
    else:
        form = SurveyForm()
    return render(request, 'survquest/surv_edit.html', {'form': form})

    