from django.test import TestCase
from .models import Course
from .forms import CourseForm
from django.urls import reverse
from django.test import Client

client = Client()
# Create your tests here.

class CreateCourseTestCase(TestCase):
	def setUp(self):
		self.data = {
			"name": "Javascript", 
    		"duration_in_months": 10,
    		"Course_number": "1001",
		    "description": "Vanilla javascript and frameworks"
    	
			}

		self.bad_data = {
			"name": " ", 
    		"duration_in_months": 10,
    		"Course_number": " ",
		    "description": " "
    	 
			}


	def test_course_form_accepts_valid_data(self):
		form = CourseForm(self.data)
		self.assertTrue(form.is_valid())

	def test_course_form_rejects_invalid_data(self):
		form = CourseForm(self.bad_data)
		self.assertFalse(form.is_valid())

	def test_add_course_view(self):
		url = reverse("add_course")
		request = client.post(url, self.data)
		self.assertEqual(request.status_code, 200)

	def test_add_course_bad_request_view(self):
		url = reverse("add_course")
		request = client.post(url, self.bad_data)
		self.assertEqual(request.status_code, 400)
