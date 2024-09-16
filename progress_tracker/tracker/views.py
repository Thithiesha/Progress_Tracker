from django.shortcuts import render
from .models import ExamScore, Subject
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    # Get the subjects and the exam scores for the logged-in user
    subjects = Subject.objects.all()

    # Dictionary to store exam scores grouped by subject
    scores_by_subject = {}
    for subject in subjects:
        exam_scores = ExamScore.objects.filter(user=request.user, subject=subject).order_by('date_of_exam')
        if exam_scores.exists():
            scores_by_subject[subject.subject_name] = exam_scores

    return render(request, 'tracker/dashboard.html', {'scores_by_subject': scores_by_subject})


@login_required
def add_score(request):
    if request.method == 'POST':
        form = ExamScoreForm(request.POST)
        if form.is_valid():
            score = form.save(commit=False)
            score.user = request.user
            score.save()
            return redirect('dashboard')
    else:
        form = ExamScoreForm()

    return render(request, 'tracker/add_score.html', {'form': form})
