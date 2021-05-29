from django.shortcuts import render
from .models import Seminar,Meeting
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def meet(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        sex = request.POST['sex']
        subject = 'Meeting with counsellor fixed'
        email_from = settings.EMAIL_HOST_USER
        data = Meeting.objects.all()
        count = Seminar.objects.all().count()
        if count < 100 :
            message = 'Hy '+name+',Hope you are doing well . We are pleased to invite you for the free seminar of '+data[0].topic+'which will be held in'+data[0].date+' via zoom . Please click this '+data[0].url+' on '+data[0].date+' at '+data[0].time+' to be a part of this seminar .Here is what you need to do if you do not know how to join in zoom meetings .1.Install zoom in your mobile or computer https://zoom.us 2. Then click the link that we have given you3. Then you will be getting an option of joining in the room where your counsellor will be waiting for youIf you face any problem feel free to message us at www.instagram.com/nepalitogether or www.facebook.com/nepalitogetherHave a great day .Thanks(Team ma kasai ko naam)SaathiTimro'
            add_member= Seminar(Name=name,email=email,age=age,sex=sex)
            add_member.save()
            send_mail(subject,message,email_from,[email], fail_silently=False)
            return render(request, "meetings/form.html")
        elif count < 200 :
            message = 'Hy '+name+',Hope you are doing well . We are pleased to invite you for the free seminar of '+data[1].topic+'which will be held in'+data[1].date+' via zoom . Please click this '+data[1].url+' on '+data[1].date+' at '+data[1].time+' to be a part of this seminar .Here is what you need to do if you do not know how to join in zoom meetings .1.Install zoom in your mobile or computer https://zoom.us 2. Then click the link that we have given you3. Then you will be getting an option of joining in the room where your counsellor will be waiting for youIf you face any problem feel free to message us at www.instagram.com/nepalitogether or www.facebook.com/nepalitogetherHave a great day .Thanks(Team ma kasai ko naam)SaathiTimro'
            email_from = settings.EMAIL_HOST_USER
            add_member= Seminar(Name=name,email=email,age=age,sex=sex)
            add_member.save()
            send_mail(subject,message,email_from,[email], fail_silently=False)
            return render(request, "meetings/form.html")
        else:
            message = "sorry full house"
            send_mail(subject,message,email_from,[email], fail_silently=False)
            return render(request, "meetings/form.html")

    return render(request, "meetings/form.html")
