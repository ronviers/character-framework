"""Growing tube model"""

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

import numbers
import numpy as np


def growing_tube_model(s, phi, E, C, T, r0=1, p0=np.zeros(3), R0=np.diag([1, 1, 1])):
    """Growing tube model
    Parameters
    =============
    s: real, np.ndarray
        growth stage
    phi: real, np.ndarray
        parameter of generating curve
    E: real, np.ndarray, or callable
        growth rate of tube
    C: real, np.ndarray, or callable
        Standardized curvature
    T: real, np.ndarray, or callable
        Standardized torsion
    r0: float
        initial tube thickness
    p0: 1D array-like
        initial position
    R0: 2D array-like
        initial orientation

    Returns
    =============
    UMat: np.ndarray
        Coordinate values
    """

    if (
        isinstance(E, numbers.Real)
        & isinstance(C, numbers.Real)
        & isinstance(T, numbers.Real)
    ):
        UMat = _growing_tube_model_const(s, phi, E, C, T, r0, p0, R0)
    else:
        raise NotImplementedError("Not implemented yet")

    return UMat


def _generating_spiral_const(s, E, C, T, r0):
    E_g = E
    C_g = C
    T_g = T

    D = np.sqrt(C_g**2 + T_g**2)

    ED3E2pD2 = E_g * D**3 * (E_g**2 + D**2)
    expEs = np.exp(E_g * s)
    sinDs = np.sin(D * s)
    cosDs = np.cos(D * s)

    P = (
        r0
        * D
        * (
            (
                (D**2) * (T_g**2)
                + (E_g**2) * (T_g**2)
                + C_g**2 * E_g**2 * cosDs
                + E_g * D * (C_g**2) * sinDs
            )
            * expEs
            - D**2 * (E_g**2 + T_g**2)
        )
        / ED3E2pD2
    )
    Q = (
        r0
        * C_g
        * D
        * E_g
        * (-expEs * (C_g**2 + T_g**2) * cosDs + D * (D + expEs * E_g * sinDs))
        / ED3E2pD2
    )
    R = (
        r0
        * C_g
        * T_g
        * D
        * (
            ((E_g**2) + (D**2) - (E_g**2) * cosDs - E_g * D * sinDs) * expEs
            - D**2
        )
        / ED3E2pD2
    )

    PMat = np.array([P, Q, R]).T

    return PMat


def _generating_curve_const(s, phi, E, C, T, r0):
    D = np.sqrt(C**2 + T**2)
    X = -(
        C
        * np.exp(E * s)
        * r0
        * (
            (D**2) * np.cos(phi) * np.sin(s * D)
            + T * D * (-1 + np.cos(s * D)) * np.sin(phi)
        )
    ) / (D**3)
    Y = (
        np.exp(E * s)
        * r0
        * (np.cos(s * D) * np.cos(phi) - (T * np.sin(s * D) * np.sin(phi)) / D)
    )
    Z = (
        np.exp(E * s)
        * r0
        * (
            (T * np.cos(phi) * np.sin(s * D)) / D
            + (C**2 + (T**2) * np.cos(s * D)) * np.sin(phi) / (D**2)
        )
    )

    QMat = np.array([X, Y, Z]).T

    return QMat


def _growing_tube_model_const(
    s, phi, E, C, T, r0=1, p0=np.zeros(3), R0=np.diag([1, 1, 1])
):
    """Growing tube model with constant parameters

    Parameters
    =============
    s: real, np.ndarray
    phi: real, np.ndarray
    E: real
    C: real
    T: real
    r0: real
    p0: 1D array-like
    R0: 2D array-like

    Returns
    =============
    UMat: np.ndarray
        Coordinate values
    """

    PMat = _generating_spiral_const(s, E, C, T, r0)
    QMat = _generating_curve_const(s, phi, E, C, T, r0)

    UMat = PMat + QMat
    UMat = p0 + np.apply_along_axis(lambda v: R0 @ v, -1, UMat)
    UMat = UMat.T

    return UMat
