from django.shortcuts import render, redirect, get_object_or_404
from main.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard:index")
        else:
            return render(request, "login.html", {"error": "Noto‘g‘ri login yoki parol!"})

    return render(request, "dashboard/login.html")

@login_required(login_url='dashboard:login')
def index(request):
    quizs = Quiz.objects.all()
    context = {
        'quizs': quizs
    }
    return render(request, 'dashboard/index.html', context=context)

@login_required(login_url='dashboard:login')
def add_quiz(request):
    if request.method == "POST":
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        class_number = request.POST.get('class_number')
        img = request.FILES.get('image')

        if title and subject and description:
            Quiz.objects.create(title=title, subject=subject, description=description, image=img, class_number=class_number)
            return redirect('dashboard:index')

    return render(request, 'dashboard/add_test.html')

@login_required(login_url='dashboard:login')
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    context = {
        'quiz': quiz,
        'questions': questions,
    }
    return render(request, 'dashboard/quiz_detail.html', context)

@login_required(login_url='dashboard:login')
def add_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == 'POST':
        text = request.POST.get('text')
        option_a = request.POST.get('option_a')
        option_b = request.POST.get('option_b')
        option_c = request.POST.get('option_c')
        option_d = request.POST.get('option_d')
        answer = request.POST.get('answer')

        Question.objects.create(
            quiz=quiz,
            text=text,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            answer=answer
        )
        return render(request, 'dashboard/quiz_detail.html', {'quiz': quiz})

    return render(request, 'dashboard/add_question.html', {'quiz': quiz})

@login_required(login_url='dashboard:login')
def edit_question(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question = get_object_or_404(Question, id=question_id, quiz=quiz)

    if request.method == "POST":
        question.text = request.POST.get("text")
        question.option_a = request.POST.get("option_a")
        question.option_b = request.POST.get("option_b")
        question.option_c = request.POST.get("option_c")
        question.option_d = request.POST.get("option_d")
        question.answer = request.POST.get("answer")
        question.save()
        return render(request, "dashboard/quiz_detail.html", {"quiz": quiz})

    return render(request, "dashboard/edit_question.html", {"quiz": quiz, "question": question})


@login_required(login_url='dashboard:login')
def delete_question(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question = get_object_or_404(Question, id=question_id, quiz=quiz)
    question.delete()
    return render(request, "dashboard/quiz_detail.html", {"quiz": quiz})

@login_required(login_url='dashboard:login')
def delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.delete()
    return redirect('dashboard:index')

@login_required(login_url='dashboard:login')
def logout_view(request):
    logout(request)
    return redirect('main:index')

@login_required(login_url='dashboard:login')
def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'dashboard/contacts.html', {'contacts': contacts})