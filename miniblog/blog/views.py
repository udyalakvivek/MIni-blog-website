from django.shortcuts import render , redirect , HttpResponseRedirect , HttpResponse,get_object_or_404
from .forms import Register_form ,LoginForm , BlogPost_form
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import blog_post
from django.contrib.auth.decorators import login_required
# for subscription email
from django.core.mail import send_mail,EmailMultiAlternatives
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
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile_number')
        message = request.POST.get('message')
        subject = 'Contact Form submission'
        # personal email where you want to send contact form data 
        email_data = {
            'first_name':request.POST.get('first_name'),
            'last_name':request.POST.get('last_name'),
            "email": request.POST.get('email'),
            'mobile':request.POST.get('mobile_number'),
            'message':request.POST.get('message')
            }
        send_subscription_email(email_data)
        return redirect('contact_page')
        messages.success(request, 'Thanks for contacting us! We will get back to you shortly.')
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
                <html>
                <body>
                    <p>Dear {email},</p>
                    <p>Congratulations on subscribing to our newsletter!</p>
                    <p>We are thrilled to have you with us. Here are some things you can look forward to:</p>
                    <ul>
                        <li>Weekly updates on the latest trends</li>
                        <li>Exclusive insights and articles</li>
                        <li>Special promotions and offers</li>
                    </ul>
                    <p>If you have any questions, feel free to contact us. Please note that this is an automated email, and replies to this email address are not monitored.</p>From Blog Team</p>
                    <p>(no-reply)</p>
                </body>
                </html>
                
                """
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                # send_mail(
                #     subject,
                #     message,
                #     from_email,
                #     recipient_list,
                #     fail_silently=False,
                # )
                msg = EmailMultiAlternatives(subject, "", from_email, recipient_list)
                msg.attach_alternative(message, "text/html")
                msg.send()

                return redirect('success_subscribe')
            except Exception as e:
                logger.error(f"Error sending email: {e}")
                return HttpResponse(f'Error sending email: {e}', status=500)
        else:
            logger.debug("No email provided")
            return HttpResponse('No email provided', status=400)
    logger.debug("Invalid request method")
    return HttpResponse('Invalid request', status=400)



#successfully Subscribing 
def success(request):
    return render(request, 'SubscribeSuccess.html')



def send_subscription_email(data):
    # clt + shift + p
    print('➡ miniblog/blog/views.py:238 data type:', data)
    subject = 'Congratulations on Subscribing!'
    message = f"""
    <html>
    <body>
        <p>Dear You received a Contact subscription,</p>

<table style="border: 1px solid black; border-collapse: collapse;">
    <thead>
        <tr>
            <th style="border: 1px solid black; padding: 8px;">First Name</th>
            <th style="border: 1px solid black; padding: 8px;">Last Name</th>
            <th style="border: 1px solid black; padding: 8px;">Email</th>
            <th style="border: 1px solid black; padding: 8px;">Phone</th>
            <th style="border: 1px solid black; padding: 8px;">Message</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid black; padding: 8px;">{data['first_name']}</td>
            <td style="border: 1px solid black; padding: 8px;">{data['last_name']}</td>
            <td style="border: 1px solid black; padding: 8px;">{data['email']}</td>
            <td style="border: 1px solid black; padding: 8px;">{data['mobile']}</td>
            <td style="border: 1px solid black; padding: 8px;">{data['message']}</td>
        </tr>
    </tbody>
</table>

    </body>
    </html>
    
    """
    from_email = settings.EMAIL_HOST_USER
    # recipient_list = ['amanpandeyudyalak@gmail.com']
    recipient_list = ['chochaprasad@gmail.com']
    msg = EmailMultiAlternatives(subject, "", from_email, recipient_list)
    msg.attach_alternative(message, "text/html")
    msg.send()
    