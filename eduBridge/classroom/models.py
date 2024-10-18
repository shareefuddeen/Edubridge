from django.db import models

class Course(models.Model):
	course_name = models.CharField(max_length = 100)
	course_description = models.CharField(max_length = 200)
	course_creator = models.CharField(max_length = 30)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	course_image_cover = models.ImageField(upload_to=pictures)


	def __str__(self):
		return self.course_name