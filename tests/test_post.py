from datetime import date
import unittest
from app.models import Post


class PostModelTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Post class
    '''

    def setUp(self):
        self.new_post = Post(id = 1, date_created = date.today(), content = "My very short test blog post")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def test_instance_variables(self):
        self.assertEqual(self.new_post.id, 1)
        self.assertEqual(self.new_post.content, "My very short test blog post")