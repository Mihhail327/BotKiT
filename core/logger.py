import json
from datetime import datetime


def log_event(event: str, level: str = "INFO", **kwargs):
    """
    Логирует событие в формате JSON.
    Пример: log_event("dispatch", command="/hello", user_id=123)
    """
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event,
        "level": level,
        **kwargs
    }
    print(json.dumps(log, ensure_ascii=False))

def log_error(event: str, **kwargs):
    """
    Логирует ошибку как событие уровня ERROR.
    Пример: log_error("dispatch_failed", error="KeyError", command="/start")
    """
    log_event(event, level="ERROR", **kwargs)