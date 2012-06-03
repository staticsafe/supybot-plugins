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
    
    #def show(self, irc, msg, args, query):
    #    """<show>

    #    Shows the information about requested TV show.
    #    """
    #    answer = quickinfo.fetch(query)
    #    irc.reply(answer)
    #show = wrap(show, ['text'])

    def genre(self, irc, msg, args, show):
        """<show>
        Shows the genre about TV show
        """
        genrereply = tvrage.api.Show(show)
        irc.reply(genrereply.genres)
    genre = wrap(genre, ['text'])

    def nextepisode(self, irc, msg, args, show):
        """<show>
        Shows the next episode of show
        """
        nextreply = tvrage.api.Show(show)
        irc.reply(nextreply.next_episode)
    nextepisode = wrap(nextepisode, ['text'])

Class = Tvrage

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
