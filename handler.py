import json
import http.server
import urllib.parse

from data import get_data


class HCIRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # API request for data

        if "/data/" in self.path or "/data?" in self.path:
            parsed_request = urllib.parse.urlparse(self.path)
            data = json.dumps(get_data(dict(urllib.parse.parse_qsl(parsed_request[4]))))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(data.encode("utf-8"))
            return

        # Requesting a resource (html, js, css)
        if "/shared/" not in self.path:
            if '/' == self.path:
                self.path = "/index.html"

            if "Mobi" in self.headers['user-agent']:
                # Requested by a mobile device
                self.path = '/mobile%s' % self.path
            else:
                self.path = '/desktop%s' % self.path

        return http.server.SimpleHTTPRequestHandler.do_GET(self)
