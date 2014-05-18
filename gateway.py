# -*- coding: utf-8 -*-

'''
	WSGI gateway
'''

import webapp2
import analyzer


application = webapp2.WSGIApplication([
    ('/', analyzer.Landing)
], debug=False)
