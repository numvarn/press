# แบบฝึกหัด Django App สำหรับทำความเข้าใจความสัมพันธ์แบบ One-to-Many

## โดย

ผู้ช่วยศาสตราจารย์พิศาล สุขขี

สาขาวิทยาการคอมพิวเตอร์

มหาวิทยาลัยราชภัฏศรีสะเกษ

## โมเดล

เป็นการอธิบายความสัมพันธ์แบบ One-to-Many ระหว่างโมเดล 2 โมเดล คือ Author และ Article
โดยกำหนดให้ Author สามารถเขียนบทความ (Article) ได้หลายบทความ แต่
บทความ 1 บทความ สามารถมีผู้เขียนได้แค่ 1 คนเท่านั้น

```python
class Author(models.Model):
    """Model definition for Author."""
    prefix = models.IntegerField(choices=name_prefix_choice)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Author."""

        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        """Unicode representation of Author."""
        return self.first_name + " "+self.last_name
```

```python
class Article(models.Model):
    """Model definition for Article."""

    # TODO: Define fields here
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    detail = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.title
```

## Screen Shot

(!image)[statics/thumbnails/001.png]

![image]("./statics/thumbnails/001.png")

<kbd>![001]("https://github.com/numvarn/press/blob/main/statics/thumbnails/001.png?raw=true")</kbd>
