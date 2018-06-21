from django.db import models

class Mobile(models.Model):
    Manufacturer = models.CharField(max_length = 60)
    Model_Name = models.CharField(max_length = 100)
    Model_Number = models.CharField(max_length = 50)

    #image
    Image = models.ImageField(default = None)

    #Specifications
    Display_Size = models.FloatField()
    CPU = models.CharField(max_length = 100)
    RAM = models.DecimalField(max_digits = 3, decimal_places = 0)
    GPU = models.CharField(max_length = 100)
    Front_Camera = models.DecimalField(max_digits = 3, decimal_places = 1)
    Rear_Camera = models.DecimalField(max_digits = 3, decimal_places = 1)
    Weight = models.DecimalField(max_digits = 4, decimal_places = 2)
    Resolution = models.CharField(max_length = 40)
    Battery_Rating = models.DecimalField(max_digits = 5, decimal_places = 0)
    Colour = models.CharField(max_length = 50)
    OS = models.CharField(max_length = 40)
    Storage = models.CharField(max_length = 40)

    #Warranty
    Warranty_Type = models.CharField(max_length = 50)
    Warranty_Duration = models.CharField(max_length = 70)

    Description = models.TextField(max_length = 240)
    Price = models.DecimalField(max_digits = 7, decimal_places = 2)

    def __str__(self):
        return 'Mobile: {} {}'.format(self.Manufacturer, self.Model_Name)

class Laptop(models.Model):
    Manufacturer = models.CharField(max_length = 60)
    Model_Name = models.CharField(max_length = 100)
    Model_Number = models.CharField(max_length = 50)

    #image
    Image = models.ImageField(default = None)

    #Specifications
    Screen_Size = models.FloatField()
    CPU = models.CharField(max_length = 100)
    RAM = models.DecimalField(max_digits = 3, decimal_places = 0)
    GPU = models.CharField(max_length = 100)
    Camera = models.CharField(max_length = 40)
    IO = models.TextField(max_length = 480)
    Storage = models.CharField(max_length = 100)
    OS = models.CharField(max_length = 40)
    Battery_Rating = models.DecimalField(max_digits = 3, decimal_places = 2)
    RAM_Type = models.CharField(max_length = 30)
    VRAM = models.DecimalField(max_digits = 3, decimal_places = 1)
    Internet_Connectivity = models.TextField(max_length = 140)

    #Warranty
    Warranty_Type = models.CharField(max_length = 50)
    Warranty_Duration = models.CharField(max_length = 70)

    Description = models.TextField(max_length = 240)
    Price = models.DecimalField(max_digits = 7, decimal_places = 2)

    def __str__(self):
        return 'Laptop: {} {}'.format(self.Manufacturer, self.Model_Name)

class Tablet(models.Model):
    Manufacturer = models.CharField(max_length = 60)
    Model_Name = models.CharField(max_length = 100)
    Model_Number = models.CharField(max_length = 50)

    #image
    Image = models.ImageField(default = None)

    #Specifications
    Display_Size = models.FloatField()
    CPU = models.CharField(max_length = 100)
    RAM = models.DecimalField(max_digits = 3, decimal_places = 0)
    GPU = models.CharField(max_length = 100)
    Front_Camera = models.DecimalField(max_digits = 3, decimal_places = 1)
    Rear_Camera = models.DecimalField(max_digits = 3, decimal_places = 1)
    Weight = models.DecimalField(max_digits = 4, decimal_places = 2)
    Resolution = models.CharField(max_length = 40)
    Battery_Rating = models.DecimalField(max_digits = 5, decimal_places = 0)
    Colour = models.CharField(max_length = 50)
    SKU = models.CharField(max_length = 40)
    OS = models.CharField(max_length = 40)
    Storage = models.CharField(max_length = 40)

    #Warranty
    Warranty_Type = models.CharField(max_length = 50)
    Warranty_Duration = models.CharField(max_length = 70)

    Description = models.TextField(max_length = 240)
    Price = models.DecimalField(max_digits = 7, decimal_places = 2)


    def __str__(self):
        return 'Tablet: {} {}'.format(self.Manufacturer, self.Model_Name)

class Headset(models.Model):
    Manufacturer = models.CharField(max_length = 60)
    Model_Name = models.CharField(max_length = 100)
    Model_Number = models.CharField(max_length = 50)

    #Image
    Image = models.ImageField(default = None)

    #Specifications
    Colour = models.CharField(max_length = 50)
    Driver_Size = models.DecimalField(max_digits = 4, decimal_places = 0)
    Type = models.CharField(max_length = 90)
    Driver_Type = models.CharField(max_length = 100)

    #Warranty
    Warranty_Type = models.CharField(max_length = 50)
    Warranty_Duration = models.CharField(max_length = 70)

    Description = models.TextField(max_length = 240)
    Price = models.DecimalField(max_digits = 7, decimal_places = 2)

    def __str__(self):
        return 'Headset: {} {}'.format(self.Manufacturer, self.Model_Name)

class PowerBank(models.Model):
    Manufacturer = models.CharField(max_length = 60)
    Model_Name = models.CharField(max_length = 100)
    Model_Number = models.CharField(max_length = 50)

    #Image
    Image = models.ImageField(default = None)

    #Specifications
    Capacity = models.CharField(max_length = 50)
    Input_Power = models.CharField(max_length = 50)
    Output_Power = models.CharField(max_length = 50)
    Output_ports = models.DecimalField(max_digits = 2, decimal_places = 0)
    Weight = models.DecimalField(max_digits = 3, decimal_places = 2)
    Dimension = models.CharField(max_length = 60)
    Colour = models.CharField(max_length = 50)

    #Warranty
    Warranty_Type = models.CharField(max_length = 50)
    Warranty_Duration = models.CharField(max_length = 70)

    Description = models.TextField(max_length = 240)
    Price = models.DecimalField(max_digits = 7, decimal_places = 2)

    def __str__(self):
        return 'PowerBank: {} {}'.format(self.Manufacturer, self.Model_Name)

class MemoryCard(models.Model):
    Manufacturer = models.CharField(max_length = 60)
    Model_Name = models.CharField(max_length = 100)
    Model_Number = models.CharField(max_length = 50)

    #Image
    Image = models.ImageField(default = None)

    #Specifications
    Capacity = models.DecimalField(max_digits = 3, decimal_places = 0)
    Write_Speed = models.DecimalField(max_digits = 3, decimal_places = 0)
    Dimension = models.CharField(max_length = 60)
    Weight = models.DecimalField(max_digits = 3, decimal_places = 2)
    Colour = models.CharField(max_length = 50)

    #Warranty
    Warranty_Type = models.CharField(max_length = 50)
    Warranty_Duration = models.CharField(max_length = 70)

    Description = models.TextField(max_length = 240)
    Price = models.DecimalField(max_digits = 7, decimal_places = 2)

    def __str__(self):
        return 'MemoryCard: {} {}'.format(self.Manufacturer, self.Model_Name)
        








        