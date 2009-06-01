# -*- test-case-name: knoboo.external.twisted.web.test.test_httpauth -*-
# Copyright (c) 2009 Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Implementation of RFC2617: HTTP Digest Authentication

@see: U{http://www.faqs.org/rfcs/rfc2617.html}
"""

from zope.interface import implements
from twisted.cred import credentials
from knoboo.external.twisted.web.iweb import ICredentialFactory

class DigestCredentialFactory(object):
    """
    Wrapper for L{digest.DigestCredentialFactory} that implements the
    L{ICredentialFactory} interface.
    """
    implements(ICredentialFactory)

    scheme = 'digest'

    def __init__(self, algorithm, authenticationRealm):
        """
        Create the digest credential factory that this object wraps.
        """
        self.digest = credentials.DigestCredentialFactory(algorithm,
                                                          authenticationRealm)


    def getChallenge(self, request):
        """
        Generate the challenge for use in the WWW-Authenticate header

        @param request: The L{IRequest} to with access was denied and for the
            response to which this challenge is being generated.

        @return: The C{dict} that can be used to generate a WWW-Authenticate
            header.
        """
        return self.digest.getChallenge(request.getClientIP())


    def decode(self, response, request):
        """
        Create a L{twisted.cred.digest.DigestedCredentials} object from the
        given response and request.

        @see: L{ICredentialFactory.decode}
        """
        return self.digest.decode(response,
                                  request.method,
                                  request.getClientIP())
