from django.tests import TestCase
from student.models import Student
from course.models import Course
from teacher.models import Teacher
import datetime



class StudentCourseTestCase(TestCase):
	"""docstring for StudentCourseTestCase"""
	def setUp(self):
		self.student_a = Student (
			first_name="Tiffany",
			last_name="Jeruto",
			date_of_birth=datetime.date(2000,6,24),
			registration_number="254016", 
			Email="tiffanylalampaa@gmail.com", 
			phone_number="0789647745", 
			place_of_residence="Rongai", 
			guardian_phone="0789567484", 
			id_number=345378625, 
			date_joined=datetime.date.today(),)

		self.student_b = Student (
			first_name="Clay",
			last_name="Jensen",
			date_of_birth=datetime.date(1999,7,25),
			registration_number="254017", 
			Email="jensenclay@gmail.com", 
			phone_number="0789765945", 
			place_of_residence="Roysambu", 
			guardian_phone="0780007684", 
			id_number=3453734789, 
			date_joined=datetime.date.today(),)

		self.python = Course (
			name= "Python", 
    		duration_in_months= 10,
    		Course_number= "1001",
		    description= "Django and Flask frameworks")

		self.javascript = Course (
			name= "Javascript", 
    		duration_in_months= 10,
    		Course_number= "1002",
		    description= "Vanilla javascript and frameworks")

		self.hardware = Course (
			name= "Hardware", 
    		duration_in_months= 10,
    		Course_number= "1003",
		    description= " Product design using Fusion 360")

		self.teacher = Teacher (
			first_name= "James",
	        last_name= "Mwai",
	        place_of_residence= "Kilimani",
	        phone_number= "0723456786",
	        Email= "jamesmwai@gmail.com",
	        id_number= 3128956743,
	        profession= "Google Expert",
	        registration_number= "2344",
	        date_joined= datetime.date.today())

	def test_student_can_join_many_courses(self):
		self.assertEqual(self.student_a.courses.count(), 0)
		self.student_a.courses.add(self.python)
		self.assertEqual(self.student_a.courses.count(),1)

		