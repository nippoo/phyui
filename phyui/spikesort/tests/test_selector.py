# -*- coding: utf-8 -*-

"""Tests of sparse matrix structures."""

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------

import os

import numpy as np
from numpy.testing import assert_array_equal
from pytest import raises

from ...datasets.mock import artificial_spike_clusters
from ..clustering import Clustering


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------

def test_selector():
    pass