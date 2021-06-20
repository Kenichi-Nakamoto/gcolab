from google.cloud import speech
import io

with io.open( "/content/drive/MyDrive/cloudspeech/test.wav", "rb" ) as audio_file:
  content = audio_file.read()

audio = speech.RecognitionAudio( content = content )
config = speech.RecognitionConfig(
    encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz = 16000,
    language_code = "ja-JP"
)

client = speech.SpeechClient()
response = client.recognize( config = config, audio = audio )

for result in response.results:
  print( result.alternatives[0].transcript)         
