from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Course, Enrollment, Announcement, Lesson, Material
from .forms import ContactCourse, CommentForm
from .decorators import enrollment_required

def index(request):
	courses = Course.objects.all()
	template_name = 'index.html'
	context = {
		'courses': courses
	}
	return render(request, template_name, context)

def details(request, slug):
	course = get_object_or_404(Course, slug=slug)
	context = {}
	if request.method == 'POST':
		form = ContactCourse(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form.send_mail(course)
			form = ContactCourse()
					
	else:
		form = ContactCourse()	
	context['form'] = form
	context['course'] = course
	#context = {
	#	'course': course,
	#	'form': ContactCourse()
	#}
	template_name = 'details.html'
	return render(request, template_name, context)

@login_required
def enrollment(request, slug):
	course = get_object_or_404(Course, slug = slug)
	enrollment, created = Enrollment.objects.get_or_create(user=request.user,
		 course=course
	)
	if created:
		#enrollment.active()
		messages.success(request, 'Você foi inscrito no curso com sucesso')
	else:
		messages.info(request, 'Você já está inscrito no curso')
	return redirect('dashboard')

@login_required
def undo_enrollment(request, slug):
	course = get_object_or_404(Course, slug = slug)
	enrollment = get_object_or_404(
			Enrollment, user=request.user, course=course
	)
	if request.method == 'POST':
		enrollment.delete()
		messages.success(request, 'Inscrição cancelada com sucesso')
		return redirect('dashboard')
	template = 'undo_enrollment.html'
	context = {
		'enrollment': enrollment,
		'course': course
	}
	return render(request, template, context)

@login_required
@enrollment_required
def announcements(request, slug):
	course = request.course
	template = 'announcements.html'
	context = {
		'course': course,
		'announcements': course.announcements.all()
	}
	return render(request, template, context)

@login_required
@enrollment_required
def show_announcement(request, slug, pk):
    course = request.course
    announcement = get_object_or_404(course.announcements.all(), pk = pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.announcement = announcement
        comment.save()
        form = CommentForm()
        messages.success(request, 'Seu comentário foi enviado com sucesso')
    template = 'show_announcement.html'
    context = {
        'course': course,
        'announcement': announcement,
        'form': form,
    }
    return render(request, template, context)

@login_required
@enrollment_required
def lessons(request, slug):
	course = request.course
	template = 'lessons.html'
	lessons = course.release_lessons
	if  request.user.is_staff:
		lessons = course.lessons.all()
	context = {
		'course': course,
		'lessons': lessons
	}
	return render(request, template, context)

@login_required
@enrollment_required
def lesson(request, slug, pk):
	course = request.course
	lesson = get_object_or_404(Lesson, pk=pk, course=course)
	if not request.user.is_staff and not lesson.is_available():
		messages.error(request, 'Esta aula não está disponível')
		return redirect('lessons', slug=course.slug)
	template = 'lesson.html'
	context = {
		'course': course,
		'lesson': lesson
	}
	return render(request, template, context)

@login_required
@enrollment_required
def material(request, slug, pk):
	course = request.course
	material = get_object_or_404(material, pk=pk, lesson__course=course)
	lesson = mateiral.lesson
	if not request.user.is_staff and not lesson.is_available():
		messages.error(request, 'Este material não está disponível')
		return redirect('lesson', slug=course.slug, pk=lesson.pk)
	if material.is_embedded():
		return redirect(material.file.url)
	template = 'material.html'
	context = {
		'course': course,
		'lesson': lesson,
		'material': material
	}
	return render(request, template, context)