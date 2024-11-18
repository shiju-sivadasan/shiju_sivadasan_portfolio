from django.shortcuts import render,HttpResponse
from .models import ProjectDetails,BlogData,Education,Experience
from django.core.mail import send_mail
from django.conf import settings
import qrcode
from io import BytesIO
# Create your views here.
def index(request):
    return render(request,'index.html')
def education(request):
    education = Education.objects.all()
    return render(request,'education.html',{'education':education})
def skills(request):
    return render(request,'skills.html')
def project(request):
    p_data=ProjectDetails.objects.all()
    return render(request,'project.html',{'p_data':p_data})
def blog(request):
    b_data=BlogData.objects.all()
    return render(request,'blog.html',{'b_data':b_data})
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        subject = f"New Contact Form Submission from {name}"
        message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['shijusivadazz86@gmail.com']  # Replace with your recipient email

        send_mail(subject, message_body, from_email, recipient_list)
    return render(request,'contact.html')
def experience(request):
    experience = Experience.objects.all()
    return render(request,'experience.html',{'experience':experience})
def generate_qr_code(request):
    # Define the URL for which you want to generate the QR code
    url = request.build_absolute_uri('/')  # Builds the URL of your site

    # Generate the QR code
    qr = qrcode.make(url)

    # Save the QR code to an in-memory file
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    # Return the image as an HTTP response
    return HttpResponse(buffer, content_type="image/png")