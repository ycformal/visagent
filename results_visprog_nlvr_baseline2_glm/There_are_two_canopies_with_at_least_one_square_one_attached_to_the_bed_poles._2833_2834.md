Question: There are two canopies with at least one square one attached to the bed poles.

Reference Answer: False

Left image URL: https://ae01.alicdn.com/kf/HTB1iMgLNFXXXXXiXpXXq6xXFXXXK/1pc-Summer-Magic-Bedroom-Mongolian-Yurt-Mosquito-Net-Mesh-Folded-Home-Travel-Outdoor-Lazy-Bed-Nets.jpg_640x640.jpg

Right image URL: http://i2.cdscdn.com/pdt2/3/0/3/1/700x700/auc3700707200303/rw/moustiquaire-ciel-de-lit-lit-s.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are two canopies with at least one square one attached to the bed poles.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are two canopies with at least one square one attached to the bed poles.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

