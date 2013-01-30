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

_ = PluginInternationalization('Bofh')

@internationalizeDocstring
class Bofh(callbacks.Plugin):
    """Add the help for "@plugin help Bofh" here
    This should describe *how* to use this plugin."""
    threaded = True

    def bofh(self, irc, msg, args):
        """<bofh>
        Shows a random catfact"""

        with open("/home/ss/dev/supybot-plugins/Bofh/excuses.txt", "r") as text:
            excuses = list(text)

        randomexcuses = random.choice(excuses).encode("utf-8")

        irc.reply(randomexcuses.strip('\n'))

Class = Bofh


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
