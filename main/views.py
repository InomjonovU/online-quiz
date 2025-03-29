from django.shortcuts import render, get_object_or_404
from .models import *

app_name = 'front'

def index(request):
    context = {
        'quizs': Quiz.objects.all()
    }
    return render(request, 'front/index.html', context=context)

def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    correct_answers = 0
    total_questions = questions.count()

    if request.method == "POST":
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer and user_answer == question.answer:
                correct_answers += 1

    score_percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
    return render(request, 'front/result.html', {'quiz': quiz, 'score': score_percentage})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'front/test_detail.html', {'quiz': quiz, 'questions': questions})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, message=message)
        context = {
            'success': True
        }
        return render(request, 'front/contact.html', context=context)
    return render(request, 'front/contact.html')

def filter(request):
    search = request.POST.get('search', '').strip()
    subject = request.POST.get('subject', '')
    class_number = request.POST.get('class_number', '')

    quizzes = Quiz.objects.all()

    if search:
        quizzes = quizzes.filter(title__icontains=search)
    if subject:
        quizzes = quizzes.filter(subject=subject)
    if class_number:
        quizzes = quizzes.filter(class_number=class_number)

    context = {'quizs': quizzes}
    return render(request, 'front/index.html', context)
