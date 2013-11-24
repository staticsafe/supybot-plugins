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
import datetime
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

    def whois(self, irc, msg, args, domain):
        """<whois>
        Returns information about a domain"""
        results = pythonwhois.get_whois(domain, normalized=True)
        creation_date = results["creation_date"].pop()
        creation_date = creation_date.isoformat()
        expiration_date = results["expiration_date"].pop()
        expiration_date = expiration_date.isoformat()
        nameservers = results["nameservers"]
        registrar = results["registrar"].pop()
        registrant = results["contacts"].get("admin").get("name")
        contact_email = results["contacts"].get("admin").get("email")
        formatting = ("The domain {0} was registered on {1} by {2} via {3}, expires on \
{4}, nameservers are {5}, contact e-mail is {6}.".format(domain, \
creation_date, registrant, registrar, expiration_date, nameservers, \
contact_email))
        irc.reply(formatting)
    whois = wrap(whois, ['text'])



Class = Whois


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
