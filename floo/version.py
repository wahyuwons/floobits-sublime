PLUGIN_VERSION = '3.4.2'
# The line above is auto-generated by tag_release.py. Do not change it manually.

try:
    from .common import shared as G
    assert G
except ImportError:
    from common import shared as G

G.__VERSION__ = '0.11'
G.__PLUGIN_VERSION__ = PLUGIN_VERSION
