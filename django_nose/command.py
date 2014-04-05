from django_nose.plugin import DjangoSetUpPlugin
from django_nose.runner import NoseTestSuiteRunner


class NoseDjango(DjangoSetUpPlugin):
    name = 'django'

    def __init__(self, runner=None):
        if not runner:
            runner = NoseTestSuiteRunner()
        DjangoSetUpPlugin.__init__(self, runner)
