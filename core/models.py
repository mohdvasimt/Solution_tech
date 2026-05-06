from django.db import models

SERVICE_CHOICES = [
    ('whatsapp_bot', 'WhatsApp Bot Development'),
    ('automation', 'Business Automation'),
    ('website', 'Website Template / Development'),
    ('mobile_app', 'Mobile App Development'),
    ('other', 'Other / Multiple Services'),
]

class ContactQuery(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.EmailField()
    phone      = models.CharField(max_length=20, blank=True)
    service    = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='other')
    message    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read    = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Query'
        verbose_name_plural = 'Contact Queries'

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.get_service_display()}"


class WebTemplate(models.Model):
    CATEGORY_CHOICES = [
        ('business','Business'),('ecommerce','E-Commerce'),
        ('portfolio','Portfolio'),('restaurant','Restaurant'),
        ('realestate','Real Estate'),('saas','SaaS / Tech'),
    ]
    name        = models.CharField(max_length=120)
    category    = models.CharField(max_length=40, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    emoji       = models.CharField(max_length=10, default='🌐')
    gradient    = models.CharField(max_length=200, default='linear-gradient(135deg,#0a2a20,#0d3d2b)')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MobileTemplate(models.Model):
    PLATFORM_CHOICES = [
        ('both','iOS & Android'),('ios','iOS Only'),('android','Android Only'),
    ]
    name        = models.CharField(max_length=120)
    category    = models.CharField(max_length=60)
    description = models.TextField()
    platform    = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default='both')
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    emoji       = models.CharField(max_length=10, default='📱')
    gradient    = models.CharField(max_length=200, default='linear-gradient(135deg,#0a1a35,#0d2558)')
    tech_stack  = models.CharField(max_length=200, default='React Native')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
