from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from Blogs.models import Post
# Create your views here.

def home(request):
    allposts = Post.objects.all()
    context = {'allposts': allposts}
    return render(request,'home/home.html',context)

def about(request):return render(request,'home/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        # print(name,phone,email,content)
        if len(name)<3 or len(email)<5 or len(phone)<10 or len(content)<3:
            messages.add_message(request, messages.ERROR, 'Fill the form Correctly')
        else:
            contact = Contact(name = name ,email = email ,phone = phone , content = content)
            contact.save()
            messages.add_message(request, messages.SUCCESS, 'Thanks for filling the form')


    return render(request,'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allpost = Post.objects.none()
    else:
        allpost = Post.objects.filter(title__icontains=query)
        allpost = Post.objects.filter(author__icontains=query)
        allpost = Post.objects.filter(content__icontains=query)

    if allpost.count() == 0:
        messages.warning(request,"Please refine your query")
    params = {'allpost':allpost,
              'query':query}
    return render(request,'home/search.html',params)

def signin(request):
    if request.method == "POST":
        # parameters
        fname = request.POST['inputfname']
        lname = request.POST['inputlname']
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['inputemail']

        if(password2 == password):
            #creating user
            myuser = User.objects.create_user(username,email,password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.add_message(request, messages.SUCCESS, 'your account has been created')
            return redirect('home')

        else:
            messages.add_message(request, messages.ERROR, 'Error Signing in')
            return redirect('home')

def blogin(request):
    if request.method =="POST":
        #parameters for post
        loginusername = request.POST["lusername"]
        loginpassword = request.POST["Password"]

        user = authenticate(username = loginusername,password = loginpassword)
        if user is None:
            messages.error(request,"Invalid Credentials")
            return redirect('home')
        else:
            login(request, user)
            messages.success(request,"Successfully logged in ")
            return redirect('home')
    else:return HttpResponse("Lawda")

def blogout(request):
    if request.method == "GET":
        logout(request)
        messages.error(request, "You have been logged out")
        return redirect('home')




