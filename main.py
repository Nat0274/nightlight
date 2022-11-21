def on_forever():
    led.set_brightness(255)
    basic.show_leds("""
    # # # # #
    # # # # #
    # # # # #
    # # # # # 
    . . . . .
    """)
basic.forever(on_forever)
