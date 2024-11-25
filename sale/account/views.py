from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .froms import LoginForm, RegisterForm
from django.core.mail import send_mail

# def login_request(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'account/login.html',{
#                 "error": "username or password is false"
#             })
#     return render(request, 'account/login.html')



def login_request(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Kullanıcıyı doğrula
            user = authenticate(username=username, password=password)
            if user is not None:
                # Başarılı giriş
                login(request, user)
                return redirect('home')
            else:
                # Yanlış giriş; formu temizle (kullanıcı adı alanını boşalt)
                form = LoginForm()  # Formu tamamen sıfırlıyoruz
                return render(request, 'account/login.html', {
                    "form": form,
                    "error": "Kullanıcı adı veya şifre yanlış.",
                })
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {"form": form})



# def register_request(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         password = request.POST['password']
#         repassword = request.POST['repassword']

#         if password == repassword:
#             if User.objects.filter(username=username):
#                 return render(request, 'account/register.html',
#                         {
#                             "error": "bu adda username var",
#                             "username": username,
#                             "email": email,
#                             "first_name": first_name,
#                             "last_name": last_name
#                         })
#             else:
#                 if User.objects.filter(email=email):
#                     return render(request, 'account/register.html',
#                         {
#                             "error": "this email already exist",
#                             "username": username,
#                             "email": email,
#                             "first_name": first_name,
#                             "last_name": last_name
#                         })
#                 else:
#                     user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
#                     user.save()
#                     login(request,user)
#                     return redirect('home')
#         else:
#             return render(request, 'account/register.html',
#                         {
#                             "error": "password is not same",
#                             "username": username,
#                             "email": email,
#                             "first_name": first_name,
#                             "last_name": last_name
#                         })
#     return render(request, 'account/register.html')


def register_request(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = RegisterForm()  # Boş form nesnesi

    if request.method == "POST":
        form = RegisterForm(request.POST)  # POST verilerini forma geçir

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            repassword = form.cleaned_data['repassword']

            # Şifrelerin aynı olup olmadığını kontrol et
            if password == repassword:
                # Kullanıcı adının daha önce kullanılıp kullanılmadığını kontrol et
                if User.objects.filter(username=username).exists():
                    return render(request, 'account/register.html', {
                        "error": "Bu kullanıcı adı zaten mevcut.",
                        "form": form  # Form verilerini geri gönder
                    })
                # E-postanın daha önce kullanılıp kullanılmadığını kontrol et
                elif User.objects.filter(email=email).exists():
                    return render(request, 'account/register.html', {
                        "error": "Bu e-posta zaten mevcut.",
                        "form": form  # Form verilerini geri gönder
                    })
                else:
                    # Yeni kullanıcı oluştur
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        password=password
                    )
                    user.save()
                    # Kullanıcıyı giriş yap
                    login(request, user)
                    send_mail(
                         subject="Xosgelmissiniz!",
                         message="Thank you for registering.",
                         from_email='nadir0091991@gmail.com',  # Gönderen e-posta adresi
                         recipient_list=[email],  # Alıcılar bir liste içinde olmalı
                    )
                    return redirect('home')
            else:
                # Şifrelerin uyuşmadığı durumu yönet
                return render(request, 'account/register.html', {
                    "error": "Şifreler uyuşmuyor.",
                    "form": form  # Form verilerini geri gönder
                })
    else:
        form = RegisterForm()  # GET isteği için boş form

    return render(request, 'account/register.html', {"form": form})





def logout_request(request):
    logout(request)
    return redirect('home')