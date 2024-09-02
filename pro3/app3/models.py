from django.db import models
class department(models.Model):

    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name=models.CharField(max_length=255)
    doc_spec=models.CharField(max_length=255)
    dep_name=models.ForeignKey(department,on_delete=models.CASCADE)
    doc_image= models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'DR. ' + self.doc_name + ' -' + '(' + self.doc_spec + ')'


class Booking(models.Model):
    pati_name  =models.CharField(max_length=255)
    pati_phone=models.CharField(max_length=10)
    pati_email=models.EmailField()
    dep_name=models.ForeignKey(department,on_delete=models.CASCADE)
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    book_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
