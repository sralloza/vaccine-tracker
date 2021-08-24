from typing import Generator, List, Optional

from pydantic import BaseSettings,validator


class Settings(BaseSettings):
    bot_token: str
    admin_id: int
    other_ids: List[int] = []
    s3_bucket: str
    filter_keyword: Optional[str]

    @property
    def chat_ids(self) -> Generator[int, None, None]:
        yield self.admin_id
        yield from self.other_ids

    @validator("filter_keyword")
    def check_filter_keyword(cls, v):
        if isinstance(v, str):
            v = v.lower()
        return v

settings = Settings()
