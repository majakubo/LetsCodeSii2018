from flask import url_for
from flask_testing import TestCase
import helpful_spirits
from helpful_spirits.models import *

class HelpfulSpiritsTestCase(TestCase):

    def create_app(self):
        return helpful_spirits.create_app('test')