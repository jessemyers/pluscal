from dataclasses import dataclass


@dataclass(frozen=True)
class Print:
    value: str

    def __str__(self) -> str:
        return f"print \"{self.value}\""
