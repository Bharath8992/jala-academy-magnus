from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Employee CRUD
    path('employee/create/', views.employee_create, name='employee_create'),
    path('employee/search/', views.employee_search, name='employee_search'),
    path('employee/edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('employee/delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

    # UI/UX Components
    path('more/tabs/', views.multiple_tabs_view, name='multiple_tabs'),
    path('more/menu/', views.menu_view, name='menu'),
    path('tags/', views.tags_view, name='tags'),
    path('more/collapsible/', views.collapsible_view, name='collapsible'),
    path('features/', views.multi_features_view, name='multi_features'),
    path('slider/', views.slider_view, name='slider'),
    path('tooltip/', views.tooltip_view, name='tooltip'),
    path('popup/', views.popup_view, name='popup'),
    path('link/', views.link_view, name='link'),
    path('css_properties/', views.css_view, name='css_properties'),
    path('iframes/', views.iframe_display, name='iframe_display'),
]

# Media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
