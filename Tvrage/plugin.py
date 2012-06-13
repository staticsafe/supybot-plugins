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
from tvrage import quickinfo
import tvrage.api
_ = PluginInternationalization('Tvrage')


@internationalizeDocstring
class Tvrage(callbacks.Plugin):
    """Add the help for "@plugin help Tvrage" here
    This should describe *how* to use this plugin."""
    threaded = True

    def genre(self, irc, msg, args, show):
        """<show>
        Shows the genre about TV show"""
        genrereply = tvrage.api.Show(show)
        irc.reply(genrereply.genres)
    genre = wrap(genre, ['text'])

    def nextepisode(self, irc, msg, args, show):
        """<show>
        Shows the next episode of show
        """
        nextreply = quickinfo.fetch(show)
        if 'Next Episode' in nextreply:
            nextinfo = nextreply['Next Episode']
            properformat = ("The next episode of {0} will air on {1} and \
will be episode {2} named {3}.".format(show, nextinfo[2],
nextinfo[0], nextinfo[1]))
            irc.reply(properformat)
        else:
            irc.reply("There is no next episode info for {0}.".format(show))
    nextepisode = wrap(nextepisode, ['text'])

    def latestepisode(self, irc, msg, args, show):
        """<show>
        Shows info on the latest episode of show
        """
        latestreply = quickinfo.fetch(show)
        if 'Latest Episode' in latestreply:
            latestinfo = latestreply['Latest Episode']
            properformat = ("The latest episode of {0} aired on {1} and \
was episode {2} named {3}.".format(show, latestinfo[2],
latestinfo[0], latestinfo[1]))
            irc.reply(properformat)
        else:
            irc.reply(("There is no latest episode info available for \
{0}.".format(show)))
    latestepisode = wrap(latestepisode, ['text'])

Class = Tvrage

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
