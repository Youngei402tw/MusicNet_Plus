import os
from pydub import AudioSegment

def convert(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.mp3'):
            mp3_path = os.path.join(folder_path, file_name)
            wav_path = os.path.join(folder_path, file_name.replace('.mp3', '.wav'))
            
            try:
                audio = AudioSegment.from_mp3(mp3_path)

                audio.export(wav_path, format="wav")
                print(f"Converted '{file_name}' to WAV format.")
                
                os.remove(mp3_path)
                print(f"Deleted original MP3 file: '{file_name}'")
            except Exception as e:
                print(f"Error processing '{file_name}': {e}")

folder_path = "/Users/arushiverma/Downloads/Baroque"
convert(folder_path)
