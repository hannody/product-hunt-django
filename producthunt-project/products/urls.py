from django.urls import path
from . import views

urlpatterns = [
	path('create', views.ShowPages.show_create_product, name='create'),
	path('<int:product_id>', views.ShowPages.show_product_details, name='details'),
	path('<int:product_id>/upvoate', views.ShowPages.upvote, name='upvote'),
]