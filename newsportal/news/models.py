from django.db import models
from django.contrib.auth.models import User

# apps "News"


class User(User):
    """Таблица о пользователях"""
    pass


class Category(models.Model):
    """Таблица категорий"""
    name = models.CharField(max_length=100)



class Post(models.Model):
    """Таблица о постах"""
    news = 'NS'
    art = 'AT'
    blank = [(news, 'новость'),
             (art, 'статья')]
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=blank, default='NS')
    title = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1000)
    category = models.ManyToManyField('Category', through='PostCategory', blank = True)
    rating = models.IntegerField(default=0)


    def __str__(self):
        format_string = '%d.%m.%Y: %H:%M'
        return (f' Дата: {self.data.strftime(format_string)}'
                f'| Заголовок: {self.title} '
                f'| Автор:{self.author} '
                f'| Рейтинг:{self.rating}')


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating += 1
        self.save()

    def preview(self):
        return f'{self.content[:124]}...'


class PostCategory(models.Model):
    '''Таблица категорий с постами'''
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(models.Model):
    """Таблица комментарий"""
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        format_string = '%d.%m.%Y: %H:%M'
        return f' Date:{self.data.strftime(format_string)} | User:{self.user} | rating:{self.rating}  | comment:{self.content[:64]}...'

    def like(self):
        self.rating += 1
        self.save()


    def dislike(self):
        self.rating -= 1
        self.save()


class Author(models.Model):
    """Таблица о авторах постов"""
    name = models.OneToOneField('User', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{User.objects.get(pk=self.name.pk)}'

    def update_rating(self):
        posts = Post.objects.filter(author_id = self.pk)
        comments = Comment.objects.filter(user = self.name)

        self.rating = 0
        for post in posts:
            self.rating += post.rating * 3
            post_coments = Comment.objects.filter(post = post)
            for post_comment in post_coments:
                self.rating += post_comment.rating

        for comment in comments:
            self.rating += comment.rating

        self.save()




