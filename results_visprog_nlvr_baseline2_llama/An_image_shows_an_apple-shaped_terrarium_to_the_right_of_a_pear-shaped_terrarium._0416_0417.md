Question: An image shows an apple-shaped terrarium to the right of a pear-shaped terrarium.

Reference Answer: True

Left image URL: https://ae01.alicdn.com/kf/HTB1pvH.RpXXXXXeXVXXq6xXFXXXN/Ev-Dekor-Armut-Kristal-Vazo-Teraryum-Ekici-Konteyner-Topraks-z-Pot-JJ2834.jpg

Right image URL: http://image.dhgate.com/0x0s/f2-albu-g3-M01-BD-E9-rBVaHVR5TCOAT9enAAJSKWpnlL4298.jpg/2pcs-fruit-shape-flower-glass-vase-transparent.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is the apple-shaped terrarium to the right of the pear-shaped terrarium?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is the apple-shaped terrarium to the right of the pear-shaped terrarium?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the apple-shaped terrarium to the right of the pear-shaped terrarium?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

