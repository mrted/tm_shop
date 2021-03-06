from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Model: Category


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name

# Model: Product Brand

# class Brand(models.Model):
#     name = models.CharField(max_length=30, blank=True, null=True)
    

#     def __str__(self):
#         return self.name

# Model: Product color

# class Color(models.Model):
#     name = models.CharField(max_length=30, blank=True, null=True)

#     def __str__(self):
#         return self.name

# Model: Product availability

# class Available(models.Model):
#     name = models.CharField(max_length=30, blank=True, null=True)

#     def __str__(self):
#         return self.name

# Model: Product

class Product(models.Model): 
    product_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    stock = models.IntegerField()
    product_image = models.ImageField(upload_to='product', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    product_color = models.CharField(max_length=50, blank=True, null=True)
    featured_products = models.BooleanField(default=False)
    hot_deals = models.BooleanField(default=False)
    # product_short_description = models.TextField(max_length=200, blank=True)
    # product_full_description = models.TextField(blank=True)  
    product_condition_1 = models.CharField(max_length=30, blank=True, null=True)      
    product_condition_2 = models.CharField(max_length=30, blank=True, null=True)      
    product_condition_3 = models.CharField(max_length=30, blank=True, null=True)      
    product_condition_4 = models.CharField(max_length=30, blank=True, null=True)      
    product_condition_5 = models.CharField(max_length=30, blank=True, null=True)      
    product_condition_6 = models.CharField(max_length=30, blank=True, null=True)      
    product_condition_7 = models.CharField(max_length=30, blank=True, null=True)      
    product_condition_8 = models.CharField(max_length=30, blank=True, null=True)      
    product_condition_9 = models.CharField(max_length=30, blank=True, null=True)      
    product_condition_10 = models.CharField(max_length=30, blank=True, null=True)      
    # product_specification_1 = models.TextField(blank=True, null=True)
    # title_of_product_specification_2 = models.CharField(max_length=30, blank=True, null=True)
    # product_specification_2 = models.TextField(blank=True, null=True)
    # title_of_product_specification_3 = models.CharField(max_length=30, blank=True, null=True)
    # product_specification_3 = models.TextField(blank=True, null=True)
    # specification4_title = models.CharField(max_length=30, blank=True, null=True)
    # specification4 = models.TextField(blank=True, null=True)
      
    
    #brand = models.CharField(max_length=50, blank=True, null=True)
    #brand_image = models.ImageField(upload_to='brand_image', blank=True, null=True)
    
    #product_image_thumb1 = models.ImageField(upload_to='product', blank=True, null=True)
    #product_image_thumb2 = models.ImageField(upload_to='product', blank=True, null=True)
    #product_image_thumb3 = models.ImageField(upload_to='product', blank=True, null=True)
    #product_image_thumb4 = models.ImageField(upload_to='product', blank=True, null=True)
    # image2 = models.ImageField(upload_to='product', blank=True, null=True)
    
    available = models.BooleanField(default=True)
    product_created_at = models.DateTimeField(auto_now_add=True)
    product_updated_at = models.DateTimeField(auto_now=True)
    
    
    # featured_products_description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('product_name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


# Customer

# class CustomerInfo(models.Model):
#     full_name= models.ChartField(max_length  = 150)
#     email= models.EmailField()
#     phone_number = models.CharField(max_length= 20)
#     address = models.CharField(max_length = 150)

# Model: Cart


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='product', blank=True, null=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return str(self.product)

# Model: Order


class Order(models.Model):
    token = models.CharField(max_length=250, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='USD Order Total')
    emailAddress = models.EmailField(max_length=250, blank=True, verbose_name='Email Address')
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=250, blank=True)
    billingAddress1 = models.CharField(max_length=250, blank=True)
    billingCity = models.CharField(max_length=250, blank=True)
    billingPostcode = models.CharField(max_length=250, blank=True)
    billingCountry = models.CharField(max_length=250, blank=True)
    shippingName = models.CharField(max_length=250, blank=True)
    shippingAddress1 = models.CharField(max_length=250, blank=True)
    shippingCity = models.CharField(max_length=250, blank=True)
    shippingPostcode = models.CharField(max_length=250, blank=True)
    shippingCountry = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'Order'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='USD Price')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'OrderItem'

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.content
