from pytube import YouTube
import whisper

# Descarga un Video de YouTube, usando Pytube, y lo transcribe, usando OpenAI Whisper.

output_path = "/Users/joaquin/Code/HackathonValencia/"
audio_name =  "download_video.mp4"

def download_video(link):
    yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)  

    try:
        yt.streams.filter(progressive = True, file_extension = "mp4").first().download(output_path = output_path, filename = audio_name)
    except Exception as e:
        print("Some Error!", e)

def transcript_video():
    model = whisper.load_model('base')
    result = model.transcribe(output_path+"/"+audio_name)
    print(result['text'])


link = "https://youtu.be/0cwA6mPyrg0"
download_video(link)
transcript_video()