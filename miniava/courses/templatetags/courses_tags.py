from django.template import Library

from miniava.courses.models import Enrollment

register = Library()

@register.inclusion_tag('templatetags/my_courses.html')
def my_courses(user):
	enrollments = Enrollment.objects.filter(user=user)
	context = {
		'enrollments': enrollments
	}
	return context

#outro jeito de fazer
@register.simple_tag
def load_my_courses(user):
	return Enrollment.objects.filter(user=user)