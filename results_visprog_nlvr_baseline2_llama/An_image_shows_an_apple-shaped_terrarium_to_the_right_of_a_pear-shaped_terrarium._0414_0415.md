Question: An image shows an apple-shaped terrarium to the right of a pear-shaped terrarium.

Reference Answer: True

Left image URL: https://ae01.alicdn.com/kf/HTB1yV.4HFXXXXXpXFXXq6xXFXXXg/Apel-transparan-mutiara-vas-kaca-Hidroponik-meja-vas-Dekorasi-rumah.jpg_640x640.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1_hX2OVXXXXXiaVXXq6xXFXXXl/YENI-Ev-Dekor-Armut-Kristal-Vazo-Teraryum-Ekici-Konteyner-Topraks%C4%B1z-Pot.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Does the image show an apple-shaped terrarium to the right of a pear-shaped terrarium?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Does the image show an apple-shaped terrarium to the right of a pear-shaped terrarium?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the image show an apple-shaped terrarium to the right of a pear-shaped terrarium?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

