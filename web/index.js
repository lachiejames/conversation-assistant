const express = require("express");
const fs = require("fs");
const app = express();

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

app.get("/audio", (req, res) => {
  const range = req.headers.range;
  if (!range) {
    res.status(400).send("Requires Range header");
  }

  const audioPath = "test2.wav";
  const audioSize = fs.statSync(audioPath).size;

  // Parse Range
  // Example: "bytes=32324-"
  const CHUNK_SIZE = 10 ** 6; // 1MB
  const start = Number(range.replace(/\D/g, ""));
  const end = Math.min(start + CHUNK_SIZE, audioSize - 1);

  // Create headers
  const contentLength = end - start + 1;
  const headers = {
    "Content-Range": `bytes ${start}-${end}/${audioSize}`,
    "Accept-Ranges": "bytes",
    "Content-Length": contentLength,
    "Content-Type": "audio/wav",
  };

  // HTTP Status 206 for Partial Content
  res.writeHead(206, headers);

  // create audio read stream for this particular chunk
  const audioStream = fs.createReadStream(audioPath, { start, end });

  // Stream the audio chunk to the client
  audioStream.pipe(res);
});

app.listen(3000, () => {
  console.log("Listening on port 3000");
});
