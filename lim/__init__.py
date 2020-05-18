# -*- coding: utf-8 -*-

import pbr.version

version_info = pbr.version.VersionInfo('lim')
try:
    __version__ = version_info.version_string()
except AttributeError:
    __version__ = '19.8.2'

try:
    __release__ = version_info.release_string()
except AttributeError:
    __release__ = '19.8.2'

__author__ = 'Dave Dittrich'
__email__ = 'dave.dittrich@gmail.com'

__all__ = ['__author__', '__email__', '__version__', '__release__']

# vim: set ts=4 sw=4 tw=0 et :
