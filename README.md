# Conversation Assistant

Helping you find the right words.

# So whats the plan here?

Where will the audio be recorded?

- On the Android microphone

Where will speech to text take place?

- In Google Cloud, since it's the only way to support identifying speakers

Should it use a stream or record and send a file?

- A stream would be pretty cool, but might take some work to implement
- Ideally the messages and text would be showing up in real time as they are recognised
- I won't have to worry about the 1 word at a time thing. Just send an update upon final phrase recognition.

Well how do I set up a stream between android and GCP?

- For Android, I can use a HTTP post stream with OkHTTP
- I will send the audio chunks and receive text/speaker
- For server side, can this just be a function? Maybe people will want to go for longer than 15 minutes? Not necesserally a requirement, but a consideration
- Can functions even handle streaming data?
- Oh wait, all I'm doing is receiving audio chunks on the backend right? Do I even need streaming here? Well yeah because I want to get the updates in real time, so it has to be streaming

So maybe I need a separate cloud function that:

- Accepts audio chunks as input
- Responds with list of messages including text + speaker
- Android app can then use this to generate a suggestion when the button is pressed

Ooh this page shows a working example of streaming with GCP speech to text directly from Android
https://medium.com/@srinathsingh007/android-speech-to-text-using-google-cloud-api-58a89fa1bfaa
Ah nevermind it doesn't actually work lol, and there's no github.

Do I actually need the backend thing here?  I reckon it will be much more performant to do it from the Android device.  I'm going to try out this guys solution and see where that gets me.

Let's try something simpler.  Let's aim to set up a streaming connection from android to local flask.  What do we need?

- Okhttp stream - https://square.github.io/okhttp/recipes/#post-streaming-kt-java
- flask running

Okay that's done, I can now have 2-way audio streaming between the browser and flask

Now how can we do the same with Android?

Or maybe we should see how to return something from the endpoint first...

Maybe I'll be better off just recording an audio file on Android and uploading that for now?

If I'm doing that I may as well set up that lambda now.