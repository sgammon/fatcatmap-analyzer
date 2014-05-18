# -*- coding: utf-8 -*-

'''
  FCM analyzer
'''

import webapp2


class Routine(webapp2.RequestHandler):

  ''' generic handler class that presents an interface for declaring an analyzer routine '''

  pass


class Landing(Routine):

  def get(self):

    ''' handles generic GET '''

    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, webapp2 World!')

