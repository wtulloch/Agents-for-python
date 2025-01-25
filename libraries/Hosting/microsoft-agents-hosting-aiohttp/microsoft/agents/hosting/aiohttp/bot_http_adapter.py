# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from abc import abstractmethod
from typing import Optional, Protocol

from aiohttp.web import (
    Request,
    Response,
)

from microsoft.agents.botbuilder import Bot


class BotHttpAdapter(Protocol):
    @abstractmethod
    async def process(
        self, request: Request, bot: Bot
    ) -> Optional[Response]:
        raise NotImplementedError()
