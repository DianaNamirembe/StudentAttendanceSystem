from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def student_create(request):
    if request.method == "POST":
       
        name_from_html = request.POST.get('student_name')
        id_from_html = request.POST.get('sid')
       
        is_present_from_html = 'present' in request.POST 
        date_from_html = request.POST.get('attendance_date')

        
        Student.objects.create(
            name=name_from_html,
            student_id=id_from_html,
            is_present=is_present_from_html,
            date=date_from_html
        )

        
        return redirect('student_list')

    return render(request, 'attendance/student_form.html')

    
def student_list(request):
    all_students = Student.objects.all()
    return render(request, 'attendance/student_list.html', {'students': all_students})

# 2. READ (Detail View)
def student_detail(request, pk):
    
    single_student = Student.objects.get(id=pk)
    return render(request, 'attendance/student_detail.html', {'student': single_student})

# 3. UPDATE (Edit Record)
def student_update(request, pk):
    student = Student.objects.get(id=pk)
    
    if request.method == "POST":
        # Grabbing new data from the HTML form
        student.name = request.POST.get('student_name')
        student.student_id = request.POST.get('sid')
        student.is_present = 'present' in request.POST
        student.date = request.POST.get('attendance_date')
        student.save() # Saves the changes to the existing student
        return redirect('student_list')

    # This sends the existing student data to the form so it's "pre-filled"
    return render(request, 'attendance/student_form.html', {'student': student})

# 4. DELETE (Remove Record)
def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'attendance/student_confirm_delete.html', {'student': student})
