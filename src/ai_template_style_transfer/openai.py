from enum import Enum


class StrEnum(str, Enum):
    def __str__(self) -> str:
        return str(self.value)


class Models(StrEnum):
    GPT4 = "gpt-4"
    GPT40613 = "gpt-4-0613"
    GPT432K = "gpt-4-32k"
    GPT432K0613 = "gpt-4-32k-0613"
    GPT35TURBO = "gpt-3.5-turbo"
    GPT35TURBO16K = "gpt-3.5-turbo-16k"
