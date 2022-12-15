from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from ...data import config


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,

        )