import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator
from .forms import EmployeeForm
from .models import Employee

logger = logging.getLogger(__name__)

@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        email = request.POST.get('email').strip().lower()
        password = request.POST.get('password')
        try:
            user_obj = User.objects.get(email__iexact=email)
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'auth/login.html', {'error': 'Invalid email or password'})
        except User.DoesNotExist:
            return render(request, 'auth/login.html', {'error': 'Email not found'})
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    logger.debug("Home page accessed.")
    return render(request, 'dashboard.html')

@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp = form.save(commit=False)
            emp.skills = ",".join(form.cleaned_data.get('skills', []))
            emp.save()
            return redirect('employee_search')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form, 'form_mode': 'create'})

@login_required
def employee_edit(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            emp = form.save(commit=False)
            emp.skills = ",".join(form.cleaned_data.get('skills', []))
            emp.save()
            return redirect('employee_search')
    else:
        form = EmployeeForm(instance=emp, initial={'city': emp.city, 'country': emp.country})
    return render(request, 'employee_form.html', {'form': form, 'form_mode': 'edit'})

@login_required
def employee_search(request):
    query_name = request.GET.get('name', '')
    query_mobile = request.GET.get('mobile', '')
    employees = Employee.objects.all()
    if query_name:
        employees = employees.filter(first_name__icontains=query_name)
        logger.debug(f"Filtered employees by name: {query_name}")
    if query_mobile:
        employees = employees.filter(mobile_number__icontains=query_mobile)
        logger.debug(f"Filtered employees by mobile: {query_mobile}")
    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    logger.info(f"Search returned {employees.count()} employees.")
    return render(request, 'employee_search.html', {
        'employees': page_obj,
        'query_name': query_name,
        'query_mobile': query_mobile,
        'page_obj': page_obj,
    })

@login_required
def employee_delete(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        emp.delete()
        return redirect('employee_search')
    return render(request, 'employee_confirm_delete.html', {'employee': emp})

@login_required
def load_cities(request):
    country_id = request.GET.get('country')
    city_choices = {
        'India': [('Chennai', 'Chennai'), ('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Bangalore', 'Bangalore')],
        'USA': [('New York', 'New York'), ('Chicago', 'Chicago'), ('Los Angeles', 'Los Angeles')],
        'UK': [('London', 'London'), ('Manchester', 'Manchester'), ('Liverpool', 'Liverpool')],
    }
    cities = city_choices.get(country_id, [])
    data = [{'value': city[0], 'text': city[1]} for city in cities]
    return JsonResponse(data, safe=False)

@login_required
def multiple_tabs_view(request):
    return render(request, 'menus/multiple_tabs.html')

@login_required
def menu_view(request):
    return render(request, 'menus/menu.html')

@login_required
def tags_view(request):
    return render(request, 'menus/tags.html')

@login_required
def collapsible_view(request):
    return render(request, 'menus/collapsible_content.html')

@login_required
@csrf_exempt
def multi_features_view(request):
    image_list = []
    if request.method == 'POST' and request.FILES.get('image'):
        file = request.FILES['image']
        name = request.POST.get('name') or file.name
        fs = FileSystemStorage()
        filename = fs.save(name, file)
        image_list.append({'url': fs.url(filename), 'name': filename})
    return render(request, 'menus/image.html', {'image_list': image_list})

@login_required
def slider_view(request):
    return render(request, 'menus/slider.html')

@login_required
def tooltip_view(request):
    return render(request, 'menus/tooltip.html')

@login_required
def popup_view(request):
    return render(request, 'menus/popup.html')

@login_required
def link_view(request):
    return render(request, 'menus/link.html')

@login_required
def css_view(request):
    return render(request, 'menus/css_properties.html')

@login_required
def iframe_display(request):
    return render(request, 'menus/iframe_display.html')
