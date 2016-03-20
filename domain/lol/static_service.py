# coding=utf-8
import httplib2
import simplejson



class HelloLoL(object):
    def __init__(self):
        self.conn = httplib2.Http()
        self.apiKey = "api_key=dad3cbe4-23a8-419b-984b-8ba98b134928"
        self.url_service = "https://global.api.pvp.net/api/lol/static-data/br/v1.2/champion"
        self.headers = {"Content-type": "application/json", "Accept": "application/json", "Accept-Language": "en-US",
                        "Accept-Charset": "utf-8"}

    def get_champions(self, args):
        try:
            url = self._get_additional_args(args, self.url_service + "?" + self.apiKey)
            response, content = self.conn.request(url, "GET", "", self.headers)
            return simplejson.loads(content.decode("utf-8"))
        except Exception as e:
            raise Exception(e)

    def get_champions_by_id(self, id, args):
        try:
            url = self._get_additional_args(args, self.url_service + "/" + id + "?" + self.apiKey)

            response, content = self.conn.request(url, "GET", "", self.headers)
            return simplejson.loads(content.decode("utf-8"))
        except Exception as e:
            raise Exception(e)

    def _get_additional_args(self, args, url):
        if args:
            for arg in args:
                url += '&' + arg + '=' + args[arg]
            print(url)
        return url
