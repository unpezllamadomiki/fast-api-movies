from typing import Dict, Any


class SingletonMeta(type):
    _instances: Dict = {}

    def __call__(cls: "SingletonMeta", *args: Any, **kwargs: Any) -> Dict:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]