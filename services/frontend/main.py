import os
import json
import logging
from urllib.parse import urljoin

import falcon
import requests
from wsgiref import simple_server

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('test-logger')
logger.setLevel(logging.DEBUG)

search_srv = os.environ.get('SEARCH_SERVICE_ENDPOINT', 'http://srv-search:8001')
booking_srv = os.environ.get('SEARCH_SERVICE_ENDPOINT', 'http://srv-booking:8002')


class RoomResource(object):
    def book(self, req, resp, room_id):
        result = requests.get(urljoin(search_srv, '/search/{0}'.format(room_id)))
        if not result.ok:
            self.write_error(resp)
            return
        book_result = requests.post(urljoin(booking_srv, '/rooms/{0}/book'.format(room_id)))
        if not book_result.ok:
            self.write_error(resp)
            return
        resp.body = json.dumps({
            'room': result.json(),
            'booking': book_result.json()
        })

    def write_error(self, resp):
        resp.body = json.dumps({
            'error': 'could not book room. something went wrong'
        })
        resp.status = '500 internal server error'

    def on_get(self, req, resp, room_id):
        self.book(req, resp, room_id)

    def on_post(self, req, resp, room_id):
        self.book(req, resp, room_id)


# falcon.API instances are callable WSGI apps
app = falcon.API()

app.add_route('/rooms/{room_id:int}/', RoomResource())
app.add_route('/rooms/{room_id:int}/book', RoomResource())

if __name__ == '__main__':
    port = 8000
    print('starting server: ', port)
    httpd = simple_server.make_server('0.0.0.0', port, app)
    httpd.serve_forever()
