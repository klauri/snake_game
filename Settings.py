from pydantic import BaseSettings
from typing import Tuple

class Settings(BaseSettings):
    IMG_SNAKE_PATH: str
    SNAKE_SPEED_FACTOR: float
    SCREEN_WIDTH: int
    SCREEN_HEIGHT: int
    BG_COLOR: Tuple[int, int, int]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'