# -*- coding: utf-8 -*-

"""Clustering utility functions."""

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------

import numpy as np


#------------------------------------------------------------------------------
# Utility functions
#------------------------------------------------------------------------------

def _unique(x):
    """Faster version of np.unique().

    This version is restricted to 1D arrays of non-negative integers.

    It is only faster if len(x) >> len(unique(x)).

    """
    if len(x) == 0:
        return np.array([], dtype=np.int)
    return np.nonzero(np.bincount(x))[0]


def _spikes_in_clusters(spike_clusters, clusters):
    """Return the labels of all spikes belonging to the specified clusters."""
    if len(spike_clusters) == 0 or len(clusters) == 0:
        return np.array([], dtype=np.int)
    return np.nonzero(np.in1d(spike_clusters, clusters))[0]
