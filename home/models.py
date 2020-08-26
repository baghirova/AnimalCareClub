from django.db import models
import os
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Languages(models.Model):

    language_name = models.CharField(max_length=122)
    language_id=models.IntegerField()
    language_short_name=models.CharField(max_length=3)
    def __str__(self):
        return self.language_name



class Menu(models.Model):
    home = models.CharField(max_length=122)
    about = models.CharField(max_length=122)
    events = models.CharField(max_length=122)
    rescued=models.CharField(max_length=60)
    contact = models.CharField(max_length=122)

    adoption = models.CharField(max_length=20)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    temporary - models.CharField(max_length=1)

    def __str__(self):

        return self.language.language_name



class Home(models.Model):

    slogan=models.CharField(max_length=265)
    total_donation_title = models.CharField(max_length=122)
    total_donation_text = models.TextField()
    total_donation_amount = models.CharField(max_length=122)
    total_volunteers_title = models.CharField(max_length=122)
    total_volunteers_text = models.TextField()
    total_volunteers_amount = models.CharField(max_length=15)
    future_plans_title = models.CharField(max_length=122)
    future_plans_amount=models.CharField(max_length=12)
    future_plans_text = models.TextField()
    total_projects_title = models.CharField(max_length=33)
    total_projects_amount = models.CharField(max_length=22)
    image_welcome_acc = models.ImageField(blank=True)
    about_us_title = models.CharField(max_length=100)
    about_us_text = models.TextField(max_length=2500)
    our_key_features_title = models.CharField(max_length=122)
    our_key_features_text = models.TextField()
    sponsorship_title = models.CharField(max_length=44)
    sponsorship_text = models.TextField()
    donate_amount_title = models.CharField(max_length=44)
    donate_amount_text = models.TextField()
    become_volunteer_title = models.CharField(max_length=44)
    become_volunteer_text = models.TextField()
    testimonial_title=models.CharField(max_length=122)
    testimonial_text=models.TextField(max_length=200)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    upcoming_events_title=models.CharField(max_length=120)
    upcoming_events_slogan=models.CharField(max_length=120)
    logo=models.ImageField(blank=True)
    def __str__(self):
        return str(self.slogan) + str(self.total_donation_title)

class Report(models.Model):
    donor_name = models.CharField(max_length=44)
    amount = models.CharField(max_length=19)


class Event(models.Model):
    title_in_eng = models.CharField(max_length=44)
    event_little_detail_in_eng = models.TextField()
    details_in_eng = models.TextField()
    title_in_az = models.CharField(max_length=44)
    event_little_detail_in_az = models.TextField()
    details_in_az = models.TextField()
    report=models.ManyToManyField(Report,blank=True)
    date = models.DateTimeField()
    event_address = models.CharField(max_length=120)
    event_city = models.CharField(max_length=120)
    image_main = models.CharField(max_length=720, blank=True)
    event_image1 = models.CharField(max_length=720, blank=True)
    event_image2 = models.CharField(max_length=720, blank=True)
    event_image3 = models.CharField(max_length=720, blank=True)
    event_image4 = models.CharField(max_length=720, blank=True)
    event_image5 = models.CharField(max_length=720, blank=True)
    event_image6 = models.CharField(max_length=720, blank=True)
    event_image7 = models.CharField(max_length=720, blank=True)
    event_image8 = models.CharField(max_length=720, blank=True)
    event_image9 = models.CharField(max_length=720, blank=True)
    event_image10 = models.CharField(max_length=720, blank=True)
    event_image11 = models.CharField(max_length=720, blank=True)
    event_image12 = models.CharField(max_length=720, blank=True)
    event_image13 = models.CharField(max_length=720, blank=True)
    event_image14 = models.CharField(max_length=720, blank=True)
    event_image15 = models.CharField(max_length=720, blank=True)
    event_image16 = models.CharField(max_length=720, blank=True)
    event_image17 = models.CharField(max_length=720, blank=True)
    event_image18 = models.CharField(max_length=720, blank=True)
    event_image19 = models.CharField(max_length=720, blank=True)
    event_image20 = models.CharField(max_length=720, blank=True)
    event_image21 = models.CharField(max_length=720, blank=True)
    event_image22 = models.CharField(max_length=720, blank=True)
    event_image23 = models.CharField(max_length=720, blank=True)
    event_image24 = models.CharField(max_length=720, blank=True)
    event_image25 = models.CharField(max_length=720, blank=True)
    event_image26 = models.CharField(max_length=720, blank=True)
    event_image27 = models.CharField(max_length=720, blank=True)
    event_image28 = models.CharField(max_length=720, blank=True)
    event_image29 = models.CharField(max_length=720, blank=True)
    event_image30 = models.CharField(max_length=720, blank=True)
    event_image31 = models.CharField(max_length=720, blank=True)
    event_image32 = models.CharField(max_length=720, blank=True)
    event_image33 = models.CharField(max_length=720, blank=True)
    event_image34 = models.CharField(max_length=720, blank=True)
    event_image35 = models.CharField(max_length=720, blank=True)
    event_image36 = models.CharField(max_length=720, blank=True)
    event_image37 = models.CharField(max_length=720, blank=True)
    event_image38 = models.CharField(max_length=720, blank=True)
    event_image39 = models.CharField(max_length=720, blank=True)
    event_image40 = models.CharField(max_length=720, blank=True)
    upcoming = models.BooleanField(default=False)
    event_iframe=models.CharField(max_length=720,blank=True )
    type=models.CharField(max_length=35)
    slug=models.SlugField(unique=True, editable=False, max_length=130)


    class Meta:
        ordering = ['-date']
    def get_absolute_url_eng(self):
        return reverse('animalcare:event_detail_eng', kwargs={'slug': self.slug})

    def get_absolute_url_az(self):
        return reverse('animalcare:event_detail_az', kwargs={'slug': self.slug})

    def get_rescued_absolute_url_eng(self):
        return reverse('animalcare:rescued_detail_eng', kwargs={'slug': self.slug})

    def get_rescued_absolute_url_az(self):
        return reverse('animalcare:rescued_detail_az', kwargs={'slug': self.slug})

        # return "/post/{}".format(self.id)

    # def __str__(self):
    #     if self.upcoming==1:
    #         return self.title_in_az + self.title_in_eng + "////////////////////////////This event is UPCOMING/////////////////////////////////" + "this menu is in ==================>" + self.language.language_name
    #     else:
    #         return self.title_in_az+self.title_in_eng "////////////////////////////This event is NOT UPCOMING/////////////////////////////" + "this menu is in ==================> "+ self.language.language_name

    def get_unique_slug(self):
        slug = slugify(self.title_in_eng.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Event.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Event, self).save(*args, **kwargs)


class Volunteer(models.Model):
    full_name = models.CharField(max_length=122)
    birth = models.DateTimeField()
    is_doing = models.CharField(max_length=122)
    description = models.TextField()
    image = models.ImageField(blank=True)

    language = models.ForeignKey(Languages, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name + "in" + self.language.language_name


class Contacts(models.Model):
    our_address = models.CharField(max_length=122)
    our_address_detailed = models.CharField(max_length=122)
    telephone_number = models.CharField(max_length=122)
    telephone_number_text = models.TextField()
    mail = models.EmailField()
    mail_text = models.TextField()
    language = models.ForeignKey(Languages,on_delete=models.CASCADE)
    def __str__(self):
        return self.language.language_name

class Message(models.Model):
    name = models.CharField(max_length=122)
    email =models.EmailField()
    subject=models.CharField(max_length=122)
    message_text=models.TextField()
    def __str__(self):
        return self.name + self.email



class Donor_review(models.Model):
    donor_name = models.CharField(max_length=122)
    donor_is_who = models.CharField(max_length=122)
    donor_description = models.TextField()
    donor_image = models.ImageField(blank=True)
    language=models.ForeignKey(Languages,on_delete=models.CASCADE)

class Donor_Details(models.Model):
    Donor_name = models.CharField(max_length=122)
    Donor_surname = models.CharField(max_length=122)
    Donor_gives = models.IntegerField()
    Donation_time = models.DateTimeField(auto_now_add=True)

class Animal_need_help(models.Model):
    animal_name = models.CharField(max_length=122)
    animal_image1 = models.ImageField(blank=True,upload_to="animal_need_help")

    animal_image2 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image3 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image4 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image5 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image6 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image7 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image8 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image9 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image10 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image11 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image12 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image13 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_need_amount = models.IntegerField()
    animal_is_donated = models.IntegerField()

    donor = models.ManyToManyField(Donor_Details,blank=True)


# ADDED BY DEV2
class PaymentPro(models.Model):
    payment = models.TextField()

class HomePro(models.Model):
    """ info for home page """
    payments = models.ManyToManyField(PaymentPro)
    headerNews = models.TextField()
    TextNews = models.TextField()
    language = models.ForeignKey(Languages, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"Home in {self.language.language_name}"
class CarriersPro(models.Model):
    iframe = models.TextField()
    language = models.ForeignKey(Languages, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carriers form in {self.language.language_name}"
class TasksPro(models.Model):
    tasks = models.TextField()

class AboutPro(models.Model):
    maintext = models.TextField()
    secondtext = models.TextField()
    thirdtext = models.TextField()
    fourthtext = models.TextField()
    language = models.ForeignKey(Languages, null=True, on_delete=models.CASCADE)
    task = models.ManyToManyField(TasksPro)

    def __str__(self):
        return f"About in {self.language.language_name}"
class ImagePro(models.Model):
    image = models.ImageField(null=True, blank=True,upload_to="adoption_image")
    image_url = models.URLField(blank=True, help_text="eger fotonu her hansi bir platformaya yuklemisinizse, mes. Google drive, o fotonun linki bura paisdir ve sekili yuxaridaki yerden upload EtMe!))")

class AdoptionPro(models.Model):
    name = models.CharField(max_length=128)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=16) #Choises apply
    sort = models.CharField(max_length=128)
    about = models.TextField()
    images = models.ManyToManyField(ImagePro)
    contact = models.TextField()
    adopted = models.BooleanField(default=False, help_text='Eger himayeye goturulubse check box edin ki web sehifede gorunmesin')
    def __str__(self):
        return f"{self.name}"
