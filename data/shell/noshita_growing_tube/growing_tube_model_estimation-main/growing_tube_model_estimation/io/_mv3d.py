# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

from ..growing_tube import estimate_gt_e_and_r0


def _read_mv3d_as_df(filepath):
    """
    read a Microvisu3D file as pandas dataframe

    """

    PRT_MV3D_LINES = re.compile(
        r"^#(\s+)Number(\s+)of(\s+)lines(\s+)(?P<line_num>[0-9]+)$"
    )
    PRT_MV3D_PONTS = re.compile(
        r"^#(\s+)Number(\s+)of(\s+)points(\s+)(?P<point_num>[0-9]+)$"
    )
    PRT_MV3D_INTER = re.compile(
        r"^#(\s+)Number(\s+)of(\s+)inter.(\s+)(?P<inter_num>[0-9]+)$"
    )

    with open(filepath, "r") as f:
        lines = f.readlines()
    mv3d_lines = [line.replace("\n", "").split("\t") for line in lines]

    m = PRT_MV3D_LINES.match(mv3d_lines[1][0])
    line_num = int(m["line_num"])

    m = PRT_MV3D_PONTS.match(mv3d_lines[2][0])
    point_num = int(m["point_num"])

    m = PRT_MV3D_INTER.match(mv3d_lines[3][0])
    inter_num = int(m["inter_num"])

    print("line_num: ", line_num)
    print("point_num: ", point_num)
    print("inter_num: ", inter_num)

    mv3d_data_lines = [line for line in mv3d_lines[7:] if len(line) == 5]

    mv3d_data = [
        [int(line[0]), float(line[1]), float(line[2]), float(line[3]), float(line[4])]
        for line in mv3d_data_lines
    ]

    df_mv3d = pd.DataFrame(mv3d_data, columns=["no", "x", "y", "z", "d"])
    return df_mv3d


def _read_mv3d_as_growth_trajectory(filepath, adjust_direction_flag=True):
    df_mv3d = _read_mv3d_as_df(filepath)
    coords = df_mv3d[["x", "y", "z"]].to_numpy()
    thicknesses = df_mv3d["d"].to_numpy()
    arclength_parameters = np.append(
        0, np.linalg.norm(coords[0:-1] - coords[1:], axis=1)
    )
    arclength_parameters = np.cumsum(arclength_parameters)

    if adjust_direction_flag:
        e, r0 = estimate_gt_e_and_r0(arclength_parameters, thicknesses)
        if e < 0:
            coords = coords[::-1]
            thicknesses = thicknesses[::-1]
            arclength_parameters = arclength_parameters[::-1]
            arclength_parameters = -(arclength_parameters - arclength_parameters[0])
    return coords, thicknesses, arclength_parameters


def read_mv3d(filepath, read_as="df", kws={}):
    if read_as == "df":
        X = _read_mv3d_as_df(filepath)
    elif read_as == "growth_trajectory":
        if "adjust_direction_flag" in kws:
            adjust_direction_flag = kws["adjust_direction_flag"]
            X = _read_mv3d_as_growth_trajectory(filepath, adjust_direction_flag)
        else:
            X = _read_mv3d_as_growth_trajectory(filepath)

    return X
