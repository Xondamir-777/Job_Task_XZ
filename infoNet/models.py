from django.db import models
from django.core.validators import RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

    time_creation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}---------{self.time_creation}"
    class Meta:
        ordering = ['-time_creation']

class NewsPhotos(models.Model):
    news_id = models.ForeignKey("News", on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to="News/", blank=True)
    
class VideoType(models.TextChoices):

    Videos = (
        "Videos",
        _("Videolar")
    )

    Digests = (
        "Digests",
        _("Dayjestlar")
    )
    Podcasts = (
        "Podcasts",
        _("Podkastlar")
    )
    InnoTime = (
        "InnoTime",
        _("InnoTime")
    )
    Interviews = (
        "Interviews",
        _("Intervyular")
    )

class VideoNews(models.Model):
    # choices = [
    #     ('Videos','Videolar'),
    #     ('Digests', 'Dayjestlar'),
    #     ('Podcasts','Podkastlar'),
    #     ('InnoTime', 'InnoTime'),
    #     ('Interviews','Intervyular')
    # ]
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()
    url = models.CharField(max_length=255)
    news_type = models.CharField(choices=VideoType.choices)
    time_creation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}--{self.news_type}---{self.time_creation}----{self.time_creation}"
    class Meta:
        ordering = ['-time_creation']

class Brochures(models.Model):
    photo=models.ImageField(upload_to="Brochures/", blank=True)
    time_creation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"----{self.time_creation}"
    class Meta:
        ordering = ['-time_creation']

class positions(models.TextChoices):

    leadership = (
        "Leadership",
        _("Rahbariyat")
    )

    Director_Advisor = (
        "Director_Advisor",
        _("Direktor Maslahatchisi")
    )
    Departments = (
        "Departments",
        _("Boshqarmalar")
    )
    Sections = (
        "Sections",
        _("Bo'limlar")
    )
class Leadership(models.Model):
    # Choices=[
    #     ('Leadership', 'Rahbariyat'),
    #     ('Director_Advisor', 'Direktor Maslahatchisi'),
    #     ('Departments', 'Boshqarmalar'),
    #     ('Sections', "Bo'limlar"),
    # ]
    name=models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    structure = models.CharField(choices=positions.choices)
    photo = models.ImageField(upload_to="Leaders/", blank=True)
    def __str__(self):
        return f"{self.name} {self.position}"

    
class Vacancies(models.Model):
    title =models.CharField(max_length=255)
    description = RichTextUploadingField()
    def __str__(self):
        return f"{self.title}"

class Publication(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    photo = models.ImageField(upload_to="Publication/", blank=True)
    editorial_board = RichTextUploadingField()
    general_information = RichTextUploadingField()
    url = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.title}"

def user_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'article/files/{filename}'

class MagazinesPDF(models.Model):
    # url = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="Magazines/", blank=True)
    upload = models.FileField(upload_to = user_directory_path, null=True)
    time_creation = models.DateTimeField(auto_now_add=True)
    publication = models.ForeignKey("Publication", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.pk} by {self.publication}----- {self.time_creation}"
    class Meta:
        ordering = ['-time_creation']

class Partners(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    photo = models.ImageField(upload_to="Partners/", blank=True)
    def __str__(self):
        return f"{self.title}"

class Projects(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    photo = models.ImageField(upload_to="Projects/", blank=True)
    def __str__(self):
        return f"{self.title}"

class source_type(models.TextChoices):

    Information_System = (
        "Information System",
        _("Axborot tizimlari")
    )

    Data_Analys = (
        "Data Analys",
        _("Ma\'lumotlarni tahlil qilish")
    )

class InfoSySsrc(models.Model):
    # Choices=[
    #     ('Information System', 'Axborot tizimlari'),
    #     ('Data Analys', "Ma'lumotlarni tahlil qilish"),
    # ]
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    type = models.CharField(choices=source_type.choices)
    url = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.title} --- {self.type}"

class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    def __str__(self):
        return f"{self.title}"

# phone_validator = RegexValidator(
#     regex=r'^\+d{3}\d{9}$',
#     message='Введите номер в формате +998901234567'
# )

class UsersMessage(models.Model):
    user_name= models.CharField(max_length=255)
    user_email= models.CharField(max_length=255)
    phone= models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"name: {self.user_name} {'-'*10} email: {self.user_email} "
    class Meta:
        ordering = ['-created_at']

# m1=Publication(short_topic="Iim-fan",
#     title="Iim-fan", content="Coming soon1",
#             editorial_board="Coming soon1", 
#             general_information="Coming soon1")
# m2 = Publication(short_topic="Innovator",
#     title="Innovator", content="Coming soon2",
#             editorial_board="Coming soon2", 
#             general_information="Coming soon2")