from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
	course_name = models.CharField(max_length = 100)
	course_description = models.CharField(max_length = 200)
	course_creator = models.CharField(max_length = 30)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	course_image_cover = models.ImageField(upload_to='pics', null=True)

	def __str__(self):
		return self.course_name

	def is_enrolled_by(self,user):
		if self.enrollments.filter(user=user).exists():
			return True
		else:
			return False

class Assignments(models.Model):
	instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigments')
	course =models.ForeignKey(Course, on_delete=models.CASCADE,related_name='assigments', null=True)
	title = models.CharField(max_length=200)
	description = models.TextField()
	due_date= models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Submission(models.Model):
	student = models.ForeignKey(User, on_delete=models.CASCADE,related_name='submissions')
	assignment = models.ForeignKey(Assignments, on_delete=models.CASCADE, related_name='submissions')
	content = models.TextField()
	submitted_at = models.DateTimeField(auto_now_add=True)
	graded = models.BooleanField(default=False)
	grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	feedback = models.TextField(null=True)

	def __str__(self):
		return f"{self.student.username}- {self.assignment.title}"


class Enrollment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
	enroll_at = models.DateTimeField(auto_now_add=True)


	class meta:
		indexes=[
			models.Index(fields=['user','course'])
		]


	def __str__(self):
		return f'{self.user.username} enrolled in {self.course.course_name}'


class Lessons(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
	title = models.CharField( max_length=50)
	content = models.TextField()	
	order = models.IntegerField(null=True)

	def __str__(self):
		return f'{self.title}-{self.course.title}'
class Module(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	order = models.IntegerField(null=True)

	class Meta:
		verbose_name = ("Module")
		verbose_name_plural = ("Modules")

	def __str__(self):
		return f'{self.title}'

	
