from dataclasses import dataclass


@dataclass(frozen=True)
class Id:
    value: str

    def __str__(self) -> str:
        return self.value
