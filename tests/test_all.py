# -*- coding: iso-8859-1 -*-
"""
Unit tests for the WsgiDAV package.
"""

from tests import test_lock_manager, test_property_manager, test_wsgidav_app,\
    test_util
from unittest import TestSuite, TextTestRunner
import sys


def run():
    suite = TestSuite([test_util.suite(),
                       test_lock_manager.suite(),
                       test_property_manager.suite(),
                       test_wsgidav_app.suite(),
                       ])
    failures = TextTestRunner(descriptions=0, verbosity=2).run(suite)
    sys.exit(failures)



if __name__ == "__main__":
    run()