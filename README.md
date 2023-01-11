# VoiceVox_Roudoku
## 1. Description
This is a reading program for Japanese text files using a VOICEVOX. You can listen to the reading in the selected voice.

## 2. Operational Conditions
- Windows 10/11 64-bit
- Visual Studio Code (VS-Code)
- Python 3.9.4 64-bit
- Browser: Microsoft Edge or Google Chrome
- VOICEVOX Ver. 0.13.4

## 3. Demo
![VoiceVox_Roudoku](https://to-fujita.github.io/Images/Roudoku_001.png "Images for VoiceVox_Roudoku")
![VoiceVox_Roudoku](https://to-fujita.github.io/Images/Roudoku_002.png "Images for VoiceVox_Roudoku")

## 4. Details
I have confirmed this Python Script on the above conditions only. I will show you below how to execute this Python Script.

### 4-1. Preparations
(a) Download and install VOICEVOX  
Please download the [VOICEVOX](https://voicevox.hiroshiba.jp/), and install to your PC. 
  
(b) Download & unzip the file.  
Please download following file and put the unzipped folder under the system path passed.
- VoiceVox_Roudoku: Please download from above "Code".
  
(c) Install some libraries to your Python on VS-Code  
Please install following libraries to your Python system on VS-Code.
- requests: pip install requests
- wave: pip install wave
- Flask: pip install Flask
  
### 4-2. Try to Reading the Text File
(a) Execute the VOICEVOX  
Please execute the VOICEVOX that is downloaded and installed to your PC, before execute this program.   
  
(b) Execute the VoiceVox_Roudoku  
The VoiceVox_Roudoku program is as follow.  
- main_VoiceVox_Roudoku.py  

Please open the above file on the VS Code, then click the "Run" and the "Start Debugging" or the "Run Without Debugging". Wait a few second, it will be displayed "*Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)" at the Terminal. Then, after open the Browser, please input "http://127.0.0.1:5000". You can use the reading for Japanease text files with selected voice character.  

(c) Sample Japanese Text Files  
I prepared some sample text files in the "Sample_Text" folder. Some of them are downloaded form "[青空文庫](http://www.aozora.gr.jp/)", and others are downloaded from "[Sound Emotion](https://sound-emotion.jp/)".
  
## 5. History
2023/01/11: Upload the first version.  
  
## 6. Reference
- [VOICEVOX](https://voicevox.hiroshiba.jp/)
- [VS Code](https://azure.microsoft.com/ja-jp/products/visual-studio-code/)
- [Python](https://www.python.org/)
- [青空文庫](http://www.aozora.gr.jp/)
- [Sound Emotion](https://sound-emotion.jp/)
  
## 7. License
- Programs: MIT
- All of the images and VOICEVOX: Please confirm to each author.
  
## 8. Author
[T. Fujita](https://github.com/To-Fujita)

