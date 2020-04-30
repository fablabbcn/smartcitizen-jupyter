''' Implementation of different processes to be done in each device '''

from scdata.utils import LazyCallable
from .formulae import absolute_humidity, exp_f, fit_exp_f
from .timeseries import clean_ts, merge_ts, rolling_avg
from .baseline import find_min_max, baseline_calc, get_delta_baseline, get_als_baseline
from .alphasense import basic_4electrode_alg, baseline_4electrode_alg

