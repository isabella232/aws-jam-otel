import time
import json

import tornado.ioloop
import tornado.web

class PaymentHandler(tornado.web.RequestHandler):
    async def post(self):
        amount_paid = 59.99
        self.write(json.dumps({"amount": amount_pid}))

def make_app():
    return tornado.web.Application([
        (r"/payments/", PaymentHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    port = 8003
    app.listen(port, '0.0.0.0')
    print('starting server on: ', port)
    tornado.ioloop.IOLoop.current().start()
