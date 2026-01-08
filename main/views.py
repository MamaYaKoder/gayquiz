from django.shortcuts import render, redirect
from .models import Question
import random

def welcome(request):
    return render(request, 'welcome.html')

def start_quiz(request):
    questions = list(Question.objects.all())
    random.shuffle(questions)
    request.session['questions'] = [q.id for q in questions]
    request.session['current'] = 0
    request.session['score'] = 0
    return redirect('question')

def question(request):
    if 'questions' not in request.session:
        return redirect('welcome')
    
    current = request.session['current']
    questions_ids = request.session['questions']
    
    if current >= len(questions_ids):
        return redirect('result')
    
    q_id = questions_ids[current]
    q = Question.objects.get(id=q_id)
    
    if request.method == 'POST':
        selected = int(request.POST['option'])
        if selected == q.correct_option:
            request.session['score'] += 1
        request.session['current'] += 1
        return redirect('question')
    
    return render(request, 'question.html', {'question': q})

def result(request):
    if 'score' not in request.session:
        return redirect('welcome')
    
    score = request.session['score']
    total = 8  # всего вопросов
    percentage = (score / total) * 100
    score = request.session['score']
    total = 8  # всего вопросов
    percentage = round((score / total) * 100)  # округлим до целого для красоты

    if percentage == 100:
        message = "Лавандовый раф по тебе плачет. Иди дейлики в геншине делай, пидорас 🩵"
    elif percentage > 70:
        message = "Ну слушай, в целом, ещё не всё по... Да кого я обманываю. Пшёл отсюда, гей позорный 🖕"
    elif percentage > 40:
        message = "Ты чуточку гей 😏"
    else:
        message = "Ты натурал 😎"
    
    del request.session['score']
    del request.session['current']
    del request.session['questions']
    
    return render(request, 'result.html', {'message': message, 'percentage': percentage})
