from inspect import signature
from socket import SOL_UDP
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('docs/class_device.html'), features="html.parser")

