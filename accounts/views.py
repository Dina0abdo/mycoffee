from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile
from shops.models import Shop
import re
# Create your views here.


def signin(request):
    # if request.GET:
    #     messages.info(request, "test1")
    #     messages.success(request, "test3")
    #     messages.error(request, "test4")
    # if request.POST:
    #     password = request.POST['password']
    #     messages.info(request, "this is post" + password)
    #     messages.success(request, "test3")
    #     messages.error(request, "test4")
    if request.method == 'POST' and "btnlogin" in request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if 'rememberme' not in request.POST:
                request.session.set_expiry(0)
            auth.login(request, user)
            # messages.success(request, 'you are now logged in')
        else:
            messages.error(request, 'username or password invalid')
        return redirect('signin')
    else:
        return render(request, 'accounts/signin.html')


def signup(request):

    if request.method == 'POST' and 'btnsignup' in request.POST:

        # variables for fields
        fname = None
        lname = None
        address = None
        address2 = None
        city = None
        state = None
        zip_number = None
        email = None
        username = None
        password = None
        terms = None
        is_added = None

        # get values from the form
        # fname=request.POST['fnameS']
        if 'fname' in request.POST:
            fname = request.POST['fname']
        else:
            messages.error(request, 'Error in First Name')
        if 'lname' in request.POST:
            lname = request.POST['lname']
        else:
            messages.error(request, 'Error in Last Name')
        if 'address' in request.POST:
            address = request.POST['address']
        else:
            messages.error(request, 'Error in Address')
        if 'address2' in request.POST:
            address2 = request.POST['address2']
        else:
            messages.error(request, 'Error in Address2')
        if 'city' in request.POST:
            city = request.POST['city']
        else:
            messages.error(request, 'Error in City')
        if 'state' in request.POST:
            state = request.POST['state']
        else:
            messages.error(request, 'Error in State')
        if 'zip' in request.POST:
            zip_number = request.POST['zip']
        else:
            messages.error(request, 'Error in Zip')
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            messages.error(request, 'Error in Email')
        if 'username' in request.POST:
            username = request.POST['username']
        else:
            messages.error(request, 'Error in Username')
        if 'password' in request.POST:
            password = request.POST['password']
        else:
            messages.error(request, 'Error in Password')
        if 'terms' in request.POST:
            terms = request.POST['terms']
        # check var
        if fname and lname and address and address2 and city and state and zip_number and email and username and password:
            if terms == 'on':
                # check if User is taken
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username is taken')
                else:
                    # check is email is taken
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'Email is taken')
                    else:
                        patt = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                        if re.match(patt, email):
                            # add user
                            user = User.objects.create_user(
                                first_name=fname, last_name=lname, email=email, username=username, password=password)
                            user.save()
                            # add user profile
                            userprofile = UserProfile(
                                user=user, address=address, address2=address2, city=city, state=state, zip_number=zip_number)
                            userprofile.save()
                            # Success Message
                            # clear feilds after create account
                            fname = ' '
                            lname = ' '
                            address = ' '
                            address2 = ' '
                            city = ' '
                            state = ' '
                            zip_number = ' '
                            email = ' '
                            username = ' '
                            password = ' '
                            terms = None

                            messages.success(request, 'You account is created')
                            is_added = True

                        else:
                            messages.error(request, 'Email is invalid')
            else:
                messages.error(request, 'You most agree to the terms')
        else:
            messages.error(request, 'Check empty fields')
        return render(request, 'accounts/signup.html', {'fname': fname, 'lname': lname, 'address': address, 'address2': address2, 'city': city, 'state': state, 'zip': zip_number, 'email': email, 'username': username, 'password': password, 'is_added': is_added})
    else:
        return render(request, 'accounts/signup.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('index')


def profile(request):
    # if request.POST:
    #     lname = request.POST['lname']

    #     messages.info(request, "this is POST" + lname)
    # if request.GET:
    #     messages.info(request, "THIS IS GET")
    if request.method == 'POST' and "btnlogin" in request.POST:
        if request.user is not None and request.user.id != None:
            userprofile = UserProfile.objects.get(user=request.user)
            if request.POST['fname'] and request.POST['lname'] and request.POST['address'] and request.POST['address2'] and request.POST['city'] and request.POST['state'] and request.POST['zip'] and request.POST['email'] and request.POST['username'] and request.POST['password']:
                request.user.first_name = request.POST['fname']
                request.user.last_name = request.POST['lname']
                userprofile.address = request.POST['address']
                userprofile.address2 = request.POST['address2']
                userprofile.city = request.POST['city']
                userprofile.state = request.POST['state']
                userprofile.zip_number = request.POST['zip']
                # request.user.email = request.POST['email']
                # request.user.username = request.POST['username']
                if not request.POST['password'].startswith('pbkdf2_sha256$'):
                    request.user.set_password(request.POST['password'])
                # request.user.password = request.POST['password']
                request.user.save()
                userprofile.save()
                auth.login(request, request.user)
                messages.success(request, 'your data hs been save')

            else:
                messages.error(request, 'check your values')
        return redirect('profile')
    else:
        # if request.user.id == None:
        #     return redirect('index')
        if request.user is not None:
            context = None
            if not request.user.is_anonymous:
                userprofile = UserProfile.objects.get(
                    user=request.user)
                context = {
                    'fname': request.user.first_name,
                    'lname': request.user.last_name,
                    'address': userprofile.address,
                    'address2': userprofile.address2,
                    'city': userprofile.city,
                    'state': userprofile.state,
                    'zip': userprofile.zip_number,
                    'email': request.user.email,
                    'username': request.user.username,
                    'password': request.user.password}
            return render(request, 'accounts/profile.html', context)
        else:
            return redirect('profile')


def shop_fav(request, pro_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        pro_fav = Shop.objects.get(pk=pro_id)
        if UserProfile.objects.filter(user=request.user, shop_fav=pro_fav).exists():
            messages.info(request, 'you Aleardy add to fav')
        else:
            userprofile = UserProfile.objects.get(user=request.user)
            userprofile.shop_fav.add(pro_fav)
            messages.success(request, 'your product has been added to fav')
        return redirect("/shops/"+str(pro_id))
    else:
        messages.error(request, 'you must be logged in')
    return redirect("/shops/"+str(pro_id))


def show_shop_fav(request):
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        user_info = UserProfile.objects.get(user=request.user)
        pro = user_info.shop_fav.all()
        context = {'shops': pro}

    return render(request, 'shops/shops.html', context)
