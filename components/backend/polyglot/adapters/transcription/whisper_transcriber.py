from faster_whisper import WhisperModel


class WhisperTranscriber:

    def __init__(self, model: WhisperModel):
        self.model = model

    def transcription(self, audio_file) -> str:

        # Транскрипция
        segments, info = self.model.transcribe(audio_file, beam_size=5)

        print(
            f"Обнаружен язык: {info.language} (вероятность: {info.language_probability:.2f})"
        )

        for segment in segments:
            print(
                f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

        # TODO: вернуть текст
