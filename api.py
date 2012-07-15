#!/usr/bin/env python
# SQL API

import json
import sqlite3

# http://webpy.org/org
import web

urls = [
    '/debug', 'debug',
    '/size', 'size',
    '/sql', 'sql'
]

app = web.application(urls, globals())

# from scraperwiki datalib.py
def authorizer_readonly(action_code, tname, cname, sql_location, trigger):
    """Authorizer function used by the sqlite interface"""

    readonlyops = [ sqlite3.SQLITE_SELECT, sqlite3.SQLITE_READ, sqlite3.SQLITE_DETACH, 31 ]  # 31=SQLITE_FUNCTION missing from library.  codes: http://www.sqlite.org/c3ref/c_alter_table.html
    if action_code in readonlyops:
        return sqlite3.SQLITE_OK

    if action_code == sqlite3.SQLITE_PRAGMA:
        if tname in ["table_info", "index_list", "index_info",
                "page_size", "synchronous"]:     
            return sqlite3.SQLITE_OK

    # SQLite FTS (full text search) requires this permission
    # even when reading, and
    # this doesn't let ordinary queries alter sqlite_master
    # because of PRAGMA writable_schema
    if action_code == sqlite3.SQLITE_UPDATE and tname == "sqlite_master":
        return sqlite3.SQLITE_OK

    return sqlite3.SQLITE_DENY


class sql:
    def GET(self):
        try:
            q = web.input().q
        except AttributeError:
            return json.dumps(dict(error="query parameter q not present"))
        co = sqlite3.connect('scraperwiki.db')
        co.set_authorizer(authorizer_readonly)
        cu = co.cursor()
        try:
            cu.execute(q)
        except sqlite3.Error as e:
            return json.dumps(dict(error='sqlite3.'+repr(e)))
        keys = [k[0] for k in cu.description]
        return json.dumps([dict(zip(keys, row)) for row in cu])

class size:
    def GET(self):
        import os
        p = 'scraperwiki.db'
        r = os.stat(p)
        return json.dumps(dict(path=p, size=r.st_size))
class debug:
    def GET(self):
        return json.dumps(web.input().foo)

if __name__ == '__main__':
    app.run()
