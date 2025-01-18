from dataclasses import dataclass
from typing import List, Optional

from ..client import Client, Resource
from ..response_builder import ChessDotComResponse, ResponseBuilder


@Client.endpoint
def get_streamers(tts=0, **request_options) -> "GetStreamersResponse":
    """
    :param tts: the time the client will wait before making the first request.
    :returns: :obj:`GetStreamersResponse` object containing
                information about Chess.com streamers.
    """
    return Resource(
        uri="/streamers",
        tts=tts,
        request_options=request_options,
        response_builder=ResponseBuilder(),
    )


class ResponseBuilder(ResponseBuilder):
    def build(self, text):
        data = self.serializer.deserialize(text)

        return GetStreamersResponse(
            json=data,
            text=text,
            streamers=[
                Streamer(
                    username=streamer.get("username"),
                    avatar=streamer.get("avatar"),
                    twitch_url=streamer.get("twitch_url"),
                    url=streamer.get("url"),
                    is_live=streamer.get("is_live"),
                    is_community_streamer=streamer.get("is_community_streamer"),
                    platforms=[
                        Platform(
                            type=platform.get("type"),
                            stream_url=platform.get("stream_url"),
                            channel_url=platform.get("channel_url"),
                            is_live=platform.get("is_live"),
                            is_main_live_platform=platform.get("is_main_live_platform"),
                        )
                        for platform in streamer.get("platforms", [])
                    ],
                )
                for streamer in data.get("streamers", [])
            ],
        )


class GetStreamersResponse(ChessDotComResponse):
    """
    :ivar json: The JSON response from the API.
    :ivar text: The raw text response from the API.
    :ivar streamers: List of streamers. Holds a list of :obj:`Streamer` objects.
    """

    def __init__(self, json, text, streamers):
        self.json = json
        self.text = text
        self.streamers = streamers


@dataclass(repr=True)
class Streamer(object):
    username: Optional[str]
    avatar: Optional[str]
    twitch_url: Optional[str]
    url: Optional[str]
    is_live: Optional[bool]
    is_community_streamer: Optional[bool]
    platforms: List["Platform"]


@dataclass(repr=True)
class Platform(object):
    type: Optional[str]
    stream_url: Optional[str]
    channel_url: Optional[str]
    is_live: Optional[bool]
    is_main_live_platform: Optional[bool]
