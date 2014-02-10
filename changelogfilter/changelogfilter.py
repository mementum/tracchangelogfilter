# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Daniel Rodriguez <danjrod@gmail.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
from trac.core import Component, implements
from trac.ticket.api import ITicketChangelogFilter

class ChangelogFilter(Component):
    implements(ITicketChangelogFilter)

    authnamefilter = 'eve'
    vendornamefilter = 'adam'
    fieldfilter = ['comment',]

    # ITicketChangelogFilter methods
    def changelog_filter(self, req, changelog):
        # step backwards to delete without affecting indexes
        self.log.debug('changelog_filter called: changelog len %d' % len(changelog))
	if req.authname.startswith(self.authnamefilter):
            for i in xrange(len(changelog) - 1, -1, -1):
                date, author, field, old, new, permanent = changelog[i]
                if author == self.vendornamefilter and field in self.fieldfilter:
                    self.log.debug('Removing comment %d' % i)
                    del changelog[i]
                else:
                    self.log.debug('Keeping comment %d' % i)
                    pass

        return changelog
