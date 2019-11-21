# from django.test import TestCase
# from teacher.models import Teacher
# from course.models import Course
# from student.models import Student
# import datetime

# class TeacherCourseStudentTestCase(TestCase):
#     """docstring for TeacherCourseStudentTestcase"""
#     def setUp(self):
#         self.teacher_a = Teacher.objects.create (
#             first_name= "James",
#             last_name= "Mwai",
#             place_of_residence= "Kilimani",
#             phone_number ="0723456786",
#             Email = "jamesmwai@gmail.com",
#             id_number= 3128956743,
#             profession = "Software Engineer",
#             registration_number = 2344,
#             date_joined = datetime.date.today()
#             )

#         self.teacher_b = Teacher.objects.create (
#             first_name= "Nyandia",
#             last_name= "Kamawe",
#             place_of_residence= "Kilimani",
#             phone_number ="0767896786",
#             Email = "nyandiakamawe@gmail.com",
#             id_number= 3178765743,
#             profession = "Graphic Designer",
#             registration_number = 2355,
#             date_joined = datetime.date.today()
#             )

#         self.python = Course.objects.create (
#             name= "Python", 
#             duration_in_months= 10,
#             Course_number= "1001",
#             description= "Django and Flask frameworks")

#         self.graphics = Course.objects.create (
#             name= "Graphics", 
#             duration_in_months= 10,
#             Course_number= "1002",
#             description= "Visualising ideas")

#         self.javascript = Course.objects.create (
#             name= "Javascript", 
#             duration_in_months= 10,
#             Course_number= "1003",
#             description= "Front-end frameworks")


#     def test_teacher_can_teach_many_courses(self):
#         self.assertEqual(self.teacher_a.courses.count(), 0)
#         self.student_a.courses.add(self.python)
#         # self.assertEqual(self.student_a.courses.count(),1)
#         # self.student_a.courses.add(self.javascript)
#         # self.assertEqual(self.student_a.courses.count(),2)
#         # self.student_a.courses.add(self.hardware)
#         # self.assertEqual(self.student_a.courses.count(),3)


