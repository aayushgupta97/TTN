from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.

def order(request):
	number_list = [num for num in range(1,1001)]
	paginator = Paginator(number_list, 10)
	page = request.GET.get('page')
	numbers = paginator.get_page(page)
	context = {
			"person_name": "Aayush",
			"order_list": ["item1", "item2", "item3"],
			"ordered_warranty" : True, 
			"numbers": numbers,
			"Capital_name": "AAYUSH"
		}
	return render(request, 'myapp/order.html', context)
