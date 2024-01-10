# Proiect-PY
Heart Rate Monitor
Recomandări de instalare IDE
Pentru o bună funcționare a aplicației, recomandăm utilizarea IDE-ului Thonny versiunea 4.1.4 (Link de instalare: https://thonny.org/).
	Se deschide IDE-ul Thonny, iar din bara de sus se accesează meniul Tools -> Manage Plug-ins, se va deschide o nouă fereastră, iar în bara de search se tastează ”esptool” și se instalează.
	Tot din bara de sus se mai accesează o data meniul Tools -> Options -> Interpreter și se alege MicroPython (ESP32). Pentru a putea rula MicroPython pe ESP32, din aceeași fereastră (meniul Tools -> Options -> Interpreter) se va apăsa pe ”Install or update MicroPython (esptool)” și se vor completa/alege setăile:
•	se bifează caseta Erase all flash before installing (not just the write areas)
•	MicroPython family: ESP32
•	variant Espressif • ESP32/WROOM
•	version 1.22.0
•	se dă click pe Install
Pentru mai multe detalii legate de instalare, consultați următorul link: https://www.youtube.com/watch?v=elBtWZ_fOZU (instalare Thonny + instalare MicroPython pe ESP32)


Recomandări de instalare driver 
Pentru a putea folosi ecranul OLED, este nevoie de driver-ul SSD1306. Cum Thonny IDE nu are acest driver instalat, se va prelua de pe Github astfel:
•	se accesează acest repository https://github.com/adafruit/micropython-adafruit-ssd1306/blob/master/ssd1306.py
•	se copiază codul pentru ssd1306.py
•	se creează un nou File în Thonny în care se va da Paste codului
•	se salvează File-ul prin selectarea opțiunii Save As și se selectează MicroPython device cu numele ssd1306.py

Codul efectiv al programului, main.py, se va salva pe ESP32 pentru a rula mereu la pornirea ESP-ului.
Pentru mai multe detalii, consultați documentația.
