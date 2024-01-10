from machine import Pin, ADC, I2C
import ssd1306
import time

# Configurarea pinilor pentru senzorul de puls si ecranul OLED
pulse_sensor_pin = 33  
oled_sda_pin = 19
oled_scl_pin = 18

# Initializare ADC pentru senzorul de puls
adc = ADC(Pin(pulse_sensor_pin))
adc.atten(ADC.ATTN_11DB)  # Setam atenuarea la 11dB pentru domeniul maxim de tensiune de 3.3V

# Initializare ecran OLED
i2c = I2C(0, sda=Pin(oled_sda_pin), scl=Pin(oled_scl_pin), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

HEART = [
[ 0, 0, 0, 0, 0, 0, 0, 0, 0],
[ 0, 1, 1, 0, 0, 0, 1, 1, 0],
[ 1, 1, 1, 1, 0, 1, 1, 1, 1],
[ 1, 1, 1, 1, 1, 1, 1, 1, 1],
[ 1, 1, 1, 1, 1, 1, 1, 1, 1],
[ 0, 1, 1, 1, 1, 1, 1, 1, 0],
[ 0, 0, 1, 1, 1, 1, 1, 0, 0],
[ 0, 0, 0, 1, 1, 1, 0, 0, 0],
[ 0, 0, 0, 0, 1, 0, 0, 0, 0],
]

def read_pulse():
    # Citire valoare analogica de la senzorul de puls
    pulse_value = adc.read() #o sa citeasca o valoare intre 0-4095

    # Convertire valoare analogica in puls #o persoana poate avea pulsul intre 0-220
    pulse_rate = pulse_value / 18.61 #cum ESP32 citeste o valoare intre 0-4095, 0 va corespunde lui 0, iar 220 lui 4095
                                     #impartim valoarea la 18.61 pentru a afla corespondenta dintre semnal si puls
    return pulse_rate

while True:
    try:  #in caz ca nu merge din cauza unei erori, se va afisa eroarea pe ramura except
        pulse_rate = read_pulse()

        # Golire ecran OLED
        oled.fill(0)

        # Afisare puls pe ecranul OLED
        oled.text("Pulse Rate:", 11, 1)
        oled.text("{} BPM".format(int(pulse_rate)), 0, 11)
        for y, row in enumerate(HEART):
            for x, c in enumerate(row):
                 oled.pixel(x, y, c)
        if(pulse_rate==0):
            oled.text("Mort", 0, 21)
        elif(pulse_rate<50):
            oled.text("Bradicardie", 0, 21)
        elif(pulse_rate<101):
            oled.text("Puls normal", 0, 21)
        elif(pulse_rate<160):
            oled.text("Tahicardie", 0, 21)
        else:
            oled.text("Apelati la 112", 0, 21)
       
        # Afisare pe ecran
        oled.show()

        # Se asteapta 4 secunde inainte de afisarea urmatoare
        time.sleep(4)

    except Exception as e:
        print("Error:", e)