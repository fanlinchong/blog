# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "My blog"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-26T12:30+08:00"
author = "Fan Linchong"
email = "fanlinchong@gmail.com"
author_homepage = "https://blog.fanlinchong.me"
description = "只坚持一种正义。我的正义。"
key_words = ['Maverick', 'fanlinchong', 'blog']
language = 'zh-CN'


head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''