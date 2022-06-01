from django.shortcuts import render, HttpResponse, redirect
from .models import Farmer
from .forms import FarmerForm, LoginFarmer
from django.contrib import messages
import sqlite3
from django.core.mail import send_mail
# Create your views here.
conn = sqlite3.connect(
    r'C:\Users\91950\OneDrive\Documents\projects\SoftwareEngProj\swe\db.sqlite3', check_same_thread=False)
cursor = conn.cursor()


def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse('this is home page')


def about(request):
    return render(request, 'about.html')


def certification(request):
    return render(request, 'certification.html')


def certifiedlist(request):
    all_farmers = Farmer.objects.all
    return render(request, 'certifiedlist.html', {'a_f': all_farmers, 'start': 1})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        print(message_email)
        message_phone = request.POST['phone']
        message = request.POST['message']
        # send an email
        send_mail(
            'Contact: {}'.format(message_name),  # subject
            message + '\n\n\n{}-{}'.format(message_email,
                                           message_phone),  # message
            message_email,  # from email
            ['odfrdummy@gmail.com'],    # to email
        )
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')


def login(request):
    
    if request.method == "POST":
        # form = LoginFarmer(request.GET or None)
        data_email = request.POST['email']
        data_password = request.POST['password']
        cursor.execute(
            f"""Select email,password from home_farmer where email='{data_email}' and password='{data_password}'""")
        row = cursor.fetchone()
        print(row)
        if row:
            print(row)
            messages.success(
                request, ('Your form has been submitted successfully'))
        else:
            messages.error(
                request, ('There is an error in your form,Please try again'))

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        form = FarmerForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'register.html', {'form': form})

    else:
        form = FarmerForm()
        return render(request, 'register.html', {'form': form})


def join(request):
    if request.method == "POST":
        form = FarmerForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            phno = request.POST['phno']
            messages.error(
                request, ('There is an error in your form,Please try again'))
            return render(request, 'join.html', {'fname': fname, 'lname': lname, 'email': email, 'phno': phno})

        messages.success(
            request, ('Your form has been submitted successfully'))
        return redirect('join')
    else:
        return render(request, 'join.html', {})


def certform1(request):
    if request.method == "POST":
        msg_mobile = request.POST['mobile']
        msg_name = request.POST['name']
        msg_state = request.POST['state']
        msg_district = request.POST['district']
        msg_block = request.POST['block']
        msg_town = request.POST['town']
        msg_age = request.POST['age']
        msg_gender = request.POST['gender']
        msg_qualification = request.POST['qualification']
        msg_land = request.POST['land']
        if 'sms' in request.POST:
            msg_sms = request.POST['sms']
        else:
            msg_sms = False
        message = f"Details of {msg_name}\n\nMobile: {msg_mobile}\nState: {msg_state}\nDistrict: {msg_district}\nBlock: {msg_block}"\
            + f"\nVillage/Town: {msg_town}\nAge: {msg_age}\nGender: {msg_gender}\nQualification: {msg_qualification}\nLand holding: {msg_land}\nsms: {msg_sms}"
        # send an email
        send_mail(
            'Farmer Registration Form - {} :'.format(msg_name),  # subject
            message,  # message
            'odfrdummy@gmail.com',  # from email
            ['odfrdummy@gmail.com'],    # to email
        )
        messages.success(
            request, ('Your form has been submitted successfully'))
        return redirect('certform1')

    return render(request, 'certform1.html')


def certform2(request):
    if request.method == "POST":
        msg_email = request.POST['email']
        msg_mobile = request.POST['mobile']
        msg_name = request.POST['name']
        msg_state = request.POST['state']
        msg_address = request.POST['address']
        msg_age = request.POST['age']
        msg_year = request.POST['year']
        msg_product = request.POST['product']
        msg_water = request.POST['water']
        msg_electricity = request.POST['electricity']
        msg_date = request.POST['start']
        message = f"Details of {msg_name}\n\nEmail: {msg_email}\nMobile: {msg_mobile}\nState: {msg_state}\nAddress: {msg_address}\nAge: {msg_age}"\
            + f"\nNo. of years : {msg_year}\nProduct: {msg_product}\nWater supply used: {msg_water}\nSanction Electricity Load or HP Used (0 if not used): {msg_electricity}\nIntended date of start: {msg_date}"
        # send an email
        send_mail(
            # subject
            'FSSAI Product quality assurance form - {} :'.format(msg_name),
            message,  # message
            'odfrdummy@gmail.com',  # from email
            ['odfrdummy@gmail.com'],    # to email
        )
        try:
            thank_you = f'Thank you for filling the FSSAI Product quality assurance form , please expect a visit from our organisation before {msg_date}'
            send_mail(
                'FSSAI Product quality assurance form filled',
                thank_you,
                'odfrdummy@gmail.com',
                [msg_email],
            )
            messages.success(
                request, ('Your form has been submitted successfully'))
            return redirect('certform2')
        except:
            messages.success(
                request, ('Your form has been submitted successfully'))
            return redirect('certform2')

    return render(request, 'certform2.html')


def certform3(request):
    if request.method == "POST":
        msg_email = request.POST['email']
        msg_mobile = request.POST['mobile']
        msg_name = request.POST['name']
        msg_state = request.POST['state']
        msg_address = request.POST['address']
        message = f"Details of {msg_name}\n\nEmail: {msg_email}\nMobile: {msg_mobile}\nState: {msg_state}\nAddress: {msg_address}"\
            # send an email
        send_mail(
            # subject
            'Farmer Practices form - {} :'.format(msg_name),
            message,  # message
            'odfrdummy@gmail.com',  # from email
            ['odfrdummy@gmail.com'],    # to email
        )
        try:
            thank_you = f'Thank you for filling the Farmer practices form , please expect a visit from our organisation before 30 days of registration'
            send_mail(
                'Farmer Practices form  form filled',
                thank_you,
                'odfrdummy@gmail.com',
                [msg_email],
            )
            messages.success(
                request, ('Your form has been submitted successfully'))
            return redirect('certform3')
        except:
            messages.success(
                request, ('Your form has been submitted successfully'))
            return redirect('certform3')

    return render(request, 'certform3.html')
