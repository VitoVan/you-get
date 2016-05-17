#!/usr/bin/env python

__all__ = ['eastmoney_download']
return_info = None

from ..common import *

def eastmoney_download(url, output_dir = '.', output_file = None, merge = True, info_only = False, **kwargs):
    if "video.eastmoney.com" in url:
        html = get_content(url)
        title = match1(html, r'<h1>(.+)</h1>')
        src = match1(html, r'src="http://player.kankanews.com/embed/([^"]+)"')
        frame_url = 'http://player.kankanews.com/embed/' + src
        frame_html = get_content(frame_url)
        url = match1(frame_html, r'var mp4 = "([^"]+)"')
        _, ext, size = url_info(url)
        print_info(site_info, title, ext, size)
        if info_only:
            return size
        else:
            download_urls([url], title, ext, size, output_dir = output_dir, merge = merge, output_file = output_file)

site_info = "video.eastmoney.com"
download = eastmoney_download
download_playlist = playlist_not_supported('eastmoney')
