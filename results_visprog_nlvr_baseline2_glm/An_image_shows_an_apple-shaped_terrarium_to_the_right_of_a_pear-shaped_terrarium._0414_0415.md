Question: An image shows an apple-shaped terrarium to the right of a pear-shaped terrarium.

Reference Answer: True

Left image URL: https://ae01.alicdn.com/kf/HTB1yV.4HFXXXXXpXFXXq6xXFXXXg/Apel-transparan-mutiara-vas-kaca-Hidroponik-meja-vas-Dekorasi-rumah.jpg_640x640.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1_hX2OVXXXXXiaVXXq6xXFXXXl/YENI-Ev-Dekor-Armut-Kristal-Vazo-Teraryum-Ekici-Konteyner-Topraks%C4%B1z-Pot.jpg

Original program:

```
Statement: An image shows an apple-shaped terrarium to the right of a pear-shaped terrarium.
Program:
ANSWER0=VQA(image=LEFT,question='Is there an apple-shaped terrarium in the image?')
ANSWER1=VQA(image=RIGHT,question='Is there a pear-shaped terrarium in the image?')
ANSWER2=VQA(image=LEFT,question='Is the apple-shaped terrarium to the right of the pear-shaped terrarium?')
ANSWER3=EVAL(expr='{ANSWER0} and {ANSWER1} and {ANSWER2}')
FINAL_ANSWER=RESULT(var=ANSWER3)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows an apple-shaped terrarium to the right of a pear-shaped terrarium.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows an apple-shaped terrarium to the right of a pear-shaped terrarium.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

