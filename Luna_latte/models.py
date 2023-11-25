# lunalatte/models.py
from django.db import models


class MenuItem(models.Model):
    """
    Represents a menu item in the application.

    Attributes:
    - name (str): The name of the menu item.
    - description (str): The description of the menu item.
    - price (float): The price of the menu item.
    - image (str): The URL or path to the image of the menu item.

    Methods:
    - __str__: Returns a string representation of the menu item.
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    image = models.CharField(max_length=2083)

    def __str__(self):
        """
        Returns a string representation of the menu item.

        Returns:
        - str: The name of the menu item.
        """
        return self.name

    class Meta:
        app_label = 'Luna_latte'
