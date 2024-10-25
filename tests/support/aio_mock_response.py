class AioMockResponse:
    def __init__(self, text, status, headers=None):
        self._text = text
        self.status = status
        self.headers = headers or {}

    def headers(self):
        return {}

    async def text(self):
        return self._text

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def __aenter__(self):
        return self
