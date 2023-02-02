from django.shortcuts import render, redirect
from tests.models import TestModel, TestModelCategories
from tests.forms import TestForm, TestFormCategories
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def create_tests(request):
    if request.method == 'POST':
        form = TestFormCategories(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.save()
            return redirect('show_tests')
    elif request.method == 'GET':
        form = TestFormCategories()
        return render(request, 'tests/create_tests.html', {'form':form})



def add_questions(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TestForm(request.POST)
            if form.is_valid:
                post = form.save(commit=False)
                post.save()
                return redirect('add_questions')
        elif request.method == 'GET':
            form = TestForm()
            return render(request, 'tests/add_question.html', {'form':form})
    else:
        return redirect('login')

def show_tests(request):
    tests = TestModelCategories.objects.all()
    count = TestModelCategories.objects.count()
    count_questions = TestModel.objects.count()
    return render(request, 'tests/tests.html',{'tests':tests, 'count':count,'count_questions':count_questions} )


def tests_detail(request, tests_pk):
    if request.user.is_authenticated:
        test = TestModel.objects.filter(category=tests_pk)
        return render(request,'tests/tests_detail.html', {'test':test, 'test_pk':tests_pk})
    else:
        return redirect('login')

def delete_question(request, question_pk):
    test = get_object_or_404(TestModel, pk=question_pk).delete()
    return redirect('show_tests')

def delete_test(request, test_pk):
    if request.user.is_authenticated:
        test = get_object_or_404(TestModelCategories,pk=test_pk ).delete()
        return redirect('show_tests')
    else:
        return redirect('login')

def edit_question(request,question_pk ):
    test = get_object_or_404(TestModel, pk=question_pk)
    if request.method == 'POST':
        form = TestForm(request.POST, instance=test)
        if form.is_valid:
            post = form.save(commit=False)
            post.save()
            return redirect('show_tests')
    elif request.method == 'GET':
        form = TestForm(instance=test)
        return render(request, 'tests/add_question.html', {'form':form})


def testing(request, test_pk):
    test = TestModel.objects.filter(category=test_pk)
    return render(request,'tests/testing.html', {'test':test, 'test_pk':test_pk})

def check(request, test_pk):

    if request.method == 'POST':
        r=request.POST
        print(r)
        # answer = request.POST.get("answer")
        # question_pk = request.POST.get('pk')
        # test = TestModel.objects.get("answer")


        return render(request, 'tests/xz.html', {'r':r})






        