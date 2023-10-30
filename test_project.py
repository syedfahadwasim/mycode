import pytest
from project import is_valid
from project import regression
from project import correlation
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import os


def test_is_valid1():
    data = pd.DataFrame({'A': [100, 50, 25, 5], 'B':[150, 75, 40, 10]})
    indep_var = 'A'
    dep_var = 'B'
    outcome = is_valid(data, indep_var, dep_var)
    assert outcome is not None
    #assert type(outcome) == pd.DataFrame

def test_is_valid_when_both_variables_are_same2():
    data = pd.DataFrame({'A': [100, 50, 25, 5], 'B':[150, 75, 40, 10]})
    indep_var = 'A'
    dep_var = 'A'
    outcome = is_valid(data, indep_var, dep_var)
    assert outcome is None

def test_is_valid_when_one_variable_is_invalid3():
    data = pd.DataFrame({'A': [100, 50, 25, 5], 'B':[150, 75, 40, 10]})
    indep_var = 'C'
    dep_var = 'A'
    outcome = is_valid(data, indep_var, dep_var)
    assert outcome is None

def test_regression4():
    data_subset = pd.DataFrame({'A': [100, 50, 25, 5], 'B':[150, 75, 40, 10]})
    indep_var = 'B'
    dep_var = 'A'
    outcome = regression(data_subset, indep_var, dep_var)
    assert outcome is None

def test_regression_plot_generation5():
    data_subset = pd.DataFrame({'A': [100, 50, 25, 5], 'B':[150, 75, 40, 10]})
    indep_var = 'B'
    dep_var = 'A'
    regression(data_subset, indep_var, dep_var)
    assert os.path.exists('regression_plot.png')
    os.remove('regression_plot.png')


def test_correlation6():
    data_subset = pd.DataFrame({'A': [100, 50, 25, 5], 'B':[150, 75, 40, 10]})
    indep_var = 'B'
    dep_var = 'A'
    outcome = correlation(data_subset)
    assert outcome is None

def test_correlation_plot_generation7():
    data_subset = pd.DataFrame({'A': [100, 50, 25, 5], 'B':[150, 75, 40, 10]})
    correlation(data_subset)
    assert os.path.exists('correlation_plot.png')
    os.remove('correlation_plot.png')


