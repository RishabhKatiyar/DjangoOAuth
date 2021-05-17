from .models import Assignment, Question, GradedAssignment
from .serializers import AssignmentSerializer, QuestionSerializer, GradedAssignmentSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from rest_framework.generics import ListAPIView, CreateAPIView


class AssignmentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    model = Assignment
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def create(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            assignment = serializer.create(request)
            if assignment:
                return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    model = Question
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class GradedAssignmentListView(ListAPIView):
    serializer_class = GradedAssignmentSerializer

    def get_queryset(self):
        print("in query set")
        queryset = GradedAssignment.objects.all()
        username = self.request.query_params.get('username', None)
        
        try:
            if username is None:
                username = self.request.data['username']
        except:
            username = None

        if username is not None:
            queryset = queryset.filter(student__username=username)
        
        return queryset


class GradedAssignmentCreateView(CreateAPIView):
    serializer_class = GradedAssignmentSerializer
    queryset = GradedAssignment.objects.all()

    def post(self, request):
        print(request.data)
        serializer = GradedAssignmentSerializer(data=request.data)
        serializer.is_valid()
        graded_assignment = serializer.create(request)
        if graded_assignment:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)