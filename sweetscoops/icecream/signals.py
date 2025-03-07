from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.db.models.signals import post_save,post_delete
from sweetscoops.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.dispatch import receiver
from icecream.models import Icecream
from django.template.loader import render_to_string
import datetime

now = datetime.datetime.now()

@user_logged_in.connect
def login_signal(sender,request,user,**kwargs):
    print('*************************(login signals:start)*************************')
    print("sender:",sender)
    print("request:",request)
    print("user:",user)
    print("kwargs:",kwargs)

    send_mail(f"[{user} placed]",
              "Someone logged in!.....",
               EMAIL_HOST_USER,
            ["shankkarpal46@gmail.com","priyanka.vibhute@itvedant.com"],fail_silently=False)
    
    print("*************************(login signals:end)*************************")

@user_logged_out.connect
def login_signal(sender,request,user,**kwargs):    
    print('*************************(login signals:start)*************************')
    print("sender:",sender)
    print("request:",request)
    print("user:",user)
    print("kwargs:",kwargs)

    send_mail(f"[{user} placed]",
              f"Someone logged out!...,..datetime:{now}",
               EMAIL_HOST_USER,
            ["shankkarpal46@gmail.com","priyanka.vibhute@itvedant.com"],
            fail_silently=False)
    
    print("*************************(login signals:end)*************************")


@receiver(post_save,sender=Icecream)
def add_icecream_signal(sender,instance,created,**kwargs):
    now = datetime.datetime.now()
    if created: 
        send_mail(f"[new icecream added]",
                f"Product created.{now}",
                EMAIL_HOST_USER,
                ["shankkarpal46@gmail.com","priyanka.vibhute@itvedant.com"],
                html_message=render_to_string("email.html",{"product":instance}),
                fail_silently=False)
    else:
        send_mail(f"[icecream updated]",
                f"Product updated.{now},{instance.id},{instance.icecream_name},{instance.icecream_description},{instance.icecream_price},{instance.icecream_description}",
                EMAIL_HOST_USER,
                ["shankkarpal46@gmail.com","priyanka.vibhute@itvedant.com"],html_message=render_to_string("email.html",{"icecream":instance}),fail_silently=False)

    print("*************************************Icecream Add Signal**********************************")

    print("sender:",sender)
    print("instance:",instance)
    print("created:",created)
    print("**kwargs:",kwargs)

    print("*************************************Icecream Stop Signal**********************************")

@receiver(post_delete,sender = Icecream)
def delete_icecream_signal(sender,instance,**kwargs):
    now = datetime.datetime.now()
    send_mail(f"[icecream deleted]",
              f"Product deleted at {now}",
            EMAIL_HOST_USER,
            ["shankkarpal46@gmail.com","priyanka.vibhute@itvedant.com"],html_message = render_to_string("email.html",{"icecream":instance}),fail_silently = False)
    
    print("***********************************Icecream Delete Signal*********************************")
        
    print("sender:",sender)
    print("instance:",instance)
    print("**kwargs",kwargs)