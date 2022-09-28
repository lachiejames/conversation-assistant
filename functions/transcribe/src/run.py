import os
from scipy.io import wavfile
from google.cloud import speech
import json
from typing import Any, Union

from flask import Response


def run_transcribe(request_body: Union[Any, None]) -> Response:
    file_path = os.path.abspath(os.path.join(__file__, "..", "..", "assets", "test2.wav"))
    transcription = transcribe_file(file_path)

    return Response(
        response=json.dumps({"body": transcription}),
        status=200,
        headers={
            "Content-Type": "application/json",
        },
    )


def transcribe_file(speech_file: str) -> str:
    """Transcribe the given audio file asynchronously."""
    samplerate, _ = wavfile.read(speech_file)

    client = speech.SpeechClient()

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    """
     Note that transcription is limited to a 60 seconds audio file.
     Use a GCS file for audio longer than 1 minute.
    """
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
    # # Each result is for a consecutive portion of the audio. Iterate through
    # # them to get the transcripts for the entire audio file.
    # for result in response.results:
    #     # The first alternative is the most likely one for this portion.
    #     print("Transcript: {}".format(result.alternatives[0].transcript))
    #     print("Confidence: {}".format(result.alternatives[0].confidence))

