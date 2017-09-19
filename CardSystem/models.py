from django.db import models


def image_path(instance, filename):
    return './cards/%s/%s' % (instance.username, filename)


def background_path(instance, filename):
    return './background/%s/%s' % (instance.username, filename)


class Cards(models.Model):
    # 名片对应的用户, 内容对应 Users.username
    username = models.CharField(max_length=18)
    # 名片标题
    title = models.CharField(max_length=32)
    # 联系方式
    name = models.CharField(max_length=16)
    phone = models.IntegerField()
    qq = models.IntegerField()
    wechat = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    address = models.CharField(max_length=50)
    # 背景图*1 和 名片图片*10
    background = models.FileField(upload_to=background_path)
    image0 = models.FileField(upload_to=image_path)
    image1 = models.FileField(upload_to=image_path)
    image2 = models.FileField(upload_to=image_path)
    image3 = models.FileField(upload_to=image_path)
    image4 = models.FileField(upload_to=image_path)
    image5 = models.FileField(upload_to=image_path)
    image6 = models.FileField(upload_to=image_path)
    image7 = models.FileField(upload_to=image_path)
    image8 = models.FileField(upload_to=image_path)
    image9 = models.FileField(upload_to=image_path)

    def __str__(self):
        return self.title


class Users(models.Model):
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=18)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Messages(models.Model):
    # 留言者的信息
    name = models.CharField(max_length=16)
    phone = models.IntegerField()
    # 留言内容
    content = models.TextField(max_length=200)
    # 留言目标用户, 内容对应 Users.username
    target_user = models.CharField(max_length=18)

    def __str__(self):
        return self.target_user
