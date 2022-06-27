from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
import brightway2 as bw
import SALib
from tabulate import tabulate
from sympy import *
from scipy.stats import binned_statistic
import seaborn as sns
from IPython.display import HTML, display
import bw2analyzer as bwa
import matplotlib as mpl 
import scipy
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

# Custom utils defined for inter-acv
from lca_algebraic import *
from lca_algebraic.params import FixedParamMode
from lca_algebraic.stats import *
from lca_algebraic.stats import _generate_random_params, _compute_stochastics

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:70% !important; }</style>"))

import bw2io

pd.options.display.max_rows = 100
pd.options.display.float_format = '{:,.3g}'.format


# Setup bw2
initDb('ENFI_v1')

# Import Ecoinvent DB (if not already done)
# Update the PATH to suit your installation
importDb("ecoinvent 3.7.1 apos", 'C:/Users/DELL/ecoinvent 3.7.1_apos_ecoSpold02/datasets')

#importDb("ecoinvent 3.7.1 consequential", 'C:/Users/DELL/学术/ecoinvent 3.7.1_consequential_ecoSpold02/datasets')

# We use a separate DB for defining our model, reset it beforehand
USER_DB='ENFI_jetfuel'
resetDb(USER_DB)

# Parameters are stored at project level : reset them
resetParams(USER_DB)