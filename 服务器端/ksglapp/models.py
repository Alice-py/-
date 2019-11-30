from django.db import models
import time
# Create your models here.

# 自己创建的模型
class Stinfo(models.Model):
    class Meta:
        verbose_name = '学生管理'
        verbose_name_plural = '学生管理'
    
    st_id = models.CharField(max_length=20, db_column='学号', verbose_name='学号', primary_key=True)
    st_name = models.CharField(max_length=10,  db_column='姓名', verbose_name='姓名')
    st_password = models.CharField(max_length=20, db_column='密码', verbose_name='密码', default='001100')
    st_gender = models.CharField(max_length=2, default='男', db_column='性别', verbose_name='性别')
    st_college  = models.CharField(max_length=10,  db_column='学院', verbose_name='学院')
    st_major = models.CharField(max_length=20,  db_column='专业', verbose_name='专业')
    st_class = models.IntegerField(default=1,  db_column='班级', verbose_name='班级')
    st_position = models.CharField(max_length=10,  db_column='职位', default='群众', verbose_name='职位')

# class Verbose(models.Model):
# 	class Meta:
#         verbose_name = '职位管理'
#         verbose_name_plural = '职位管理'
# 		st_zw = models.CharField(max_length=20,db_column='职位'， verbose_name='职位', primary_key=True)
#       


class OpenDoor(models.Model):
    class Meta:
        verbose_name = '权限管理'
        verbose_name_plural = '权限管理'

    fsid = models.ForeignKey('Stinfo', on_delete=models.CASCADE, db_column='学号', verbose_name='学号')
    sprofessional = models.CharField(max_length=20, db_column='专业', verbose_name='专业')
    sposition = models.CharField(max_length=10, db_column='职位', default='群众', verbose_name='职位')

    spermissions = models.BooleanField(default=0, db_column='开门权限', verbose_name='开门权限')
	
class AppleLog(models.Model):
    class Meta:
        verbose_name = '日志'
        verbose_name_plural = '日志'
    
    stime = models.CharField(max_length=20, db_column='时间', verbose_name='时间', default=time.strftime("%m-%d %H:%M:%S", time.localtime()))
    sid = models.CharField(max_length=20, db_column='学号', verbose_name='学号')
    sprofessional = models.CharField(max_length=20, db_column='专业', verbose_name='专业')
    sphone = models.CharField(max_length=20, db_column='手机号', verbose_name='手机号')
    sresults = models.BooleanField(default=0, db_column='申请结果', verbose_name='申请结果')
    
    
    
    
    