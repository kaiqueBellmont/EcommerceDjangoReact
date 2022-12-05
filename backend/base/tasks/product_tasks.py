import time
from django.http import JsonResponse
from ..models import Product
from celery import shared_task
from rest_framework.generics import get_object_or_404
from logging import log


def run_job(product):
    update_product.delay(product)


@shared_task
def update_product(product):
    print("Start update_product: %s" % time.ctime())
    print("Product : %s" % product)
    time.sleep(10)
    job = product
    job.status = 'Success'
    print(job)
    print("End update_field: %s" % time.ctime())

