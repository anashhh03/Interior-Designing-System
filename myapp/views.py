
from django.shortcuts import render, redirect
from django.contrib import messages

from django.http import HttpResponseRedirect

from .models import login_table
from .models import detail_table
from .models import STATE_TABLE
from .models import CITY_TABLE
from .models import designs
from .models import bidding
from .models import FEEDBACK_TABLE
from .models import complain_TABLE

def home(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    context = {
      'Desgn': Desgn,
      'profiledata': profiledata,
    }
    return render(request, 'index.html', context)

  except:
    pass
  return render(request, 'index.html')


def about(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    context = {
      'Desgn': Desgn,
      'profiledata': profiledata,
    }
    return render(request, 'about.html', context)

  except:
    pass
  return render(request, 'about.html')

def complain(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    context = {
      'Desgn': Desgn,
      'profiledata': profiledata,
    }
    return render(request, 'complain.html', context)

  except:
    pass
  return render(request, 'complain.html')

def feedback(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    context = {
      'Desgn': Desgn,
      'profiledata': profiledata,
    }
    return render(request, 'contact.html', context)

  except:
    pass
  return render(request, 'contact.html')

def basic(request):
  return render(request, 'basic.html')

def login(request):
  return render(request, 'login.html')

def signup(request):
  statedetail = STATE_TABLE.objects.all()
  citydetail = CITY_TABLE.objects.all()

  context = {
    'statedetail': statedetail,
    'citydetail': citydetail,
  }

  return render(request, 'signup.html', context)

def viewdata(request):
  if request.method == 'POST':
    email = request.POST.get("email")
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    password = request.POST.get("password")
    role = request.POST.get("usertype")
    cityid = request.POST.get("cityid")
    stateid = request.POST.get("stateid")

    logindata = login_table(email=email, name=name, phone_no=phone, password=password,
                            role=role, city_id=CITY_TABLE(id=cityid), state_id=STATE_TABLE(id=stateid))
    logindata.save()


    messages.success(request, 'Data Inserted Successfully. you can login now')
    return redirect(home)
  else:
    messages.error(request, 'error occured')

  return redirect(home)

def checklogin(request):
  if request.method == 'POST':
    username = request.POST['email']
    password = request.POST['password']

    try:
      user = login_table.objects.get(email=username, password=password)


    except login_table.DoesNotExist:
      user = None

    if user is not None:
      request.session['log_user'] = user.email
      request.session['log_id'] = user.id
      request.session.save()
      print("successfully logged in")
      messages.success(request, 'Successfully Logged In')
      return redirect(home)
    else:
      print("not logged in")
      messages.error(request, 'Invalid USER ID')
  return redirect(login)


def logout(request):
  try:
    del request.session['log_user']
    del request.session['log_id']
  except:
    pass
  return redirect(home)

def completeprofile(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)

    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    context = {
      'Desgn': Desgn,
      'profiledata': profiledata,
    }
    return render(request, 'completeprofile.html', context)

  except:
    pass
  return render(request, 'completeprofile.html')


def completeprofilesubmit(request):
  uid = request.session['log_id']
  if request.method == 'POST':
    desc = request.POST.get("desc")
    experience = request.POST.get("experience")


    userdata = detail_table(login_id=login_table(id=uid), i_desc=desc, i_experience=experience)
    userdata.save()
    messages.success(request, 'Data Inserted Successfully.')
    return redirect(home)
  else:
    messages.error(request, 'error occured')

def designerprofile(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    context = {
      'Desgn': Desgn,
      'user': user,
      'profiledata': profiledata,
    }
    return render(request, 'designerprofile.html', context)

  except:
    pass
  return render(request, 'designerprofile.html')


def editprofiledesgn(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    statedetail = STATE_TABLE.objects.all()
    citydetail = CITY_TABLE.objects.all()

    context = {
      'Desgn': Desgn,
      'statedetail': statedetail,
      'citydetail': citydetail,
      'user': user,
      'profiledata': profiledata,
    }
    return render(request, 'editprofiledesgn.html', context)

  except:
    pass
  return render(request, 'editprofiledesgn.html')

def editprofiledesgnsubmit(request):
  uid = request.session['log_id']
  if request.method == 'POST':
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    cityid = request.POST.get("cityid")
    stateid = request.POST.get("stateid")
    experience = request.POST.get("experience")
    desc = request.POST.get("desc")


    cuser = detail_table.objects.get(login_id=uid)

    cuser.i_desc = desc
    cuser.i_experience = experience


    cuser.save(update_fields=['i_desc', 'i_experience'])

    cuser1 = login_table.objects.get(id=uid)

    updcity = CITY_TABLE.objects.get(id=cityid)
    updstate = STATE_TABLE.objects.get(id=stateid)

    cuser1.name = name
    cuser1.email = email
    cuser1.phone_no = phone
    cuser1.city_id = updcity
    cuser1.state_id = updstate

    cuser1.save(update_fields=['name', 'email','phone_no','city_id','state_id'])

    messages.success(request, 'Data Updated Successfully. ')

    return redirect(editprofiledesgn)

  else:
    messages.error(request, 'error occured')

  return redirect(editprofiledesgn)


def changepw(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None



    context = {
      'Desgn': Desgn,
      'user': user,
      'profiledata': profiledata,
    }
    return render(request, 'changepw.html', context)

  except:
    pass
  return render(request, 'changepw.html')

def changepwsubmit(request):
  uid = request.session['log_id']
  if request.method == 'POST':
    cpw = request.POST.get("oldpassword")
    npw = request.POST.get("password")

    cusercheck = login_table.objects.get(id=uid)

    checkpw = cusercheck.password
    print(checkpw)
    print(cpw)

    if checkpw == cpw:
      cuser1 = login_table.objects.get(id=uid)
      cuser1.password = npw
      cuser1.save(update_fields=['password'])
      messages.success(request, 'Password Changed Successfully. ')
    else:
      messages.error(request, 'Current Password is wrong.')
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  return redirect(home)


def profile(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    context = {
      'Desgn': Desgn,
      'user': user,
      'profiledata': profiledata,
    }
    return render(request, 'profile.html', context)

  except:
    pass
  return render(request, 'profile.html')


def editprofile(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    statedetail = STATE_TABLE.objects.all()
    citydetail = CITY_TABLE.objects.all()

    context = {
      'Desgn': Desgn,
      'statedetail': statedetail,
      'citydetail': citydetail,
      'user': user,
      'profiledata': profiledata,
    }
    return render(request, 'editprofile.html', context)

  except:
    pass
  return render(request, 'editprofile.html')


def editprofilesubmit(request):
  uid = request.session['log_id']
  if request.method == 'POST':
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    cityid = request.POST.get("cityid")
    stateid = request.POST.get("stateid")


    cuser1 = login_table.objects.get(id=uid)

    updcity = CITY_TABLE.objects.get(id=cityid)
    updstate = STATE_TABLE.objects.get(id=stateid)

    cuser1.name = name
    cuser1.email = email
    cuser1.phone_no = phone
    cuser1.city_id = updcity
    cuser1.state_id = updstate

    cuser1.save(update_fields=['name', 'email','phone_no','city_id','state_id'])

    messages.success(request, 'Data Updated Successfully. ')

    return redirect(editprofile)

  else:
    messages.error(request, 'error occured')

  return redirect(editprofile)


def uploaddesign(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    context = {
      'Desgn': Desgn,
      'user': user,
      'profiledata': profiledata,
    }
    return render(request, 'uploaddesign.html', context)

  except:
    pass
  return render(request, 'uploaddesign.html')


def designsubmit(request):
  uid = request.session['log_id']
  if request.method == 'POST':
    desc = request.POST.get("desc")
    category = request.POST.get("category")
    designfile = request.FILES['designimg']


    userdata = designs(login_id=login_table(id=uid), category=category, Design_Description=desc, dimage=designfile)
    userdata.save()
    messages.success(request, 'Data Inserted Successfully.')
    return redirect(home)
  else:
    messages.error(request, 'error occured')

def viewdesigns(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    designdata = designs.objects.all()

    context = {
      'Desgn': Desgn,
      'user': user,
      'profiledata': profiledata,
      'designdata': designdata,
    }
    return render(request, 'viewdesigns.html', context)

  except:
    designdata = designs.objects.all()

    context = {

      'designdata': designdata,
    }
  return render(request, 'viewdesigns.html', context)


def viewdesignbids(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None


    mylogindata = designs.objects.filter(login_id=login_table(id=uid)).values('id')

    try:
      recbids = bidding.objects.filter(d_id__in=mylogindata)
    except bidding.DoesNotExist:
      recbids = None

    context = {
      'Desgn': Desgn,
      'user': user,
      'profiledata': profiledata,
      'recbids': recbids,
    }
    return render(request, 'viewdesignbids.html', context)

  except:
    pass
  return render(request, 'viewdesignbids.html')

def designsingle(request, dsid):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    designdata = designs.objects.get(id=dsid)

    context = {
      'Desgn': Desgn,
      'user': user,
      'profiledata': profiledata,
      'designdata': designdata,
    }
    return render(request, 'designsingle.html', context)

  except:
    designdata = designs.objects.get(id=dsid)

    context = {

      'designdata': designdata,
    }
  return render(request, 'designsingle.html', context)

def makeabid(request):
  uid = request.session['log_id']
  if request.method == 'POST':
    desc = request.POST.get("desc")
    designid = request.POST.get("designid")
    budget = request.POST.get("budget")



    biddata = bidding(login_id=login_table(id=uid), d_id=designs(id=designid), approx_budget=budget, b_status='0')
    biddata.save()
    messages.success(request, 'Bid made Successfully.')
    return redirect(home)
  else:
    messages.error(request, 'error occured')

def designerprofiledata(request, dpdid):
  try:

    user = login_table.objects.get(id=dpdid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=user)
    except detail_table.DoesNotExist:
      profiledata = None

    context = {
      'Desgn': Desgn,
      'user': user,
      'profiledata': profiledata,
    }
    return render(request, 'designerprofiledata.html', context)

  except:
    pass
  return render(request, 'designerprofiledata.html')

def approvebid(request, abid):
  uid = request.session['log_id']

  upbidstat = bidding.objects.get(id=abid)


  upbidstat.b_status = "1"
  upbidstat.p_status = "pending"
  upbidstat.show_interest_button = False

  upbidstat.save(update_fields=['b_status','p_status', 'show_interest_button'])

  messages.success(request, 'Bid Approved. ')


  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def rejectbid(request, rbid):
  uid = request.session['log_id']

  upbidstat = bidding.objects.get(id=rbid)

  upbidstat.b_status = "2"
  upbidstat.rejected = True

  upbidstat.save(update_fields=['b_status', 'rejected'])

  messages.error(request, 'Bid Rejected. ')

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def mybids(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    mybidsdata = bidding.objects.filter(login_id=uid)

    context = {
      'Desgn': Desgn,
      'user': user,
      'profiledata': profiledata,
      'mybidsdata': mybidsdata,
    }
    return render(request, 'mybids.html', context)

  except:
    pass
  return render(request, 'mybids.html')

def deletebid(request, dbid):
  uid = request.session['log_id']

  bidding.objects.get(id=dbid).delete()
  messages.error(request, 'Bid Deleted')

  return redirect(mybids)

def mydesigns(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    designdata = designs.objects.filter(login_id=uid)

    context = {
      'Desgn': Desgn,
      'user': user,
      'profiledata': profiledata,
      'designdata': designdata,
    }
    return render(request, 'mydesigns.html', context)

  except:
    pass
  return render(request, 'mydesigns.html')

def deletedesign(request, ddid):
  uid = request.session['log_id']

  designs.objects.get(id=ddid).delete()
  messages.error(request, 'Design Deleted')

  return redirect(mydesigns)

def approveddesign(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None



    mylogindata = designs.objects.filter(login_id=login_table(id=uid)).values('id')

    try:
      apprbids = bidding.objects.filter(d_id__in=mylogindata, b_status="1")
    except bidding.DoesNotExist:
      apprbids = None



    context = {
      'Desgn': Desgn,
      'user': user,
      'profiledata': profiledata,
      'apprbids': apprbids,
    }
    return render(request, 'approveddesign.html', context)

  except:
    pass
  return render(request, 'approveddesign.html')


def designers(request):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    designersdata = login_table.objects.filter(role="Designer").values('id')

    try:
      desprofiles = detail_table.objects.filter(login_id__in=designersdata)
    except detail_table.DoesNotExist:
      desprofiles = None



    context = {
      'Desgn': Desgn,
      'user': user,
      'profiledata': profiledata,
      'desprofiles': desprofiles,
    }
    return render(request, 'designers.html', context)

  except:
    designersdata = login_table.objects.filter(role="Designer").values('id')

    try:
      desprofiles = detail_table.objects.filter(login_id__in=designersdata)
    except detail_table.DoesNotExist:
      desprofiles = None

    context = {

        'desprofiles': desprofiles,
      }
  return render(request, 'designers.html', context)


def feedbacksubmit(request):
  uid = request.session['log_id']
  if request.method == 'POST':
    name = request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    message = request.POST.get("message")


    userdata = FEEDBACK_TABLE(name=name, email=email, subject=subject, COMMENT=message)
    userdata.save()
    messages.success(request, 'Response recorded Successfully.')
    return redirect(feedback)
  else:
    messages.error(request, 'error occured')

def complainsubmit(request):
  uid = request.session['log_id']
  if request.method == 'POST':
    type = request.POST.get("type")
    desc = request.POST.get("desc")

    mydetail = detail_table.objects.get(login_id=uid)

    userdata = complain_TABLE(login_id=login_table(id=uid), i_ID=mydetail, Type=type, Description=desc)
    userdata.save()
    messages.success(request, 'Response recorded Successfully.')
    return redirect(complain)
  else:
    messages.error(request, 'error occured')


def makepayment(request, mpid):
  try:
    uid = request.session['log_id']
    user = login_table.objects.get(id=uid)
    Desgn = False
    if user.role == "Designer":
      Desgn = True
      print(Desgn)
      print(user.role)

    try:
      profiledata = detail_table.objects.get(login_id=uid)
    except detail_table.DoesNotExist:
      profiledata = None

    selbd = bidding.objects.get(id=mpid)



    context = {
      'Desgn': Desgn,
      'user': user,
      'profiledata': profiledata,
      'selbd': selbd,
    }
    return render(request, 'makepayment.html', context)

  except:
    pass
  return render(request, 'makepayment.html')

def paymentsubmit(request):

  if request.method == 'POST':
    bidid = request.POST.get("bidid")

    upbidstat = bidding.objects.get(id=bidid)

    upbidstat.p_status = "done"
    upbidstat.payment_done = True

    upbidstat.save(update_fields=['p_status', 'payment_done'])

    return redirect(viewdesignbids)

