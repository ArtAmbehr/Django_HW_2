# from django.shortcuts import render
from django.http import HttpResponse
import logging
from myapp.models import Order, Client, Product

logger = logging.getLogger(__name__)


def hello_world(requesr):
    logger.info("Visit page Hello world")
    return HttpResponse('Hello world')


def main(request):
    descryption_main = '''
Some INFOS
    '''
    logger.info("Visit page main")
    return HttpResponse(descryption_main)


def about(request):
    about_descryption = '''
    <h2>Я студент в сфере IT,<br>
    и мне ни за что, с пути не сойти..<br>
    буду я профи, в backend разработке,<br>
    и будет доход минимальный 3 стоки!!!</h2><br>
    '''
    logger.info("Visit page about")
    return HttpResponse(about_descryption)


def all_orders(request):
    order = Order.objects.all()
    return HttpResponse(order)