Question: There are zebras drinking water.

Reference Answer: True

Left image URL: https://wallpapersfun.files.wordpress.com/2011/08/herd-of-zebra-at-watering-place-1.jpg

Right image URL: https://onekindplanet.org/wp-content/uploads/2016/09/az_zebras.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are zebras drinking water.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAfAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDPnsrN2WC4QeWwJJHGGxUdnbxiJ4jF8yjAEX931qyySrMhjlj2fd2Muep/XtTpFgiuo5LnK7lAPOMY4OB9MV59Nc0bM65uzuVoNG022vTeeVsnBwpkYsQTwBirTrHNGUigWOJyS2Opwefb0ql5zLYi4USBXwPmbJQbsBvyqPUpltGVoRIys5EimTc2R/Xn9RWiik7kttqxZiWwhuwtvE0jYLNIeVU4PU5/D61attMt5rlrtGxjBKnIwfas4amiJFJjPm9Eb+DrhePYfyqTT3uru989pisIRgpC8up7fgRjP1qKiVm09RwbvqdJAEOqWaZGRMpHPXmtyw1/S9SvZbK3uB9piJBikUozY7rn7w9xXHabA99qsYaZlmDY3r0jJyAcdD9Ktazotjpl3YR6bDPPqCYVgm5m3AZDccBsA9O3at8LeEGZ1rSkjc8Q6s1nJFa2k6x3P+sPyq4IHRWB559R2FV9O8Y2txcpb30Udo0hxHIsm6Mk9FJIGCe3Y+tcvqd/eXTF7iC4td21ZLgwbHlwDhCSBkde/Hv2qW1n5mqvFdxyxIIxKZG5BTAC8+hzn3P0xW3tJN3RnyJHq0M0FznyJY5cHnYwOK5bxH4pexukg014JpY2xKjjKsf7m4HKng89j+NY0lzHbEhHlCg7VMR7Drg/T1/Wqi3VrJYqyRrM8rEKFG4bs9PUnPrmm6jegKCWp39jexajYQXkQwkyBtpxlfUH3FFeXGSUySKkcjMjlZAAwKsOoI7EUUe1l2HyLuX1t7xoy13A0ckTfMGcER+5x07YHvmrcMUWsQymVHCwAKOSOT1OfwFeoP4Y065aRjHt8zHmFTjfxgZ9eAKy9U8Do0EaabMlvtkDsGXO72PtWPJZWS0K5ru7PNNL0l7mxnhupj5TOURox83ODyew9vUmtEw2Z0sRrCskwJVlZOhBIY/1/Gunv/B2px21lFA1vNJGriYElFlJPBx7Zq1d+ENQ+wpLHLE1yFBaAj92Gxg4OfQnGadugrnnF/osZRZEnzK0gDIRgAnoBitSxhuYza2SyxRszbEwMjjrwetdTpHhC/i1Ca+uIUjj8tlEKy7h0OOv+elULbwrfzQtcLaQRTwmT7M8su4qWAG4Y6EHkfWodNMtTZRS7fS9btrdxEITKGaUAj65HqPX3rettTsba9nuXuxI0rEx5HKA43D9FH0Ue9c9rmna1a6Hq2oTQxedb27y+cs3+rIAwQMfNz2968cPjPxCSM6k/HT5E/wqqcZRWhM2m9T6LuNa0yffHOyTRSYyjkHd7YPArmYrOwBW4juZbG7S32JIsyyDBZsxsjEhlA2+hz0NeNnxt4iPB1OQj3RP8Kb/AMJlr566ix+saf4Vo+d9iFyo9q0r/hH4nuoLuO1lui/mtLIdyjIAAyT+nvTornTZvFH9orPBbLbKiBIiIw7bec4OGHPUew7GvET4u1wtuN7z/wBcU/8AiaT/AIS3XCc/buf+uSf4UrSD3T2HWbhZ9Vmnto7eRJNpLvMg3HaBxx7UV423ifWWOTfNn/cX/Cii0x3if//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are zebras drinking water.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

