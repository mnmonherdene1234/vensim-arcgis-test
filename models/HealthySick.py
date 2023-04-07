"""
Python model 'HealthySick.py'
Translated using PySD
"""

from pathlib import Path
import numpy as np

from pysd.py_backend.statefuls import Integ
from pysd import Component

__pysd_version__ = "3.9.1"

__data = {"scope": None, "time": lambda: 0}

_root = Path(__file__).parent


component = Component()

#######################################################################
#                          CONTROL VARIABLES                          #
#######################################################################

_control_vars = {
    "initial_time": lambda: 0,
    "final_time": lambda: 30,
    "time_step": lambda: 0.03125,
    "saveper": lambda: time_step(),
}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


@component.add(name="Time")
def time():
    """
    Current time of the model.
    """
    return __data["time"]()


@component.add(
    name="FINAL TIME",
    units="Day",
    limits=(1.0, 30.0, 1.0),
    comp_type="Constant",
    comp_subtype="Normal",
)
def final_time():
    """
    The final time for the simulation.
    """
    return __data["time"].final_time()


@component.add(
    name="INITIAL TIME", units="Day", comp_type="Constant", comp_subtype="Normal"
)
def initial_time():
    """
    The initial time for the simulation.
    """
    return __data["time"].initial_time()


@component.add(
    name="SAVEPER",
    units="Day",
    limits=(0.0, np.nan),
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time_step": 1},
)
def saveper():
    """
    The frequency with which output is stored.
    """
    return __data["time"].saveper()


@component.add(
    name="TIME STEP",
    units="Day",
    limits=(0.0, np.nan),
    comp_type="Constant",
    comp_subtype="Normal",
)
def time_step():
    """
    The time step for the simulation.
    """
    return __data["time"].time_step()


#######################################################################
#                           MODEL VARIABLES                           #
#######################################################################


@component.add(
    name="get sick",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"infection_fraction": 1, "healthy": 1, "sick": 1},
)
def get_sick():
    return infection_fraction() * healthy() * sick()


@component.add(
    name="total poulation",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"healthy": 1, "sick": 1},
)
def total_poulation():
    return healthy() + sick()


@component.add(
    name="healthy",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_healthy": 1},
    other_deps={"_integ_healthy": {"initial": {}, "step": {"get_sick": 1}}},
)
def healthy():
    return _integ_healthy()


_integ_healthy = Integ(lambda: -get_sick(), lambda: 1000, "_integ_healthy")


@component.add(
    name="infection fraction",
    limits=(0.0, 0.005, 0.0001),
    comp_type="Constant",
    comp_subtype="Normal",
)
def infection_fraction():
    return 0.001


@component.add(
    name="sick",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_sick": 1},
    other_deps={"_integ_sick": {"initial": {}, "step": {"get_sick": 1}}},
)
def sick():
    return _integ_sick()


_integ_sick = Integ(lambda: get_sick(), lambda: 1, "_integ_sick")
