from django.test import TestCase

from ..controllers import Capacity


class FacultyTest(TestCase):
    
    def test_capacity_with_35_teacher_to_student_ratio(self):
        pharmacy = Capacity(
            name="Pharmacy",
            students_count=100,
            teacher_to_student_ratio=35,
            local_fulltime_specialist_count=7,
            local_fulltime_supportive_count=5,
            foreign_fulltime_specialist_count=4,
            foreign_fulltime_supportive_count=3,
            parttime_specialist_count=8,
            parttime_supportive_count=4,
            master_count=17,
            locality_percentage=0.5,
        )

        self.assertEqual(pharmacy.required_local_count, 16)
        self.assertEqual(pharmacy.capacity, 1260)
        self.assertEqual(pharmacy.capacity_difference, 1160)
        self.assertEqual(pharmacy.allowed_specialist_parttime_count, 8)
        self.assertEqual(pharmacy.allowed_supportive_parttime_count, 4)
        self.assertEqual(pharmacy.allowed_masters_count, 11)

    def test_capacity_with_50_teacher_to_student_ratio(self):
        
        management = Capacity(
            name="Management",
            students_count=1_500,
            teacher_to_student_ratio=50,
            local_fulltime_specialist_count=7,
            local_fulltime_supportive_count=5,
            foreign_fulltime_specialist_count=4,
            foreign_fulltime_supportive_count=3,
            parttime_specialist_count=15,
            parttime_supportive_count=7,
            master_count=17,
            locality_percentage=0.5,
        )

        self.assertEqual(management.required_local_count, 19)
        self.assertEqual(management.capacity, 2100)
        self.assertEqual(management.capacity_difference, 600)
        self.assertEqual(management.allowed_specialist_parttime_count, 11)
        self.assertEqual(management.allowed_supportive_parttime_count, 7)
        self.assertEqual(management.allowed_masters_count, 11)

