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
from supybot.i18n import PluginInternationalization, internationalizeDocstring
import random

_ = PluginInternationalization('BOFH')

@internationalizeDocstring
class BOFH(callbacks.Plugin):
    """Add the help for "@plugin help BOFH" here
    This should describe *how* to use this plugin."""
    threaded = True

    def bofh(self, irc, msgs, args):
        """<bofh>
        Shows a random BOFH excuse"""

        with open ("excuses.txt", "r") as text:
            excuses = list(text)

        randomexcuse = random.choice(excuses).encode("utf-8")

        irc.reply(randomexcuse.strip('\n'))

Class = BOFH


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
