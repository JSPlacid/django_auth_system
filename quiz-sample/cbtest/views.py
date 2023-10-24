from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Option, UserResponse
from datetime import datetime


@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()

    context = {
        'quizzes': quizzes
    }

    return render(request, 'quiz_list.html', context)


@login_required
def quiz_question(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    # questions = Question.objects.filter(quiz=quiz)
    questions = quiz.question_set.all()

    if request.method == 'POST':
        # create a UserResponse instance and store them in the database
        # user_answers['quiz_id'] = quiz_id
        for question in questions:
            answer_key = f'question_{question.id}_answer'
            selected_option_id = request.POST.get(answer_key)
            if selected_option_id:
                selected_option = Option.objects.get(id=selected_option_id)
                is_correct = selected_option.is_correct
                UserResponse.objects.create(user=request.user,
                                            quiz=quiz,
                                            question=question,
                                            selected_option=selected_option,
                                            is_correct=is_correct)

        return redirect('submit_quiz')

    context = {
        'quiz': quiz,
        'questions': questions
    }

    return render(request, 'quiz_question.html', context)


@login_required
def submit_quiz(request):
    user_answers = UserResponse.objects.filter(user=request.user)
    quiz = user_answers.first().quiz
    questions = Question.objects.filter(quiz=quiz)

    # Calculate the user's score incrementally based on userResponse instances
    score = user_answers.filter(is_correct=True).count()

    # score = 0
    # for question in questions:
    #     answer_key = f'question_{question.id}_answer'
    #     selected_option_id = user_answers.get(answer_key)
    #     if selected_option_id:
    #         selected_option = Option.objects.get(id=selected_option_id)
    #         if selected_option.is_correct:
    #             score += 1

    #             # return redirect('quiz_list')

    # Get the total number of questions in the quiz
    total_question = Question.objects.filter(quiz=quiz).count()

    # # Calculate the user's score as a percentage
    if total_question != 0:
        user_score_percentage = (score / total_question) * 100
    else:
        # Handle the case where there are no questions
        user_score_percentage = 0

        # Handle quiz duration and submission time (same as previous responses)

        # Render the quiz completion page with the user's score

        # Redirect users to the quiz list if they access the submit page without submitting

    context = {
        'quiz': quiz,
        'score': score,
        'questions': questions,
        'user_score_percentage': user_score_percentage
    }
    return render(request, 'quiz_complete.html', context)


@login_required
def answer_question(request):
    # get all question associated with the logged-in user
    user_responses = UserResponse.objects.filter(user=request.user)

    question_data = []

    for response in user_responses:
        # retrieve the associated question
        question = response.question

        # retrieve all options for the current question
        options = Option.objects.filter(question=question)

        # get selected answer for the user

        # selected_option = response.selected_option

        user_answers = UserResponse.objects.filter(
            user=request.user, question=question)
        if user_answers:  # if user_answers.exists():
            user_selected_option = user_answers.first().selected_option
        else:
            user_selected_option = None
        correct_answer = Option.objects.get(question=question, is_correct=True)

        question_data.append({
            'question': question,
            'options': options,
            'user_selected_option': user_selected_option,
            'correct_answer': correct_answer
            # 'selected_option': selected_option
        })

    return render(request, 'answer_question.html', {'question_data': question_data})
