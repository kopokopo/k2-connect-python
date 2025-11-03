from k2connect.k2_requests_v2 import K2Requests


class BaseService(K2Requests):
    def __init__(self, base_url, access_token=None):
        super(BaseService, self).__init__(access_token)
        self.base_url = base_url

    def _build_url(self, url_path):
        return self.base_url + url_path

    def query_resource(self, resource_url):
        return self._query_transaction_status(headers=self._headers, query_url=self._build_url(resource_url))
