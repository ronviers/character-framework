"""Growing tube model estimation"""

# Copyright 2020 Koji Noshita
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import make_lsq_spline
from scipy import integrate


def estimate_gt_e_and_r0(arclength_parameters, thicknesses):
    """Estimate E in the growting tube model.
    The E corresponds to the $\log{\rm{Okamoto's} E}$ (see Noshita 2014, Okamoto 1988)

    Parameters
    =============
    arclength_parameters: 1D array-like
        arclength parameters for representing the positions
        on the growth trajectory
    thickness: 1D array-like
        tube thickness

    Returns
    =============
    e: float
        growth rate of tube $E$
    r0:
        initial tube thickness $r_0$
    """
    sol, cov = curve_fit(lambda l, r0, e: e * l + r0, arclength_parameters, thicknesses)
    r0, e = sol
    return e, r0


def gen_knots(start, end, num, rep):
    start_rep = np.repeat(start, rep - 1)
    knots = np.linspace(start, end, num)
    end_rep = np.repeat(end, rep - 1)
    knots = np.append(start_rep, knots)
    knots = np.append(knots, end_rep)
    return knots


def fit_bspline_curve(
    arclength_parameters, coords, initial_knots, k=3, revised_ratio=0.9, tol=10 ** (-7)
):
    """fit B-spline curve to the growth trajectory
    and update the archlength parameters to avoid over-estimation

    Parameters
    =============
    initial_knots: array_like, shape (n + k + 1,).
        Knots. Knots and data points must satisfy Schoenberg-Whitney conditions.

    k: int, optional
        B-spline degree. Default is cubic, k=3.

    Returns
    =============
    b: a BSpline object of the degree k with knots t.
    archlength_parameters_updated: array-like


    """
    arclength_parameters_updated = arclength_parameters.copy()
    knots = initial_knots.copy()

    arclength_ratio = 0
    while abs(1 - arclength_ratio) > tol:
        # b = make_lsq_spline(arclength_parameters_updated, coords, t=knots, k=k)
        b = make_lsq_spline(arclength_parameters_updated, coords, k=k, t=knots)
        db = b.derivative()
        arclength, abserr = integrate.quad(
            lambda l: np.linalg.norm(db(l)),
            knots[0],
            knots[-1],
            points=knots,
            limit=500,
        )

        arclength_old = arclength_parameters_updated[-1]
        arclength_ratio = arclength / arclength_old
        arclength_revised_ratio = (
            (arclength - arclength_old) * revised_ratio + arclength_old
        ) / arclength_old

        arclength_parameters_updated = (
            arclength_revised_ratio * arclength_parameters_updated
        )
        # print(arclength_old, arclength, arclength_ratio, abs(1 - arclength_ratio))
        knots = gen_knots(
            arclength_parameters_updated[0],
            arclength_parameters_updated[-1],
            200,
            k + 1,
        )

    return b, arclength_parameters_updated


def estimate_gt(arclength_parameters, thicknesses):
    return e, c, t, r0
