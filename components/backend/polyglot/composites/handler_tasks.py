import os
from pathlib import Path

from dotenv import load_dotenv
from faster_whisper import WhisperModel

dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path)

# Выберите модель (tiny, base, small, medium, large-v2/v3)
# 'base' - хороший баланс скорости/качества. 'tiny' - самый быстрый, но менее точный.
model_size = os.getenv("MODEL_SIZE")

# Загрузка модели (первый раз загрузит файлы)
model = WhisperModel(model_size, device="cpu",
                     compute_type="int8")  # или "cuda" для GPU
# device="cpu" для CPU, "cuda" для NVIDIA GPU
# compute_type="int8" для более быстрой работы на CPU

# audio_file = "voice.m4a"  # Укажите ваш аудиофайл
