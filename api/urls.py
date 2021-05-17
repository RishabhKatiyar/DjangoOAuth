from api.models import GradedAssignment
from rest_framework.routers import DefaultRouter
from .views import AssignmentViewSet, QuestionViewSet, GradedAssignmentListView, GradedAssignmentCreateView
from django.urls import path


router = DefaultRouter()
router.register(r'assignment', AssignmentViewSet, basename='assignment')
# router.register(r'graded-assignment', AsignmentViewSet, basename='graded_assignment')
# router.register(r'choice', AsignmentViewSet, basename='choice')
router.register(r'question', QuestionViewSet, basename='question')
urlpatterns = router.urls

urlpattern = [
    path('graded-assignment/', GradedAssignmentListView.as_view()),
    path('graded-assignment/create/', GradedAssignmentCreateView.as_view()),
]

urlpatterns = urlpatterns + urlpattern