from django.db import models

class Topic(models.Model):
    t_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.t_name
class Website(models.Model):
    t_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    code=models.CharField(max_length=100)
    def __str__(self):
        return self.code
class Push(models.Model):
    t_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    cloud=models.IntegerField()
    def __str__(self):
        return str(self.cloud)
