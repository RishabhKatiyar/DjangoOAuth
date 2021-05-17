from rest_framework import serializers
from .models import Assignment, Question, Choice, GradedAssignment
from users.models import User


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, data):
        #return super().to_internal_value(data)
        return data


class QuestionSerializer(serializers.ModelSerializer):
    choices = StringSerializer(many=True)
    answer = StringSerializer(many=False)
    class Meta:
        model = Question
        fields = ('__all__')


# question: why self not used in get_questions or create
class AssignmentSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    teacher = StringSerializer(many=False)
    
    class Meta:
        model = Assignment
        fields = ('__all__')

    def get_questions(self, obj):
        questions = QuestionSerializer(obj.questions.all(), many=True).data
        return questions

    def create(self, request):
        data = request.data

        assignment = Assignment()
        teacher = User.objects.get(username=data['teacher'])
        assignment.teacher = teacher
        assignment.title = data['title']
        assignment.save()

        order = 1
        for q in data['questions']:
            newQ = Question()
            newQ.question = q['title']
            newQ.order = order
            newQ.save()

            for c in q['choices']:
                newC = Choice()
                newC.title = c
                newC.save()
                newQ.choices.add(newC)

            newQ.answer = Choice.objects.get(title=q['answer'])
            newQ.assignment = assignment
            newQ.save()
            order += 1
        return assignment


class GradedAssignmentSerializer(serializers.ModelSerializer):
    student = StringSerializer(many=False)
    
    class Meta:
        model = GradedAssignment
        fields = ('__all__')

    def create(self, request):
        data = request.data
        print(data)

        assignment = Assignment.objects.get(id=data['asntId'])
        student = User.objects.get(username=data['username'])

        graded_asnt = GradedAssignment()
        graded_asnt.assignment = assignment
        graded_asnt.student = student

        questions = [q for q in assignment.questions.all()]
        answers = [data['answers'][a] for a in data['answers']]

        answered_correct_count = 0
        for i in range(len(questions)):
            if questions[i].answer.title == answers[i]:
                answered_correct_count += 1
            i += 1

        grade = answered_correct_count / len(questions) * 100
        graded_asnt.grade = grade
        graded_asnt.save()
        return graded_asnt