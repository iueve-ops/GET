import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pins = [16, 20, 21, 25,26, 17, 27, 22]                                                                                                                                

GPIO.setup(pins, GPIO.OUT)

U = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= U):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {U:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0 
    return int(round((voltage / U*255))

def number_to_dac(number):
    if not (0 <= number <= 255):
        print("Числа вне диапазона")
        return

    binary = [int(bit) for bit in bin (number)[2:].zfill(8)]
    GPIO.output(pins, binary)


try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах:"))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы не ввели число. попробуйте ещё раз\n")

finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()