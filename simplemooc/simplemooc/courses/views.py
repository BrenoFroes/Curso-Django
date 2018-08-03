from django.shortcuts import render,get_object_or_404
from .models import Course
from .forms import ContactCourse
# Create your views here.
def index(request):
    courses = Course.objects.all()
    templateName='courses/index.html'
    context = {
        'courses': courses
    }
    return render(request,templateName, context)
def details(request):
    course = Course.objects.all()
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_email()
            form = ContactCourse()
    else :
        form = ContactCourse()

    template_name = 'courses/course.html'
    context['courses'] = course
    context['form'] = form
    return render(request, template_name, context)
