from rest_framework.generics import RetrieveAPIView, DestroyAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from course.models import Course, Lesson
from course.serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonDetailAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = Lesson


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = Lesson


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = Lesson


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = Lesson


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = Lesson
