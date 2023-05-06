from django.shortcuts import render, redirect
from .models import Student, ClassRoom, SchoolDetails, Teacher, ContactDetails
from django.contrib import messages

# Create your views here.

def home(request):
    sclDetails = SchoolDetails.objects.first()
    contactDetails = ContactDetails.objects.first()
    context = {"scl": sclDetails, "contacts": contactDetails}
    return render(request, 'sclmain/home.html', context)

def students(request):
    if request.method == "POST":
        if request.POST["searchType"] == 'student':
            print(request.POST["searchType"])
            stu_index = request.POST["searchTerm"]
            print("..............................")
            #print("some err .........",Student.objects.get(std_index_no=stu_index).exists())
            try:
                stu = Student.objects.get(std_index_no=stu_index)
                print("Have..................")
            except Student.DoesNotExist:
                errcontext = {"who":"Student"}
                print("Not having...............................")
                messages.error(request, "Invalid search")
                return render(request, "sclmain/searchstudent.html")
                
                # return render(request, 'sclmain/error.html', errcontext)
            # if Student.objects.get(std_index_no=stu_index).count() > 0:
            #     stu = Student.objects.get(std_index_no=stu_index)
            #     print("Have..................")

            # else:
            #     errcontext = {"who": "Student"}
            #     print("Not having...............................")
            #     messages.info(request, "Invalid search")
            #     return render(request, 'sclmain/error.html', errcontext)
                
                
            # else:
                
            print(stu_index)
            context = {"student": stu}
            return render(request, 'sclmain/students.html', context)
            
        elif request.POST["searchType"] == 'classroom':
            class_name = request.POST["searchTerm"]

            try:
                clas_room = ClassRoom.objects.get(name=class_name)

                print("Have..................")
            except:
                errcontext = {"who": "Classroom"}

                print("Not having...............................")
                messages.error(request, "Invalid search")
                return render(request, "sclmain/searchstudent.html")

            students_in_class = clas_room.student_set.all()
            print(students_in_class)
            context = {"students":students_in_class}
            return render(request, 'sclmain/clsrsearch.html', context)
        else:
            return render(request, 'sclmain/error.html')
    return render(request, 'sclmain/searchstudent.html')

def contact(request):
    contactDetails = ContactDetails.objects.first()
    context = {"contacts": contactDetails}
    return render(request, "sclmain/contactus.html", context)

def teachers(request):
    teachers = Teacher.objects.all()
    context = {"teachers": teachers}

    return render(request, "sclmain/searchteacher.html", context)

# Todo marks Section

def displaymarks(request):
    if request.method == 'POST':
        stu_index = request.POST["searchTerm"]

        try:
            student = Student.objects.get(std_index_no=stu_index)
            print("Have..................")
        except:
            errcontext = {"who":"Student"}
            print("Not having...............................")
            messages.error(request, "Invalid search")
            return render(request, "sclmain/searchstudent.html")

        
        marks_set = student.marks_set.all()
        print(marks_set[0].marks)
        # marks_set = student.marks_set.all()
        context = {"marks": marks_set, "student":student}
        # for mark in marks_set:
        #     print(mark.subject)
        #     print(mark.marks)

        return render(request, 'sclmain/marksheet.html', context)
        
    return render(request, 'sclmain/searchmarks.html')