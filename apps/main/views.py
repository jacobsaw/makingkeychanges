from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .forms import ContactForm
from django.template import Context
from django.contrib import messages
from .models import Publication, Previous_Engagements
# Create your views here.

def index(request):
        return render(request, 'main/index.html')

def about(request):
        return render(request, 'main/about.html')

def services(request):
        return render(request, 'main/services.html')

def lori_testimonials(request):
        return render(request, 'main/lori_testimonials.html')

def marci_testimonials(request):
        return render(request, 'main/marci_testimonials.html')

def lori_publications(request):
        return render(request, 'main/lori_publications.html')

def marci_publications(request):
        return render(request, 'main/marci_publications.html')

def lori_engagements(request):
    return render(request, 'main/lori_engagements.html')

def marci_engagements(request):
    return render(request, 'main/marci_engagements.html')

def lori_publications(request):
    context = {
        'publications': Publication.objects.all().order_by('-date_order')
    }
    return render(request, 'main/lori_publications.html', context)

def marci_publications(request):
    context = {
        'publications': Publication.objects.all().order_by('-date_order')
    }
    return render(request, 'main/marci_publications.html', context)

def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            email_to=request.POST.get('email_to')
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            contact_phone = request.POST.get(
                'contact_phone'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('main/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_phone': contact_phone,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Making Key Changes" +'',
                [email_to],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.add_message(request, messages.SUCCESS, 'DUMMY TEXT')
            return redirect('contact')
        else:
        	print form.errors
        	return render(request, 'main/contact_us.html', {
        		'form': form,
    		})

    return render(request, 'main/contact_us.html', {
        'form': form_class,
    })

def online_resources(request):
    return render(request, 'main/online_resources.html')

def community_ensembles(request):
    return render(request, 'main/community_ensembles.html')

def composer_connections(request):
    return render(request, 'main/composer_connections.html')

def hcpss(request):
    return render(request, 'main/hcpss.html')

def instrument_repairs(request):
    return render(request, 'main/instrument_repairs.html')

def private_lessons(request):
    return render(request, 'main/private_lessons.html')

def recommended_equipment(request):
    return render(request, 'main/recommended_equipment.html')

def study_recordings(request):
    return render(request, 'main/study_recordings.html')

def summer_band_camps(request):
    return render(request, 'main/summer_band_camps.html')

# def contact(request):
# 	form_class = ContactForm

# 	# new logic!
# 	if request.method == 'POST':
# 		form = form_class(data=request.POST)

# 		if form.is_valid():
# 			contact_name = request.POST.get('contact_name', '')
#             contact_email = request.POST.get('contact_email', '')
#             form_content = request.POST.get('content', '')
#             # Email the profile with the 
#             # contact information
#             template = get_template('contact_template.txt')
#             context = Context({
#                 'contact_name': contact_name,
#                 'contact_email': contact_email,
#                 'form_content': form_content,
#             })
#             content = template.render(context)

#             email = EmailMessage(
#                 "New contact form submission",
#                 content,
#                 "Your website" +'',
#                 ['youremail@gmail.com'],
#                 headers = {'Reply-To': contact_email }
#             )
#             email.send()
#             return redirect('contact')
#     return render(request, 'main/contact.html', { 'form': form_class })

