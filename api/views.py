from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .Page import MyPageNumberPagination#,MyPageNumberPagination1,Mypagelayout


class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class = MyPageNumberPagination
    #authentication_classes = [SessionAuthentication]
    
