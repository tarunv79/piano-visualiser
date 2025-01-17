# Piano-Led-Visualizer

## Overview
This project is a addition to your piano/keyboard playing experience where you can set an led array on top of your digital piano/keyboard and the leds on top of the keys will glow as you press the keys of your piano.
It is an innovative project that combines hardware and software to create a visually stunning LED light show synchronized with your digital keyboard or piano. This project is built using a Raspberry Pi 4B, a WS2812B LED strip, and the MIDI interface of a digital keyboard/piano. The LED strip is placed above the keys of the piano, and each key press lights up the corresponding LED above it. 

The system is designed to be highly configurable, allowing users to set colors, intensity, and dynamic lighting patterns. It is generic and can be extended to work with any digital keyboard or piano, and any LED array with varying density.

## Features
- **Dynamic Key-to-LED Mapping**: The system uses mathematical calculations to map keys to LEDs based on relative positions, LED array length, and the number of LEDs. No hardcoded mappings are required.
- **Dynamic Light Intensity**: The LED intensity changes dynamically based on the velocity of the key press.
- **Configurable Colors and Patterns**: Users can set custom colors, intensity levels, and patterns directly using the piano keys in a dedicated config mode.
- **Firmware Updates**: The Raspberry Pi pulls the latest code updates from the repository when new versions are available.
- **Generic Design**: Compatible with any digital keyboard/piano and any WS2812B LED array of varying density.

## Hardware Requirements
- **Raspberry Pi 4B** (or equivalent)
- **WS2812B LED Strip**
- **Digital Keyboard or Piano** with a MIDI interface
- **MIDI-to-USB Converter** (if required)
- **Power Supply** for Raspberry Pi and LED strip

## Software Requirements
- **Operating System**: Raspberry Pi OS (or any Linux-based OS compatible with Raspberry Pi)
- **Programming Language**: Python
- **Libraries**: 
  - `neopixel` (for controlling WS2812B LEDs)
  - `mido` (for handling MIDI messages)
  - `pygame` (for clocking and event handling)

## Setup Instructions
1. **Hardware Assembly**:
   - Place the WS2812B LED strip above the keys of your digital piano.
   - Connect the MIDI output of your keyboard to the Raspberry Pi using a USB cable or MIDI to USB cable (if needed).
   - Connect the data line of the LED strip to a GPIO pin on the Raspberry Pi (e.g., GPIO 18).
   - Power the Raspberry Pi and the LED strip.

2. **Software Installation**:
   - Clone the repository:
     ```bash
     git clone <repository-url>
     cd piano-visualizer
     ```
   - Install the required Python libraries:
     ```bash
     pip install <lib-name>
     ```

3. **Run the Visualizer**:
   - Start the main script:
     ```bash
     python visualizer_active.py
     ```
   - Press keys on your piano to see the corresponding LEDs light up.

4. **Enable Config Mode**:
   - Use a specific key combination (defined in the documentation) to enter config mode.
   - Set colors, intensity, or patterns directly from the piano keys.

## Customization
- **Key-to-LED Mapping**: Adjust the following configuration variables to match your setup - KEYBOARD_LEN, LOWEST_NOTE_VAL, HIGHEST_NOTE_VAL, REF_VELOCICY, LED_ARRAY_COUNT, FIRST_LED, LAST_LED.
- **Calibration**: Update ERROR, ERR_KEY_NUM and ERR_SHIFT variables to calibrate the leds in case its not synced with keys
- **Dynamic Intensity**: Enable or disable dynamic intensity based on key velocity.
- **Color and Pattern Settings**: Configure custom lighting patterns and colors interactively in config mode.

## Auto-Update Feature
The Raspberry Pi automatically pulls the latest updates from the repository when new versions are available. Ensure your Pi has an active internet connection and `git` is installed.

## Future Enhancements
- Support for additional LED types.
- Integration with popular DAWs for advanced MIDI control.
- Mobile app for remote configuration.

## Contribution
Contributions are welcome! Please open issues or submit pull requests to suggest improvements or report bugs.

## Acknowledgments
- Inspired by the beauty of music and the desire to create immersive visual experiences.
- Special thanks to the open-source community for the amazing libraries and tools used in this project.

---

Happy Visualizing! 🎹✨
