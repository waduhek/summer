from django.shortcuts import render
from first.models import Mobile
from django.db.models import Q

def search_result(request):

	mobiles = None
	query = None
	if 'q' in request.GET:
		query = request.GET.get('q')
		mobiles = Mobile.objects.all().filter(Q(Model_Name__contains = query) | Q(Description__contains = query))
	return render(request, 'search/search.html' , {'query' : query , 'mobiles' : mobiles})


