# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('staff_dashboard', views.staff_dashboard, name='staff_dashboard' ),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:pk>/', views.update_product, name='update_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('add-rating/<int:product_id>/', views.add_rating, name='add_rating'),
    path('add-review/<int:product_id>/', views.add_review, name='add_review'),
    path('review_rate/<int:product_id>/', views.review_rate, name='review_rate'),
    path('add-testimonial/', views.add_testimonial, name='add_testimonial'),
    


    path("waitlist/join/", views.join_waitlist, name="join_waitlist"),
    path("waitlist/admin/", views.waitlist_admin, name="waitlist_admin"),
    path("waitlist/send-email/", views.send_bulk_email, name="send_bulk_email"),

    path('email-template/', views.email_template_list, name='email_template_list'),
    # path('email-template/edit/<int:template_id>/', views.email_template_edit, name='email_template_edit'),
    # path('send-email/<int:template_id>/', views.send_bulk_email, name='send_bulk_email'),

    # path("email-template/edit/<int:template_id>/", views.email_template_edit, name="email_template_edit"),
    path("email-template/delete/<int:template_id>/", views.delete_template, name="delete_template"),
    path("email-template/create/", views.email_template_create, name="email_template_create"),  # New template
    path("email-template/edit/<int:template_id>/", views.email_template_edit, name="email_template_edit"),  # Edit template
    path("waitlist/send-email/<int:template_id>/", views.send_bulk_email, name="send_bulk_email"),

]
