class Post:
    def __init__(self, key: str, value: str = None, ttl: int = None) -> None:
        self.key = key
        self.value = value
        self.ttl = ttl

    def __str__(self) -> str:
        return f"{self.key} {self.value} {self.ttl}"

    @property
    def get_key(self) -> str:
        return self.key

    @property
    def get_value(self) -> str:
        return self.value

    @property
    def get_ttl(self) -> int:
        return self.ttl
