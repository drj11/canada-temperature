#!/usr/bin/env python
# SQL API

import json
import sqlite3

# http://webpy.org/org
import web

urls = [
    '/api', 'api'
]

app = web.application(urls, globals())

class api:
    def GET(self):
        co = sqlite3.connect('scraperwiki.db')
        cu = co.cursor()
        cu.execute('select count(distinct(id)) from obs;')
        keys = [k[0] for k in cu.description]
        return json.dumps([dict(zip(keys, row)) for row in cu])

if __name__ == '__main__':
    app.run()
