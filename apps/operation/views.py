from django.shortcuts import render
from operation import models as operation
from courses import models

# Create your views here.


def comment(request, course_id):
    course = models.Course.objects.get(pk=course_id)
    all_comments = operation.CourseComments.objects.filter(course_id=course_id)
    all_resources = models.CourseResource.objects.filter(course_id=course_id)
    return render(request, 'course-comment.html', {'course': course,'all_comments': all_comments, 'all_resources':all_resources})