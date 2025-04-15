I developed a Voice Assistant project named "Jarvis", implementing key functionalities using Python:

• Speech Recognition & Text-to-Speech – Integrated `speech_recognition` (`recognize_google()`) for processing voice commands and `pyttsx3` (`speak()`) for real-time text-to-speech conversion.
• Secure Access & User Authentication – Implemented password protection at startup using file handling (`open()`, `read()`, `write()`) for enhanced security.
• Task Automation – Enabled hands-free control using `pyautogui` (`press()`, `typewrite()`) to open applications, manage files, schedule tasks, set alarms (`alarm()`), take screenshots (`screenshot()`), and retrieve news & weather updates (`requests.get()`, `BeautifulSoup`).
• System Control – Designed voice commands for volume adjustment (`volumeup()`, `volumedown()`), system shutdown (`os.system()`), and note-taking with memory recall (`open()`, `write()`, `read()`).
• Web Integration – Integrated with Google, YouTube, and Wikipedia using `webbrowser.open()` and custom search functions (`searchGoogle()`, `searchYoutube()`, `searchWikipedia()`).
• Focus Mode & Productivity Tools – Developed a dedicated focus mode (`os.startfile(FocusMode.py)`), translation service (`translategl()`), and automated messaging (`sendMessage()`).
• Interactive Features – Incorporated gameplay (`game_play()`), media controls (`pyautogui.press('k', 'm')`), and live internet speed testing (`Speedtest.upload()`, `Speedtest.download()`).
• External Script Integration – Optimized real-time execution of various tasks using modular external scripts (`os.startfile()`).

This project enhanced my expertise in Python programming, automation, AI-driven voice interfaces, and interactive system development, demonstrating my ability to create smart, voice-controlled applications.


• Speech Recognition & Text-to-Speech – recognize_google(), speak()
• Secure Access & User Authentication – open(), read(), write()
• Task Automation – press(), typewrite(), alarm(), screenshot(), requests.get(), BeautifulSoup()
• System Control – volumeup(), volumedown(), os.system(), open(), write(), read()
• Web Integration – webbrowser.open(), searchGoogle(), searchYoutube(), searchWikipedia()
• Focus Mode & Productivity Tools – os.startfile(FocusMode.py), translategl(), sendMessage()
• Interactive Features – game_play(), pyautogui.press('k', 'm'), Speedtest.upload(), Speedtest.download()
• External Script Integration – os.startfile()