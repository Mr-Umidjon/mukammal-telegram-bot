import math
from aiogram import types

from ..utils.misc import sh

from ...data.locations import Shops


def calc_disctance(lat1, lon1, lat2, lon2):
    R = 6371000
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = R * c
    return meters / 1000.0
