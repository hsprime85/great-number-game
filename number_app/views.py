from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if "random_number" not in request.session:
        request.session["random_number"] = random.randint(0,100)
    
    if "phrase" not in request.session:
        request.session["phrase"] = "Take a guess!"

    print(request.session["random_number"])
    
    return render(request, "index.html")



def guess_number(request):

    if request.session["random_number"] < int(request.POST["number"]):
        request.session["phrase"] = "Too high!"

    elif request.session["random_number"] > int(request.POST["number"]):
        request.session["phrase"] = "Too low!"

    else:
        request.session["phrase"] = f"{request.session['random_number']} was the number!"


    return redirect("/")

def reset(request):
    request.session.clear()

    return redirect("/")