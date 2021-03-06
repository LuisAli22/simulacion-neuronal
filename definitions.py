#!/usr/bin/env python3
import numpy as np
import math
import time
import simpy
import scipy
from scipy.integrate import ode
from scipy.integrate import solve_ivp
import statistics

RESISTENCIA= 60e6
CONDUCTANCIA_LEAK=(1/RESISTENCIA)
TIEMPO_TOTAL_SIMULACION=1.0
LAMBDA_EXCITATORIO=2000.0
LAMBDA_INHIBITORIO=434.0
TASA_DE_ARRIBO_EXCITATORIO=(1/LAMBDA_EXCITATORIO)
TASA_DE_ARRIBO_INHIBITORIO=(1/LAMBDA_INHIBITORIO)
PASO=1e-1
CAPACITANCIA_MEMBRANA=250e-12
TAU_MEMBRANA=(RESISTENCIA*CAPACITANCIA_MEMBRANA)
CORRIENTE_NULA=0
ALFA_EXCITATORIO=390.5e-12
TAU_EXCITATORIO=0.2e-3
TAU_INHIBITORIO=2e-3
ALFA_INHIBITORIO= -74e-12
POTENCIAL_DE_REPOSO=-60e-3
TENSION_UMBRAL=-50e-3
TIEMPO_REFRACTARIO=2e-3
DURACION= 0.2
POTENCIAL_EXCITATORIO_INVERSO=0.0
POTENCIAL_INHIBITORIO_INVERSO=-75e-3
BETA_EXCITATORIO= 7.1e-12
BETA_INHIBITORIO= 3.7e-12