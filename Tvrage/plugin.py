###
# Copyright (c) 2012, staticsafe
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from supybot.i18n import PluginInternationalization, internationalizeDocstring

_ = PluginInternationalization('Tvrage')

@internationalizeDocstring
class Tvrage(callbacks.Plugin):
    """Add the help for "@plugin help Tvrage" here
    This should describe *how* to use this plugin."""
    threaded = True


Class = Tvrage


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
