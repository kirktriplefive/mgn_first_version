from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=150)
    text = models.TextField("Предложение")
    url = models.SlugField(max_length=160, unique=True, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("view_post", kwargs={"slug": self.url})

    def __str__ (self):
        return self.title
    
    def get_comment(self):
        return self.comments_set.filter(parent__isnull=True)
    
    class Meta:
        verbose_name="Пост"
        verbose_name_plural = "Посты"

class PostImages(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Изображение", upload_to="posts_images/")
    post = models.ForeignKey(Post, verbose_name="Пост", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name="Изображение"
        verbose_name_plural = "Изображения"
    

class Comments(models.Model):
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Комментарий", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, null=True, blank = True)
    post = models.ForeignKey(Post, verbose_name="Пост", on_delete=models.CASCADE )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}-{self.post}"

    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
