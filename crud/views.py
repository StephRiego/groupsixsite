from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Genders, Users 
from django.contrib.auth.hashers import make_password

# View to list all genders
def gender_list(request):
    try:
        genders = Genders.objects.all()
        context = {
            'genders': genders
        }
        return render(request, 'gender/GendersList.html', context)
    except Exception as e:
        return HttpResponse(f'Error occurred while loading genders: {e}')


# View to add a new gender
def add_gender(request):
    try:
        if request.method == 'POST':
            gender = request.POST.get('gender')

            if gender:  # Optional: Basic validation
                Genders.objects.create(gender=gender)
                messages.success(request, 'Gender added successfully!')
                return redirect('/gender/list')
            else:
                messages.error(request, 'Gender field cannot be empty.')

        return render(request, 'gender/AddGender.html')

    except Exception as e:
        return HttpResponse(f'Error occurred while adding gender: {e}')
    

def edit_gender(request, genderId):
    try:
        if request.method == 'POST':
            genderObj = Genders.objects.get(pk=genderId)

            gender = request.POST.get('gender')

            genderObj.gender = gender
            genderObj.save()

            messages.success(request, 'Gender updated successfully!')

            data = {
                'gender': genderObj
            }

            return render(request, 'gender/EditGender.html', data)
        else:
            genderObj = Genders.objects.get(pk=genderId)

            data = {
                'gender': genderObj
            }

            return render(request, 'gender/EditGender.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during edit gender: {e}')


def delete_gender(request, genderId):
    try:
      if request.method == 'POST':
        genderObj = Genders.objects.get(pk=genderId)
        genderObj.delete()

        messages.success(request, 'Gender deleted successfully!')
        return redirect('/gender/list')
      else:
       genderObj = Genders.objects.get(pk=genderId)

      data = {
        'gender': genderObj
      }
      return render(request, 'gender/DeleteGender.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during delete gender: {e}')
    
def user_list(request):
    try:
        userObj = Users.objects.select_related('gender')
        data = {
            'users': userObj
        }

        return render(request, 'user/UsersList.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during load users: {e}')
  
    
def add_user(request):
    try:
        if request.method == 'POST':
            fullName = request.POST.get('full_name')
            gender = request.POST.get('gender')
            birth_date = request.POST.get('birth_date')
            address = request.POST.get('address')  
            contactNumber = request.POST.get('contact_number')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirmPassword = request.POST.get('confirm_password')
            
            #if password != confirmPassword:

            Users.objects.create(
                full_name=fullName,
                gender=Genders.objects.get(pk=gender),
                birth_date=birth_date,
                address=address,
                contact_number=contactNumber,
                email=email,
                username=username,
                password=make_password(password)
            ).save()

            messages.success(request, 'User added successfully!')
            return redirect('/user/add')

        else:
            genderObj = Genders.objects.all()

            data = {
                'genders': genderObj
            }

            return render(request, 'user/AddUser.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during add user: {e}')


  