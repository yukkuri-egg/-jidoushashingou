def on_forever():
    pins.analog_write_pin(AnalogPin.P2, 1023)
    basic.pause(10000)
    pins.analog_write_pin(AnalogPin.P1, 1023)
    basic.pause(3000)
    pins.analog_write_pin(AnalogPin.P0, 1023)
    basic.pause(18000)
basic.forever(on_forever)
