from django.urls import path
from .views import post_list_view, 

urlpatterns = [
    path('<int:id>', post_list_view, name = "blogs_list"),
    # path('<int:id>', post_category_list, name='job_details'),
    # path('addJob', add_job, name='jobEditor'),
    # path('<int:id>/like', like_btn, name='like'),
    # # path('<int:id>/dislike', disLiker, name='dislike'),
]

app_name = 'blog'