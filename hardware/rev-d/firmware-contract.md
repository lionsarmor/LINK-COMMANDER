# Rev D firmware interface and acceptance tests

No working bridge firmware is included yet. This file specifies what the
next implementation must do; it is not a claim that two-port USB or PS/2
behavior has been tested.

## Hardware interface

| GPIO | Function |
|---|---|
| GP0 / GP1 | Keyboard USB D+ / D− |
| GP2 / GP3 | Mouse USB D+ / D− |
| GP8 / GP9 | Keyboard DATA drive / non-inverted sense |
| GP10 / GP11 | Keyboard CLOCK drive / non-inverted sense |
| GP12 / GP13 | Mouse DATA drive / non-inverted sense |
| GP14 / GP15 | Mouse CLOCK drive / non-inverted sense |

Unused: GP4-7 and GP26-29. GP16 is the module's onboard LED. There is no
RUN_ENABLE or gamepad shift-register interface. U1 /EN1 and /EN2 are grounded.
Receiver VBUS is present whenever external power is applied; resetting the
RP2040 does not power-cycle the receivers.

Set all four drive output latches LOW before enabling them as outputs.
Enable the four sense inputs and GPIO hysteresis, with internal pulls off.
A HIGH drive pulls its PS/2 line LOW; a LOW drive releases it. A HIGH sense
means the cable line is HIGH. This reverses Rev C's sense interpretation.
Do not drive a PS/2 line HIGH electrically: only Q1-Q4 pull LOW.

## USB host

Use a deliberate two-root-port configuration with the port pair assignments
above. Configure and test both ports; wiring two GPIO pairs does not by
itself implement a USB host. The module's native USB-C remains available
for programming/debugging with JP1 removed.

[Pico-PIO-USB](https://github.com/sekigon-gonnoc/Pico-PIO-USB) is the proposed
host backend. Pin a tested commit and document its supported system clock,
PIO/state-machine allocation and timing requirements. Use its supported
low/full-speed host configuration; this design is not a high-speed USB host.
Make sure the external 15 kΩ data pulldowns are not unintentionally doubled
by internal GPIO pulldowns left enabled by the host configuration.

Start with ordinary USB HID keyboards and mice. Parse report descriptors
and report IDs for composite receivers; do not assume every receiver sends
only the simplest boot report. Maintain key-release state, modifier state,
mouse movement and button state. Test disconnect/reconnect, simultaneous
traffic and unsupported-device handling. There is no gamepad/XInput driver
in the Rev D scope.

## PS/2 device behavior

The adapter emulates a keyboard and a mouse toward the X16. Implement
separate device state machines and queues, including clock generation,
start/data/odd-parity/stop framing, host clock inhibit, host request-to-send,
acknowledgments and command response timing. Read the real sense inputs
while driving so the host can inhibit or take control of the bus.

For the keyboard, implement the X16-compatible scan-code behavior, including
make/break codes, modifiers, extended keys, reset/self-test, identification,
scan enable/disable, LEDs, typematic commands and the relevant scan-set
commands. Translation must follow the USB HID usage meaning, not the
numerical USB usage byte as a PS/2 scan code.

For the mouse, implement reset/self-test, identification, enable/disable,
stream/remote behavior, read-data, sample-rate/resolution/scaling commands
as required by the host, and correctly signed movement/button packets.
Begin with a basic PS/2 mouse identity and packet format; negotiate and
implement any extensions before advertising them. Verify the exact X16
firmware's initialization sequence on the test fixture.

## Acceptance gates

1. **GPIO fixture:** verify drive/sense polarity, low levels, released high
   levels, line rise time, and power-on/off combinations on all four lines.
2. **USB only:** print decoded keyboard and mouse reports while exercising
   both ports; include wired devices and the selected wireless receivers.
3. **PS/2 fixture:** test reset, ACK/resend behavior, parity, host inhibit,
   host commands, keyboard releases and signed mouse motion/overflow.
4. **Combined fixture:** sustain keyboard repeats and mouse motion together;
   verify USB scheduling does not break PS/2 timing or lose releases.
5. **X16:** after cable continuity and electrical checks, test keyboard first,
   then mouse, then both. Record board/ROM versions, receiver IDs and results.

Receiver compatibility remains a tested list. “2.4 GHz” describes the radio
link, not a guarantee of a particular USB HID interface.
