from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from course.models import Course, Lesson, Payments, Subscription
from course.paginators import CoursePaginator
from course.permissions import IsModerator, IsCustomPermission, IsOwner
from course.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer, SubscriptionSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsCustomPermission]
    if Course.objects.all().count() > CoursePaginator.page_size:
        pagination_class = CoursePaginator


class LessonDetailAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    if Lesson.objects.all().count() > CoursePaginator.page_size:
        pagination_class = CoursePaginator


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator | IsOwner]


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = (OrderingFilter, SearchFilter,)
    ordering_fields = ['date_pay']
    search_fields = ["type_metod", "payment_method"]
    permission_classes = [IsAuthenticated]


class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

