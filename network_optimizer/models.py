from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Link(models.Model):
    source = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='outgoing_links')
    destination = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='incoming_links')
    distance = models.FloatField()  # in kilometers
    capacity = models.IntegerField()  # in Gbps

    def __str__(self):
        return f"{self.source.name} to {self.destination.name}"

class Wavelength(models.Model):
    name = models.CharField(max_length=50)
    frequency = models.FloatField()  # in THz

    def __str__(self):
        return self.name

class Path(models.Model):
    source = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='paths_from')
    destination = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='paths_to')
    links = models.ManyToManyField(Link)
    wavelength = models.ForeignKey(Wavelength, on_delete=models.SET_NULL, null=True)
    latency = models.FloatField()  # in milliseconds

    def __str__(self):
        return f"Path from {self.source.name} to {self.destination.name}"