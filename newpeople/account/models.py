from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
     
    GENDERS = (
        ('M', '남성(Man)'),
        ('W', '여성(Woman)'),
    )
    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDERS)

    AREA = (
        (1, '서울특별시'),
        (2, '부산광역시'),
        (3, '대구광역시'),
        (4, '인천광역시'),
        (5, '광주광역시'),
        (6, '대전광역시'),
        (7, '울산광역시'),
        (8, '세종특별자치시'),
        (9, '경기도'),
        (10, '강원도'),
        (11, '충청북도'),
        (12, '충청남도'),
        (13, '전라북도'),
        (14, '전라남도'),
        (15, '경상북도'),
        (16, '경상남도'),
        (17, '제주특별자치도'),
    )
    area = models.IntegerField(default="1", choices=AREA)
    
    KEYWORD = (
        (1,'디자인'),
        (2,'실무역량'),
        (3,'뷰티'),
        (4,'영상'),
        (5,'외국어'),
        (6,'음악'),
        (7,'라이프스타일'),
        (8,'기타'),
        (9,'취미')
    )
    keyword = models.IntegerField(default="1", choices=KEYWORD)




