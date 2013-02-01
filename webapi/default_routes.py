# Copyright (C) 2013 Johnny Vestergaard <jkv@unixcluster.dk>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import bottle
from bottle import get, route, static_file, view, post
import shared_state
import logging

logger = logging.getLogger(__name__)

@post('/login')
def login():
    """Authenticate users"""
    username = post_get('username')
    password = post_get('password')
    logger.info("Authentication attempt with username: [{0}]".format(username))
    shared_state.auth.login(username, password, success_redirect='/admin', fail_redirect='/login')

@route('/login')
@view('login_form')
def login():
    """Show login form"""
    return {}

@route('/logout')
def logout():
    shared_state.auth.logout(success_redirect='/login')

@get('/')
def get_index():
    return static_file('index.html', root=shared_state.static_dir)


@get('/<filename:path>')
def static(filename):
    return static_file(filename, root=shared_state.static_dir)

def post_get(name, default=''):
    return bottle.request.POST.get(name, default).strip()

