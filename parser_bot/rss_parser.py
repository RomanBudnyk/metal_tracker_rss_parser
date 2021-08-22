from datetime import datetime
from http import HTTPStatus
from time import mktime

from feedparser import parse

from constants import STYLES, RSS_ENDPOINT, HOUR_IN_MS


def parse_rss() -> list:
    albums = parse(RSS_ENDPOINT)
    assert albums.status == HTTPStatus.OK
    found_albums = []
    for album in albums.entries:
        if this_style := [style for style in STYLES if style in album.summary_detail.value]:
            dt = datetime.fromtimestamp(mktime(album.published_parsed))
            if datetime.now().timestamp() - dt.timestamp() <= HOUR_IN_MS:
                found_albums.append(f'{album.title}\n{", ".join(this_style)}\n{album.link}\n')
    return found_albums
