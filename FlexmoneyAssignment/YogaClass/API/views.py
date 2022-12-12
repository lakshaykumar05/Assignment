from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse

# Create your views here.

def ValidateAndSaveData(request):
    
    if request.method == 'POST':
        
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        batchType = request.POST['batchType']
        paymentStatus = False

        if name == "" or age == "" or email == "" or batchType == "":
            return HttpResponse('Please fill all details correctly')

        if int(age) < 18 or int(age) > 65:
            return HttpResponse('Error! Age must be between 18 and 65')

        if not User.objects.filter(email = email).exists():
            newUser = User(name = name, email = email, age = age, batchType = batchType, paymentStatus = paymentStatus)
            newUser.save()

            # CompletePayment(newUser)

            return HttpResponse('Details have been successfully submitted!')
        else:
            return HttpResponse('Email already exists!')

    return render(request, 'index.html', {})


def CompletePayment(request):

    if request.method == 'POST':

        email = request.POST['email']

        checkCurrentUser = User.objects.filter(email = email)

        if not checkCurrentUser:
            return HttpResponse('Incorrect Email!')

        checkCurrentUser = User.objects.filter(email = email).values()

        # print(checkCurrentUser)

        if checkCurrentUser[0]['paymentStatus']:
            return HttpResponse('Payment Already done!')

        currentUser = User.objects.filter(email = email).update(paymentStatus = True)

        return HttpResponse('Payment done!')

    # return render(request, 'index.html', {})