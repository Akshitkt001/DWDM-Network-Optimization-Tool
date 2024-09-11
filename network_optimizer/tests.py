from django.test import TestCase
from .models import Node, Link

class NetworkOptimizerTests(TestCase):
    def setUp(self):
        # Create Node instances
        self.node1 = Node.objects.create(name="New York", location="40.7128° N, 74.0060° W")
        self.node2 = Node.objects.create(name="Los Angeles", location="34.0522° N, 118.2437° W")

        # Create Link instance using the Node instances
        Link.objects.create(source=self.node1, destination=self.node2, distance=100.0, capacity=50)

    def test_node_creation(self):
        node = Node.objects.get(name="New York")
        self.assertEqual(node.location, "40.7128° N, 74.0060° W")

    def test_link_creation(self):
        link = Link.objects.get(source=self.node1, destination=self.node2)
        self.assertEqual(link.distance, 100.0)
