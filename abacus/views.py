from django.shortcuts import render, redirect
from accounts.models import Profile

from django.contrib import messages

# def driveRegistration(request):  # Added missing colon
#     if request.method == 'POST':
#         profile = Profile.objects.get(user=request.user)
#         profile.drive = True
#         profile.save()
#         messages.success(request, 'You have been registered as a driver')
#         return redirect('dashboard')
#     return render(request, 'accounts/drive_registration.html')
