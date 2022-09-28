import os
from scipy.io import wavfile
from google.cloud import speech
import json
from typing import Any, Union

from flask import Response


def run_transcribe(request_body: Union[Any, None]) -> Response:
    # file_path = os.path.abspath(os.path.join(__file__, "..", "..", "assets", "test2.wav"))
    transcription = transcribe_input(request_body)

    return Response(
        response=json.dumps({"body": transcription}),
        status=200,
        headers={
            "Content-Type": "application/json",
        },
    )

def transcribe_input(input: str) -> str:
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=input)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )
    operation = client.long_running_recognize(config=config, audio=audio)
    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    return response.results[0].alternatives[0].transcript

def transcribe_file(speech_file: str) -> str:
    samplerate, _ = wavfile.read(speech_file)
    client = speech.SpeechClient()
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=samplerate,
        language_code="en-US",
    )
    operation = client.long_running_recognize(config=config, audio=audio)
    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    return response.results[0].alternatives[0].transcript

