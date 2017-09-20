from django.db import models

# Create your models here.
class Names(models.Model):
    name = models.CharField(max_length=200, verbose_name="الاسم")
    age = models.IntegerField(verbose_name="العمر")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "السواق"
        verbose_name = "السايق"

class Cars(models.Model):
    car_name = models.CharField(max_length=200, verbose_name="نوع السيارة")
    number = models.CharField(max_length=200, verbose_name="رقم السيارة")
    ali = models.CharField(max_length=200)

    q = (
        ('نعم', 'نعم'),
        ('لا', 'لا'),
    )
    Cooler = models.CharField(max_length=200, choices = q, verbose_name="مبردة")
    def __str__(self):
        return self.number
    class Meta:
        verbose_name_plural = "السيارات"
        verbose_name = "السيارة"
class Cars_lines(models.Model):

    name = models.ForeignKey(Names, on_delete=models.CASCADE, verbose_name="اسم السئق")
    car_name = models.ForeignKey(Cars, on_delete=models.CASCADE, verbose_name="السيارة")
    place = models.CharField(max_length=200, verbose_name="المكان")
    number_of_Employees = models.IntegerField(verbose_name="عدد الموظفين")
    def __str__(self):
        return self.car_name
    class Meta:
        verbose_name_plural = "سيارات الخطوط"
        verbose_name = "سيارة الخط"

class Duties(models.Model):
    name = models.ForeignKey(Names, on_delete=models.CASCADE, verbose_name="اسم الساءق")
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, verbose_name="السيارة")
    q = (
        ('ذهاب', 'ذهاب'),
        ('عودة', 'عودة'),
    )
    type = models.CharField(max_length=200, choices = q, verbose_name="النوع")
    place = models.CharField(max_length=200, verbose_name="المكان")
    Counter = models.IntegerField(verbose_name="عداد الوقود")
    date = models.DateField(verbose_name="الوقت")
    time = models.TimeField(verbose_name="التاريخ")
    def __str__(self):
        return self.car.car_name
    class Meta:
        verbose_name_plural = "الواجبات"
        verbose_name = "الواجب"

class Maintenance(models.Model):
    name = models.ForeignKey(Names, on_delete=models.CASCADE, verbose_name="اسم الساءق")
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, verbose_name="السيارة")
    type_of_problem = models.CharField(max_length=200, verbose_name="نوع العطل")
    q = (
        ('تحتاج اصلاح', 'تحتاج اصلاح'),
        ('تم الاصلاح', 'تم الاصلاح'),
    )

    case = models.CharField(max_length=200, choices = q, verbose_name="حالة السيارة")
    q = (
        ('نعم', 'نعم'),
        ('لا', 'لا'),
        ('لا تحتاج اصلاح', 'لا تحتاج اصلاح'),
    )
    possibility_of_fix = models.CharField(max_length=200, choices = q, verbose_name="امكانية الصيانة")
    date = models.DateField(verbose_name="االتاريخ")
    time = models.TimeField(verbose_name="الوقت")
    def __str__(self):
        return self.car.car_name
    class Meta:
        verbose_name_plural = "الصيانة"
        verbose_name = "الصيانة"