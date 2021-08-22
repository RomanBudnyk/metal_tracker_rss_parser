import glob
import logging
import os
import sys

from pycodestyle import Checker

directory = os.path.join('parser_bot', '**.py')
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def test_pep8():
    errors = 0
    for filename in glob.glob(directory):
        errors += Checker(filename, ignore=('E501',)).check_all()
    assert not errors, 'Please check PEP8 errors!'
    logging.info('No PEP8 errors! :)')


test_pep8()
