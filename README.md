# Text-to-Audio Converter using gTTS and pydub

This Python script provides a simple way to convert text into audio, allowing you to create audiobooks, voiceovers, or other spoken content from text. It utilizes two libraries, gTTS (Google Text-to-Speech) and pydub, to accomplish the task.

## Installation

Before running the script, make sure to install the necessary libraries by running the following command:

```bash
pip install gTTS pydub
```

## Usage

The script defines a function, `texto_para_audio`, which accepts the text you want to convert and the desired output file name. The text is then transformed into an audio file in MP3 format.

Example usage within the script:

```python
if __name__ == "__main__":
    texto = "This is an example of text-to-audio conversion using Python."
    arquivo_saida = "example_audio.mp3"

    texto_para_audio(texto, arquivo_saida)

    # Convert the audio file to a format compatible with Google Colab
    audio = AudioSegment.from_mp3(arquivo_saida)
    audio.export("example_audio.mp3", format="mp3")

    print("You can now download the 'example_audio.mp3' file and listen to it on your computer.")
```

## Notes

- The script uses the 'pt' language code for Portuguese. If you want to use Brazilian Portuguese, replace 'pt' with 'pt-br'.
- You can customize the `texto` variable to contain the text you want to convert into audio.
- The final audio file, 'example_audio.mp3' in this case, is ready for download and listening.

Enjoy using this script for your text-to-audio needs!
