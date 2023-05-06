from django.db import models

# Create your models here.


class ClassRoom(models.Model):
    name = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name + " " + self.year
    

class Subject(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name





class Student(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        
    )
    std_index_no = models.CharField(
        max_length=20, primary_key=True)
    std_ID = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    img = models.ImageField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, choices=GENDER)
    phone = models.CharField(max_length=200, null=True)
    b_date = models.DateField(null=True)
    father_name = models.CharField(max_length=200, null=True)
    mother_name = models.CharField(max_length=200, null=True)
    classRoom = models.ForeignKey(
        ClassRoom, null=True, on_delete=models.SET_NULL)
    comment = models.TextField(null=True)

    def __str__(self):
         return self.name



class Marks(models.Model):
    TERMS = (("TERM1", "TERM 1"), ("TERM2", "TERM 2"), ("TERM3", "TERM 3"))
    # student = models.ForeignKey(
    #     Student, null=True, on_delete=models.SET_NULL)
    # subject = models.ForeignKey(
    #     Subject, null=True, on_delete=models.SET_NULL)

    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)

    term = models.CharField(max_length=50, null=True, choices=TERMS)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    marks = models.IntegerField(null=True, blank=True)


    



    # def __str__(self):
    #     return self.subject

class Teacher(models.Model):
    ROLES = (("Principal", "Principal"), ("Wise_Principal", "wise Principal"),
             ("Class_Teacher", "Class Teacher"), ("Other", "Other"))
    name = models.CharField(max_length=200, null=True)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=50, null=True, choices=ROLES)
    classRoom = models.ForeignKey(
        ClassRoom, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class SchoolDetails(models.Model):
    SchoolName = models.CharField(max_length=100, null=True)
    subjectCount = models.IntegerField(null=True)
    studentCount = models.IntegerField(null=True)
    teachersCount = models.IntegerField(null=True)
    labsCount = models.IntegerField(null=True)
    latestHeading = models.CharField(max_length=100, null=True)
    latestImg = models.ImageField(null=True, blank=True)
    latestDescription1 = models.CharField(max_length=500, null=True)
    feature1 = models.CharField(max_length=100, null=True)
    feature2 = models.CharField(max_length=100, null=True)
    feature3 = models.CharField(max_length=100, null=True)
    latestDescription2 = models.CharField(max_length=500, null=True)

class ContactDetails(models.Model):
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    facebookLink = models.CharField(max_length=1000)
    twitterLink = models.CharField(max_length=1000)
    googlePlus = models.CharField(max_length=1000)
    linkedInLink = models.CharField(max_length=1000)
    youtubeLink = models.CharField(max_length=1000)
    addressLine1 = models.CharField(max_length=100)
    addressLine2 = models.CharField(max_length=100)
    addressLine3 = models.CharField(max_length=100)
    websiteLink = models.CharField(max_length=1000)

