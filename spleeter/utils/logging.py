#!/usr/bin/env python
# coding: utf8

"""Centralized logging facilities for Spleeter."""

import logging
import warnings
from os import environ

# pylint: enable=import-error

__email__ = "spleeter@deezer.com"
__author__ = "Deezer Research"
__license__ = "MIT License"

environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


logger: logging.Logger = logging.getLogger("spleeter")
logger.setLevel(logging.INFO)
