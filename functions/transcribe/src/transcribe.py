from typing import cast
from google.cloud.speech import (
    RecognitionAudio,
    RecognitionConfig,
    SpeakerDiarizationConfig,
    SpeechClient,
    RecognizeResponse,
    WordInfo,
    SpeechRecognitionAlternative,
)
from scipy.io import wavfile

from .models import Message, TranscribeResponse

DEFAULT_SAMPLE_RATE = 44100
DEFAULT_LANG = "en-US"


def is_my_word(word: WordInfo) -> bool:
    return word.speaker_tag == 0


def get_author(word: WordInfo) -> str:
    return "me" if is_my_word(word) else "them"


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
    response: RecognizeResponse = client.recognize(config=config, audio=audio)

    messages: list[Message] = []

    # First is usually the best
    best_result: SpeechRecognitionAlternative = response.results[0].alternatives[0]
    words: list[WordInfo] = cast(WordInfo, best_result.words)

    my_message = ""
    their_message = ""

    last_speaker = None
    for word in words:
        is_final_word = len(words) == words.index(word)+1
        print(f"len(words)={len(words)}  words.index(word)={words.index(word)}")
        current_speaker = word.speaker_tag
        should_add_message = is_final_word or (last_speaker != None and last_speaker != current_speaker)
        if should_add_message:
            messages.append(
                {
                    "text": my_message if (last_speaker == 0) else their_message,
                    "is_my_message": is_my_word(word),
                },
            )

        if is_my_word(word):
            my_message += f"{word.word} "
        else:
            their_message += f"{word.word} "

        last_speaker = word.speaker_tag

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
