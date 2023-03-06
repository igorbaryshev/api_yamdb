from django.urls import include, path


urlpatterns = [
    path('', include('api.reviews.urls')),
    path('v1/', include('users.urls', namespace='v1')),
]
