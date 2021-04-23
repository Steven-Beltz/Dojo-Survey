from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')
def revised(request):
    # context = {
    #     'name' = request.session["name"]
    #     'location' = request.session["location"]
    #     'language' = request.session["language"]
    #     'comment' = request.session["comment"]
    # }
    
    return render(request,'results.html')
def results(request):
    if request.method == "POST":
        request.session["name"] = request.POST["name"]
        request.session["location"] = request.POST["location"]
        request.session["language"] = request.POST["language"]
        request.session["comment"] = request.POST["comment"]
    return redirect('/revised')
