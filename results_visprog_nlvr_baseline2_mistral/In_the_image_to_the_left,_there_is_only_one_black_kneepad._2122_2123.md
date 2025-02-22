Question: In the image to the left, there is only one black kneepad.

Reference Answer: False

Left image URL: https://ae01.alicdn.com/kf/HTB1hks1azihSKJjy0Feq6zJtpXas/AOLIKES-2PCS-Lot-Volleyball-Knee-Pads-Thicker-Sponge-Sports-Support-Kneepads-for-Basketball-Dance-joelheira-rodilleras.jpg_640x640.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB18d31mnnI8KJjSszbq6z4KFXav/Aolikes-1-Par-Ni-os-El-stico-Rodilleras-Deportivas-para-Ni-os-Patinaje-Ni-os-Rodillera.jpg_640x640.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many black kneepads are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many black kneepads are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many black kneepads are in the image?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="2 == 1")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

