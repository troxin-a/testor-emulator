from datetime import datetime
from schemas.query import QueryForServer


class Log(QueryForServer):
    response: bool


class LogHistory(Log):
    id: int
    time_request: datetime
