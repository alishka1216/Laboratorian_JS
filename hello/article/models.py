from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Article(BaseModel):
    title = models.CharField(max_length=120, null=False, blank=False, verbose_name='Заголовок')
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Контент')
    author = models.CharField(max_length=150, null=False, blank=False, default='Anon', verbose_name='Автор')

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.id}. {self.author}: {self.title}'


class Comment(BaseModel):
    article = models.ForeignKey(  # Поле - внешний ключ
        'article.Article',  # Указываем на какую модель создаём внешний ключ
        on_delete=models.CASCADE,  # указываем какая стратегия будет выбрана при удалении объекта связанной модели
        related_name='comments',  # указываем названия аттрибута, который будет добавлен к связанной модели (можем обращаться article.comments)
        verbose_name='Статья',  # имя, которое будет отображаться в панели администратора
        null=False,
        blank=False
    )
    comment = models.CharField(max_length=200, verbose_name='Комментарий', null=False, blank=False)
    author = models.CharField(max_length=150, null=False, blank=False, verbose_name='Автор')

    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
