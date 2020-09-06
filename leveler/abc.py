from abc import ABC, abstractmethod
from io import BytesIO
from logging import Logger
from re import Match
from typing import List, Optional

from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from redbot.core import Config, commands
from redbot.core.bot import Red


class MixinMeta(ABC):
    """
    Base class for well behaved type hint detection with composite class.
    Basically, to keep developers sane when not all attributes are defined in each mixin.
    """

    bot: Red
    log: Logger

    config: Config

    _db_ready: bool
    client: AsyncIOMotorClient
    db: AsyncIOMotorDatabase
    session: ClientSession

    @abstractmethod
    async def _connect_to_mongo(self):
        raise NotImplementedError

    @abstractmethod
    async def _create_user(self, user, server):
        raise NotImplementedError

    @abstractmethod
    async def _is_mention(self, user) -> str:
        raise NotImplementedError

    @abstractmethod
    async def _hex_to_rgb(self, hex_num: str, a: int) -> tuple:
        raise NotImplementedError

    @abstractmethod
    async def _rgb_to_hex(self, rgb) -> str:
        raise NotImplementedError

    @abstractmethod
    async def _badge_convert_dict(self, userinfo):
        raise NotImplementedError

    @abstractmethod
    async def _process_purchase(self, ctx) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def _is_hex(self, color: str) -> Optional[Match]:
        raise NotImplementedError

    @abstractmethod
    async def _truncate_text(self, text, max_length) -> str:
        raise NotImplementedError

    @abstractmethod
    def bool_emojify(self, bool_var: bool) -> str:
        raise NotImplementedError

    @abstractmethod
    async def _handle_levelup(self, user, userinfo, server, channel):
        raise NotImplementedError

    @abstractmethod
    async def _required_exp(self, level: int) -> int:
        raise NotImplementedError

    @abstractmethod
    async def _level_exp(self, level: int) -> int:
        raise NotImplementedError

    @abstractmethod
    async def _find_level(self, total_exp) -> int:
        raise NotImplementedError

    @abstractmethod
    async def _find_server_rank(self, user, server) -> int:
        raise NotImplementedError

    @abstractmethod
    async def _find_global_rank(self, user) -> int:
        raise NotImplementedError

    @abstractmethod
    async def _find_server_exp(self, user, server) -> int:
        raise NotImplementedError

    @abstractmethod
    async def _find_server_rep_rank(self, user, server) -> int:
        raise NotImplementedError

    @abstractmethod
    async def _find_global_rep_rank(self, user) -> int:
        raise NotImplementedError

    @abstractmethod
    async def draw_profile(self, user, server) -> BytesIO:
        raise NotImplementedError

    @abstractmethod
    async def draw_rank(self, user, server) -> BytesIO:
        raise NotImplementedError

    @abstractmethod
    async def draw_levelup(self, user, server) -> BytesIO:
        raise NotImplementedError

    @abstractmethod
    async def _process_exp(self, message, userinfo, exp: int):
        raise NotImplementedError

    @abstractmethod
    async def _give_chat_credit(self, user, server):
        raise NotImplementedError

    @abstractmethod
    async def _valid_image_url(self, url):
        raise NotImplementedError

    @abstractmethod
    async def _auto_color(self, ctx, url: str, ranks) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    async def _center(self, start, end, text, font) -> int:
        raise NotImplementedError

    @abstractmethod
    async def char_in_font(self, unicode_char, font) -> bool:
        raise NotImplementedError

    @abstractmethod
    def _contrast(self, bg_color, color1, color2):
        raise NotImplementedError

    @abstractmethod
    def _luminance(self, color):
        raise NotImplementedError

    @abstractmethod
    def _contrast_ratio(self, bgcolor, foreground):
        raise NotImplementedError

    @abstractmethod
    async def _name(self, user, max_length) -> str:
        raise NotImplementedError

    async def _add_dropshadow(
        self,
        image,
        offset=(4, 4),
        background=0x000,
        shadow=0x0F0,
        border=3,
        iterations=5,
    ):
        raise NotImplementedError

    async def _add_corners(self, im, rad, multiplier=6):
        raise NotImplementedError


class CompositeMetaClass(type(commands.Cog), type(ABC)):
    """
    This allows the metaclass used for proper type detection to
    coexist with discord.py's metaclass
    """

    pass