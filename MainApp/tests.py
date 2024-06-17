from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Student, TheClass, Course

class ViewsTestCase(TestCase):
    
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create test data for classes and courses
        self.test_class = TheClass.objects.create(creator=self.user, name='Test Class', code='TST101')
        self.test_course = Course.objects.create(creator=self.user, title='Test Course', code='TEST101')
        
        # Create a test student
        self.test_student = Student.objects.create(creator=self.user, student_id='S123', first_name='John', last_name='Doe', current_class=self.test_class)
        
        # Create a Django test client
        self.client = Client()
        self.client.login(username='testuser', password='password')
    
    def test_home_page_view(self):
        response = self.client.get(reverse('home'))  # Assuming 'home' is the name of your homepage URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'))  # Assuming 'dashboard' is the name of your dashboard URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
        # Additional assertions for context data if needed
    
    def test_add_student_view(self):
        data = {
            'student_id': 'S456',
            'fname': 'Jane',
            'lname': 'Smith',
            'current_class': self.test_class.code,
        }
        response = self.client.post(reverse('add_student'), data)
        self.assertEqual(response.status_code, 302)  # Assuming successful redirect (HTTP 302)
        self.assertTrue(Student.objects.filter(student_id='S456', first_name='Jane', last_name='Smith').exists())
    
    def test_add_course_view(self):
        data = {
            'name': 'Mathematics',
            'code': 'MATH101',
        }
        response = self.client.post(reverse('add_course'), data)
        self.assertEqual(response.status_code, 302)  # Assuming successful redirect (HTTP 302)
        self.assertTrue(Course.objects.filter(title='Mathematics', code='MATH101').exists())
    
    def test_add_class_view(self):
        data = {
            'name': 'Test Class 2',
            'code': 'TST102',
            'courses': [self.test_course.id],
        }
        response = self.client.post(reverse('add_class'), data)
        self.assertEqual(response.status_code, 302)  # Assuming successful redirect (HTTP 302)
        self.assertTrue(TheClass.objects.filter(name='Test Class 2', code='TST102').exists())
    
    def test_marks_view_get(self):
        response = self.client.get(reverse('marks'))  # Assuming 'marks' is the name of your marks URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_students.html')
        # Additional assertions for context data if needed
    
    def test_marks_view_post(self):
        data = {
            'q': self.test_student.student_id,
        }
        response = self.client.post(reverse('marks'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_students.html')
        # Additional assertions for context data if needed
    
    def test_add_marks_view(self):
        data = {
            'student_id': self.test_student.student_id,
            'course': self.test_course.code,
            'cat1': 85,
            'cat2': 90,
            'fat': 80,
        }
        response = self.client.post(reverse('add_marks'), data)
        self.assertEqual(response.status_code, 302)  # Assuming successful redirect (HTTP 302)
        # Optionally, you can check if the data record exists in the database
        self.assertTrue(Data.objects.filter(student=self.test_student, course=self.test_course).exists())
    
    def test_student_report_view(self):
        response = self.client.get(reverse('student_report', kwargs={'student_id': self.test_student.student_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_report.html')
        # Additional assertions for context data if needed
    
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    
    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
    
    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Assuming successful redirect (HTTP 302)
        # Check if user is logged out (assertion depends on your application's behavior)
