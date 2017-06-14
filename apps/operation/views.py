from django.shortcuts import render
from operation.models import CourseComments, UserStore
from courses.models import Course, CourseResource

# Create your views here.


def comment(request, course_id):
	course = Course.objects.get(pk=course_id)
	all_comments = CourseComments.objects.filter(course_id=course_id)
	all_resources = CourseResource.objects.filter(course_id=course_id)
	return render(request, 'course-comment.html', {'course': course,'all_comments': all_comments, 'all_resources':all_resources})
	
	
def addstore(request):
	store_id = request.POST.get('fav_id', '')
	store_type = request.POST.get('fav_type', '')
	
	user_store = UserStore()
	user_store.user_id = request.user.id
	user_store.store_id = store_id
	user_store.store_type = store_type
	user_store.save()
	
	
    
    