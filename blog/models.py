from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, db_index=True, editable=False) #bi sıkıntı var ama hayırlısı



    def __str__(self):
        return f"{self.name}"


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Blog(models.Model): #12.satıra kadar blog için bir alan oluşturduk ve bunların içinde nelerin nasıl olmasını istediğimizi yazdık
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")#models.FileField  bu kodda olurdu fakat bu bütün dosyaları eklemeye yarar. Imagefield sadece resim ekelmek için yazılır
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True,db_index=True,editable=False)
    category = models.ForeignKey(Category,default=1, on_delete=models.CASCADE)


    def __str__(self): #title'ın str olarak dönmesini sağladık
        return f"{self.title}"
 

    def save(self,*args, **kwargs): #title'ı slug'a çevirmek için bir kod bloğu
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)

