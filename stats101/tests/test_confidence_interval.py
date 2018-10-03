#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `stats101` package."""

from unittest import TestCase

import numpy as np
import pandas as pd

from stats101.confidence_interval import mean, proportion, _interval_data


class TestIntervalData(TestCase):
    def setUp(self):
        np.random.seed(0)

    def test_type_conversions(self):
        X = [1, 2, 3]
        _interval_data(X)

        X = pd.Series([1, 2, 3])
        _interval_data(X)
