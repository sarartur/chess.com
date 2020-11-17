class ChessDotComError(Exception):

    __DEFAULT_MESSAGE__ = 'Response not 200'
    __DEFAULT_REFERENCE__ = "https://www.chess.com/news/view/published-data-api"

    def __init__(self, status_code, message = None, reference = None):
        if not message:
            message = ChessDotComError.__DEFAULT_MESSAGE__
        if not reference:
            reference = ChessDotComError.__DEFAULT_REFERENCE__
       
        super().__init__(self, message)
        self.message = message
        self.status_code = status_code
        self.reference = reference


    def __str__(self):
        return (
            f"[MESSAGE] -- {self.message}."
            f"[STATUS CODE] -- {self.status_code} "
            f"[REFERENCE] -- {self.reference} "
        )