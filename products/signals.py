from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def product_saved(sender, instance, created, **kwargs):
    if created:
        print(f'New product created: {instance}')
    else:
        print(f'Product updated: {instance}')


@receiver(pre_save, sender=Product)
def product_about_to_save(sender, instance, **kwargs):
    print(f'About to add/update the product: {instance}')


@receiver(pre_delete, sender=Product)
def product_about_to_delete(sender, instance, **kwargs):
    print(f'About to delete product: {instance}')


@receiver(post_delete, sender=Product)
def product_deleted(sender, instance, **kwargs):
    print(f'Product deleted: {instance}')
