import os
from scipy.io import wavfile
from google.cloud.speech import RecognitionConfig, RecognitionAudio, SpeechClient, SpeakerDiarizationConfig
import json
from typing import Any, Union

from flask import Response

DEFAULT_SAMPLE_RATE = 44100
DEFAULT_LANG = "en-US"


def run_transcribe(request_body: Union[Any, None]) -> Response:
    return Response(
        status=200,
        headers={
            "Content-Type": "application/json",
        },
        response=json.dumps(
            {
                "body": transcribe_input(request_body),
            }
        ),
    )


def transcribe_input(input: str) -> str:
    client = SpeechClient()
    audio = RecognitionAudio(content=input)
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

    return response.results[0].alternatives[0].transcript


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
