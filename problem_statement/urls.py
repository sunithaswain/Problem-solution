# from django.conf.urls.defaults import *
from django.conf.urls import url, include
from . import views
from rest_framework import routers
from views import ContestViewSet,ProblemViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'contests', ContestViewSet)
router.register(r'problem-solution', ProblemViewSet)
# router.register(r'all', AllUsersViewSet)
# router.register(r'test', Testviewset)


# urlpatterns = [
#     url(r'^docs/', include('rest_framework_swagger.urls')),
# ]
# urlpatterns += router.urls
