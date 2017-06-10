from django.shortcuts import render
from django.http import HttpResponse
from organization import models
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def teachers(request):
    
	all_teachers = models.Teacher.objects.all()
	teacher_count = all_teachers.count()
	sort = request.GET.get('sort', '')
	
	if sort:
		all_teachers = all_teachers.order_by('-click_nums')
			
	try:
		page = request.GET.get('page', 1)
	except PageNotAnInteger:
		page = 1	
		
	p = Paginator(all_teachers, 2, request=request)
	
	teachers = p.page(page)
	
	teacher_rank = models.Teacher.objects.order_by('-fav_nums')
	return render(request, 'teachers-list.html', {
				'all_teachers':teachers,
				'teacher_count':teacher_count,
				'teacher_rank':teacher_rank,
				'sort':sort,
				})


def orgs(request):

	all_orgs = models.CourseOrg.objects.all()
	org_rank = models.CourseOrg.objects.order_by('click_nums')[0:3]
	
	city_id = request.GET.get('city', '')
	category = request.GET.get('ct', '')
	sort = request.GET.get('sort', '')
	
	if sort:
		if sort == 'students':
			all_orgs = all_orgs.order_by('-students')
		else:
			all_orgs = all_orgs.order_by('-course_nums')
		
	
	if city_id:
		all_orgs = all_orgs.filter(city_id=city_id)
		
	if category:
		all_orgs = all_orgs.filter(category=category)
		
	orgs_count = all_orgs.count()
	
	try:
		page = request.GET.get('page', 1)
	except PageNotAnInteger:
		page = 1

	p = Paginator(all_orgs, 2, request=request)

	orgs = p.page(page)

	all_cities = models.CityDict.objects.all()
	return render(request, 'orgs-list.html', {
				'all_orgs':orgs,
				'all_cities':all_cities,
				'orgs_count':orgs_count,
				'city_id':city_id,
				'category':category,
				'sort':sort,
				'org_rank':org_rank,
				})

def home(request, org_id):
	org = models.CourseOrg.objects.get(pk=org_id)
	return render(request, 'org-home.html', {'org':org})


