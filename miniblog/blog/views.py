from django.shortcuts import render , redirect , HttpResponseRedirect , HttpResponse,get_object_or_404
from .forms import Register_form ,LoginForm , BlogPost_form
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import blog_post
from django.contrib.auth.decorators import login_required
# for subscription email
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)

# Create your views here.

# ativate virtual venv "venv\Scripts\activate"

#home
def home(request):
    posts = blog_post.objects.all()
    return render(request, 'home.html', {'posts':posts})



#single view 
def single_data(request , id):
    posts = get_object_or_404( blog_post, id = id)
    return render(request, 'single_data.html', {'posts':posts})
    

#about
def about(request):
    return render(request, 'about.html')



#contact
def contact(request):
    if request.method == 'POST':
        # name = request.POST.get('first_name')
        # # l_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # message = request.POST.get('message')
        # subject = 'New Contact Form Submission.'
        # message_body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        # from_email = 'example@gmail.com'
        # recipient_list = ['vivekudyalak@gmail.com']
        # send_mail(subject, message_body, from_email, recipient_list)
        return HttpResponse('Thank you for your message.')
        print("Result matlab contact form data = :", )
        
    return render(request, 'contact.html')



def manage_post(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            posts = blog_post.objects.all()
        else:
            posts = blog_post.objects.filter(created_by = request.user)
        return render(request , 'manage_post.html' , {'posts':posts})
    else:
        return HttpResponseRedirect('/login/')


#signup
def user_signup(request):
    if request.method == 'POST':
        rgs_form = Register_form(request.POST)
        if rgs_form.is_valid():
            user = rgs_form.save()
            messages.success(request, "Registration successful.Please login")
            print("user is saved : ", user)
            return redirect('login_page')   
    else:
        rgs_form = Register_form()
    return render(request, 'signup.html', {'form':rgs_form})


#login
def user_login(request):
    if not request.user.is_authenticated:
        
        if request.method == 'POST':
            form = LoginForm(request , data = request.POST)
            if form.is_valid():
                user = form.get_user()
                print("user whoose is trying to login :", user)
                if user is not None:
                    login(request, user)
                    messages.success(request ,'you logged in successfully !')
                    print("user login success")
                    return redirect('dashboard_page')
                else:
                    messages.warning(request ,'you logged in fail !')
                    print("user login failed")
                    
            else:
                messages.warning(request, "Invalid Login data")
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')



#logout
def user_logout(request): 
    if request.method == 'POST': 
        logout(request) 
    return redirect('home_page')


#create Blog post
@login_required
def create_blog(request):
    if request.method == 'POST':
        blog_form = BlogPost_form(request.POST, request.FILES)
        if blog_form.is_valid():
            post = blog_form.save(commit = False)
            post.created_by = request.user
            post.save()
            return redirect('manage_post')
    else:
        blog_form = BlogPost_form()
    return render(request, 'blog_post.html', {'blog_form':blog_form})



#Edit Post
def edit_blog(request, id):
    data = blog_post.objects.get(pk = id )
    
    if request.method == 'POST':
        blog_form = BlogPost_form(request.POST, instance= data)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('manage_post')
        
    else:
        blog_form = BlogPost_form(instance= data)
    return render(request, 'blog_post.html',{'blog_form':blog_form})



#delete operations 
def delete_record(request , id):
    data = get_object_or_404(blog_post, id=id, created_by = request.user)
    if request.method == 'POST':
        data.delete()
        print("Post is deleted successfully")
        return redirect('manage_post')
    return render(request, 'confirm_delete.html', {'data':data})
    
    



#dashboard
def user_dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            posts = blog_post.objects.all()
        else:
            posts = blog_post.objects.filter(created_by = request.user)
        return render(request, 'dashboard.html' , {'posts' : posts})
    else:
        return HttpResponseRedirect('/login/')
    
    
    


# news latter subscription 

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print("Subscribe email ", email)
        logger.debug(f"Received email: {email}")
        if email:
            try:
                subject = 'Congratulations on Subscribing!'
                message = f"""
                Dear {email},

                Congratulations on subscribing to our newsletter!

                We are thrilled to have you with us. Here are some things you can look forward to:
                - Weekly updates on the latest trends
                - Exclusive insights and articles
                - Special promotions and offers

                If you have any questions, feel free to contact us. Please note that this is an automated email, and replies to this email address are not monitored.

                Best regards,
                [Your Company Name]

                (no-reply)
                
                """
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(
                    subject,
                    message,
                    from_email,
                    recipient_list,
                    fail_silently=False,
                )
                return HttpResponse('Email sent successfully!')
            except Exception as e:
                logger.error(f"Error sending email: {e}")
                return HttpResponse(f'Error sending email: {e}', status=500)
        else:
            logger.debug("No email provided")
            return HttpResponse('No email provided', status=400)
    logger.debug("Invalid request method")
    return HttpResponse('Invalid request', status=400)