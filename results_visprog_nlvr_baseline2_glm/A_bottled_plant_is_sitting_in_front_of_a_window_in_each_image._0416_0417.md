Question: A bottled plant is sitting in front of a window in each image.

Reference Answer: False

Left image URL: https://ae01.alicdn.com/kf/HTB1pvH.RpXXXXXeXVXXq6xXFXXXN/Ev-Dekor-Armut-Kristal-Vazo-Teraryum-Ekici-Konteyner-Topraks-z-Pot-JJ2834.jpg

Right image URL: http://image.dhgate.com/0x0s/f2-albu-g3-M01-BD-E9-rBVaHVR5TCOAT9enAAJSKWpnlL4298.jpg/2pcs-fruit-shape-flower-glass-vase-transparent.jpg

Original program:

```
Statement: A bottled plant is sitting in front of a window in each image.
Program:
ANSWER0=VQA(image=LEFT,question='Is there a bottled plant sitting in front of a window?')
ANSWER1=VQA(image=RIGHT,question='Is there a bottled plant sitting in front of a window?')
ANSWER2=EVAL(expr='{ANSWER0} and {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A bottled plant is sitting in front of a window in each image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A bottled plant is sitting in front of a window in each image.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

