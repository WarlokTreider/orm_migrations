from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students = Student.objects.prefetch_related('teachers').order_by(ordering)

    context = {
        'students': students
    }

    return render(request, template, context)


class StudentListView(ListView):
    model = Student
    template_name = 'school/student_list.html'

    def get_queryset(self):
        # Используем prefetch_related для оптимизации запросов к базе данных
        return Student.objects.prefetch_related('teachers')