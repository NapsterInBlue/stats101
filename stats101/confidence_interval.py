# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from scipy import stats


def mean(conf_level, data):
    pHat, stdErr, degFreedom = _interval_data(conf_level, data)

    return stats.t.interval(conf_level, df=degFreedom, loc=pHat, scale=stdErr)


def proportion(conf_level, data):
    pHat, stdErr, degFreedom = _interval_data(conf_level, data)

    return stats.norm.interval(conf_level, loc=pHat, scale=stdErr)


def _interval_data(data):
    if isinstance(data, pd.Series):
        data = data.values

    if isinstance(data, list):
        data = np.array(data)

    assert isinstance(data, np.ndarray)

    pHat = np.mean(data)
    stdErr = stats.sem(data)
    degFreedom = len(data) - 1

    return pHat, stdErr, degFreedom
