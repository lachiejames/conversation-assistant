from google.cloud.speech import (
    RecognitionAudio,
    RecognitionConfig,
    SpeakerDiarizationConfig,
    SpeechClient,
)
from scipy.io import wavfile

from .models import Message, TranscribeResponse

DEFAULT_SAMPLE_RATE = 44100
DEFAULT_LANG = "en-US"


def transcribe_data(audio_data: str) -> TranscribeResponse:
    client = SpeechClient()
    audio = RecognitionAudio(content=audio_data)
    config = RecognitionConfig(
        encoding=RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=DEFAULT_SAMPLE_RATE,
        language_code=DEFAULT_LANG,
        enable_automatic_punctuation=True,
        enable_spoken_emojis=True,
        diarization_config=SpeakerDiarizationConfig(
            enable_speaker_diarization=True,
            min_speaker_count=2,
            max_speaker_count=2,
        ),
    )
    response = client.recognize(config=config, audio=audio)

    messages: list[Message] = []
    for result in response.results:
        for alternative in result.alternatives:
            messages.append(
                {
                    "text": alternative.transcript,
                    "is_my_message": alternative.words[0].speaker_tag == 0,
                },
            )

    return {"messages": messages}


def transcribe_file(speech_file: str) -> str:
    samplerate, _ = wavfile.read(speech_file)
    client = SpeechClient()
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = RecognitionAudio(content=content)
    config = RecognitionConfig(
        encoding=RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=samplerate,
        language_code=DEFAULT_LANG,
    )
    response = client.recognize(config=config, audio=audio)

    return response.results[0].alternatives[0].transcript
