from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import WebTemplate, MobileTemplate


def get_dummy_web_templates():
    return [
        {'name':'BizPro — Corporate Website','category':'Business','description':'Clean, professional multi-page corporate site with services, team, and blog sections.','price':'2,499','emoji':'🏢','gradient':'linear-gradient(135deg,#0a2a20,#0d3d2b,#062016)','tags':['Next.js','Tailwind','SEO'],'is_featured':True},
        {'name':'ShopEase — E-Commerce Store','category':'E-Commerce','description':'Full-featured online store with cart, checkout, product filters, and WhatsApp order integration.','price':'3,999','emoji':'🛒','gradient':'linear-gradient(135deg,#0a1a35,#0d2558,#06102a)','tags':['React','Stripe','WooCommerce'],'is_featured':True},
        {'name':'FolioX — Creative Portfolio','category':'Portfolio','description':'Stunning dark-mode portfolio for designers, developers, and photographers with scroll animations.','price':'1,499','emoji':'🎨','gradient':'linear-gradient(135deg,#1a0a30,#2d1060,#0d0520)','tags':['HTML','GSAP','CSS3'],'is_featured':False},
        {'name':'TasteHub — Restaurant Site','category':'Restaurant','description':'Mouth-watering restaurant website with online menu, table booking, and UberEats integration.','price':'2,999','emoji':'🍽️','gradient':'linear-gradient(135deg,#2a0a0a,#4a1515,#1a0505)','tags':['Vue.js','Booking API','Maps'],'is_featured':False},
        {'name':'PropList — Real Estate','category':'Real Estate','description':'Property listing website with advanced search filters, map view, and WhatsApp inquiry button.','price':'3,499','emoji':'🏠','gradient':'linear-gradient(135deg,#0a2a28,#104040,#051a18)','tags':['React','Google Maps','Django'],'is_featured':True},
        {'name':'LaunchPad — SaaS Landing Page','category':'SaaS / Tech','description':'High-converting SaaS landing page with pricing tables, feature showcase, and demo request form.','price':'1,999','emoji':'🚀','gradient':'linear-gradient(135deg,#0d0a30,#1a1060,#080520)','tags':['Next.js','Framer Motion','Analytics'],'is_featured':False},
    ]


def get_dummy_mobile_templates():
    return [
        {'name':'QuickBite — Food Delivery App','category':'Food & Delivery','description':'Complete food delivery app with real-time tracking, Stripe payments, driver app, and restaurant admin panel.','platform':'iOS & Android','price':'8,999','emoji':'🍔','gradient':'linear-gradient(135deg,#2a1a00,#4a3000,#1a1000)','tech':'React Native + Firebase','is_featured':True},
        {'name':'ShopGo — E-Commerce App','category':'Shopping','description':'Full-featured shopping app with product catalog, wishlist, cart, push notifications, and order tracking.','platform':'iOS & Android','price':'7,499','emoji':'🛍️','gradient':'linear-gradient(135deg,#0a1a35,#152a50,#06102a)','tech':'Flutter + Supabase','is_featured':True},
        {'name':'FitTrack — Fitness & Workout','category':'Health & Fitness','description':'Workout tracker with exercise library, progress charts, calorie counter, and social challenges.','platform':'iOS & Android','price':'5,999','emoji':'💪','gradient':'linear-gradient(135deg,#0a2a20,#0d3d2b,#051a12)','tech':'React Native + HealthKit','is_featured':False},
        {'name':'PropFind — Real Estate App','category':'Real Estate','description':'Property browsing app with map search, saved listings, agent chat, and mortgage calculator.','platform':'iOS & Android','price':'6,999','emoji':'🏠','gradient':'linear-gradient(135deg,#1a0a30,#2d1060,#0d0520)','tech':'Flutter + Google Maps','is_featured':False},
        {'name':'EduLearn — Online Learning','category':'Education','description':'E-learning app with video courses, quizzes, certificates, progress tracking, and offline mode.','platform':'iOS & Android','price':'7,999','emoji':'📚','gradient':'linear-gradient(135deg,#2a0a10,#4a1525,#1a0508)','tech':'React Native + AWS','is_featured':True},
        {'name':'BookEasy — Appointment App','category':'Booking / Services','description':'Service booking app for salons, clinics, and home services with calendar, reminders, and payments.','platform':'iOS & Android','price':'5,499','emoji':'📅','gradient':'linear-gradient(135deg,#0a2a28,#104040,#051a18)','tech':'Flutter + Stripe','is_featured':False},
    ]


def home(request):
    web_templates    = get_dummy_web_templates()
    mobile_templates = get_dummy_mobile_templates()
    form             = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your query has been submitted. We\'ll reply within 2–4 hours.')
            return redirect('home')
        else:
            messages.error(request, 'Please fix the errors below and try again.')

    context = {
        'form': form,
        'web_templates': web_templates,
        'mobile_templates': mobile_templates,
        'featured_web': [t for t in web_templates if t['is_featured']][:3],
        'featured_mobile': [t for t in mobile_templates if t['is_featured']][:3],
    }
    return render(request, 'core/home.html', context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your query has been sent! We\'ll get back to you shortly.')
            return redirect('contact')
    return render(request, 'core/contact.html', {'form': form})


def web_templates_view(request):
    templates = get_dummy_web_templates()
    return render(request, 'core/web_templates.html', {'templates': templates})


def mobile_templates_view(request):
    templates = get_dummy_mobile_templates()
    return render(request, 'core/mobile_templates.html', {'templates': templates})
