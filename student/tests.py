from django.test import TestCase
from .models import Student
import datetime
from .forms import StudentForm
from django.urls import reverse
from django.test import Client
client = Client()

# Create your tests here.

class StudentTestCase(TestCase):
	def setUp(self):
		self.student=Student(
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

	def test_full_name_contains_first_name(self):
		self.assertIn(self.student.first_name, self.student.full_name())

	def test_full_name_contains_last_name(self):
		self.assertIn(self.student.last_name, self.student.full_name())

	def test_age_is_always_above_17(self):
		self.assertFalse(self.student.clean() < 17)

	def test_age_is_always_below_30(self):
		self.assertFalse(self.student.clean() > 30)

class CreateStudentTestCase(TestCase):
	def setUp(self):
		self.data = {
		'first_name': "Tiffany", 
		"last_name": "Jeruto", 
		"date_of_birth": datetime.date(2000,6,24), 
		"registration_number": "254016", 
		"Email": "tiffanylalampaa@gmail.com", 
		"phone_number": "0789647745", 
		"place_of_residence": "Rongai", 
		"guardian_phone": "0789567484", 
		"id_number": 345378625, 
		"date_joined": datetime.date.today()}

		self.bad_data = {
		'first_name': "dfgh ", 
		"last_name": "lhgfdfgh ", 
		"date_of_birth": datetime.date(2000,6,24), 
		"registration_number": "tuiok", 
		"Email": " ", 
		"phone_number": "0789647745", 
		"place_of_residence": "Rongai", 
		"guardian_phone": "0789567484", 
		"id_number": 345378625, 
		"date_joined": datetime.date.today()}

	def test_student_form_accepts_valid_data(self):
		form = StudentForm(self.data)
		self.assertTrue(form.is_valid())

	def test_student_form_rejects_invalid_data(self):
		form = StudentForm(self.bad_data)
		self.assertFalse(form.is_valid())

	def test_add_student_view(self):
		url = reverse("add_student")
		request = client.post(url, self.data)
		self.assertEqual(request.status_code, 200)

	def test_add_student_bad_request_view(self):
		url = reverse("add_student")
		request = client.post(url, self.bad_data)
		self.assertEqual(request.status_code, 400)
