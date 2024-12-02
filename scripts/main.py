from application.models import Faculty, Specialization, Staff

def run():
    qs = Faculty.objects.all()
    for faculty in qs:
        faculty.save()
    
    qs = Specialization.objects.all()
    for specialization in qs:
        specialization.save()

    qs = Staff.objects.all()
    for staff in qs:
        staff.save()
