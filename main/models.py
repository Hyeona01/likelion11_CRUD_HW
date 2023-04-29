from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__ (self): #입력한 데이터가 호출되면 데이터의 title이 대표값으로 나오게 함
        return self.title
    
    def summary(self):
        return self.body[:50]
