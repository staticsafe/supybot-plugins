###
# Copyright (c) 2013, staticsafe
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import pythonwhois
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Whois')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

class Whois(callbacks.Plugin):
    """Add the help for "@plugin help Whois" here
    This should describe *how* to use this plugin."""
    threaded = True


Class = Whois


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
