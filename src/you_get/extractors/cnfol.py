#!/usr/bin/env python

__all__ = ['cnfol_download']
return_info = None

from ..common import *

def cnfol_download(url, output_dir = '.', merge = True, info_only = False, **kwargs):
    if "video.cnfol.com" in url:
        html = get_content(url)
        title = match1(html, r'<h1>(.+)</h1>')
        url = match1(html, r"{f:'([^']+)'")
        _, ext, size = url_info(url)
        # set info for programmable use
        global return_info
        return_info = (site_info, title, ext, size, url)
        print_info(site_info, title, ext, size)
        if not info_only:
            download_urls([url], title, ext, size, output_dir = output_dir, merge = merge)

site_info = "video.cnfol.com"
download = cnfol_download
download_playlist = playlist_not_supported('cnfol')
