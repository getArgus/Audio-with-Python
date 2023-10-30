# Instale as bibliotecas necessárias:
# pip install gTTS pydub

from gtts import gTTS
from pydub import AudioSegment

def texto_para_audio(texto, arquivo_saida):
    # Crie um objeto gTTS com o texto
    tts = gTTS(texto, lang='pt')  # Usando 'pt' em vez de 'pt-br' para evitar o aviso

    # Salve o arquivo de áudio
    tts.save(arquivo_saida)

if __name__ == "__main__":
    texto = "Este é um exemplo de leitura de texto para um audiobook usando Python."
    arquivo_saida = "exemplo_audio.mp3"

    texto_para_audio(texto, arquivo_saida)
    
    # Converta o arquivo de áudio para um formato compatível com o Google Colab
    audio = AudioSegment.from_mp3(arquivo_saida)
    audio.export("exemplo_audio.mp3", format="mp3")

    print("Agora você pode baixar o arquivo 'exemplo_audio.mp3' e ouvi-lo em seu computador.")
