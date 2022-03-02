#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
cfc_app/test_fob_Stats.py -- Characterization of behaviour on fob_stats custom command

Written by Robert Bruce, 2022
Licensed under Apache 2.0, see LICENSE for details
"""

# System imports
import datetime
import os

# Django and other third-party imports
from unittest import mock
from unittest.mock import call

import mockito
from mockito import when, verify, times
from django.conf import LazySettings
from django.test import Client
from django.test import TestCase

# Application imports
import cfc_app
from cfc_app.management.commands.fob_stats import Command

client = Client()


class GetDatasetsCustomCommandTests(TestCase):
    @classmethod
    @mock.patch("cfc_app.management.commands.fob_stats.FobStorage")
    def setUp(cls, storage):
        cls.subject = Command()

    @classmethod
    def tearDown(cls):
        return

# add_arguments
    @mock.patch("django.core.management.base.CommandParser")
    def test_add_arguments(self, parser):
        self.subject.add_arguments(parser);

        parser.add_argument.assert_has_calls([
            call("--prefix", help="Prefix of item names"),
            call("--suffix", help="Suffix of item names"),
            call("--after", help="Start after this item name"),
            call("--mode", help="From FILE, OBJECT, or BOTH"),
            call("--limit", help="Number of items to process",
                            type=int, default=self.subject.limit)])
        return

#End to End

#Show Stats