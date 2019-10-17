import pytest
import numpy as np
from numpy.testing import assert_almost_equal

from ...benchmarks.simulation import linear
from ..pearson import Pearson


class TestPearsonStat:
    @pytest.mark.parametrize("n", [10, 100, 1000])
    @pytest.mark.parametrize("obs_stat", [1.0])
    @pytest.mark.parametrize("obs_pvalue", [1/1000])
    def test_linear_oned(self, n, obs_stat, obs_pvalue):
        np.random.seed(123456789)
        x, y = linear(n, 1, dim=1, noise=0)
        stat, pvalue = Pearson().test(x, y)

        assert_almost_equal(stat, obs_stat, decimal=2)
        assert_almost_equal(pvalue, obs_pvalue, decimal=2)