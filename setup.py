from setuptools import find_packages, setup

setup(
    name="Multilingual AI Voice Assistant",
    version="0.0.0",
    author="Aman Prajapati",
    author_email="amanprajapati22@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)