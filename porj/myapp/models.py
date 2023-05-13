from django.db import models

# Create your models here.
class Books(models.Model):
    Author = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    copy_count = models.IntegerField()
    year_of_pub = models.DateField(auto_now=True)

class category(models.Model):
    cat_name = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    count = models.IntegerField()

    def __str__(self):
        return self.description

class product(models.Model):
    cat_id = models.ForeignKey(category, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    brand = models.CharField(max_length=100)
    count = models.IntegerField()
    price = models.FloatField(default=0)
    pic = models.FileField(upload_to ="myapp/static/pic", default=0)








#python manage.py makemigrations
#python manage.py migrate
# quit()
#
##Создание записи в таблице
#python manage.py shell
#from myapp.models import Books
#new = Books(Author = "", Title = "", copy_count = "")
#new.save()
#
##Получение данных из таблицы
#from myapp.models import Books
#res = Books.objects.all() # Получить все записи
#res2 = Books.objects.filter(id = 2) # Получение записи по условию
#
#res[0].Author # Получение значения столбца Author для записи

        