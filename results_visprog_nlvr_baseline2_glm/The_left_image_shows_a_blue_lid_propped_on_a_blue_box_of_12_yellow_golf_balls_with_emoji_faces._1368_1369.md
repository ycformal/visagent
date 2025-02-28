Question: The left image shows a blue lid propped on a blue box of 12 yellow golf balls with emoji faces.

Reference Answer: True

Left image URL: https://ae01.alicdn.com/kf/HTB1.nvtQXXXXXbwaXXXq6xXFXXXV/12-Pz-1-Scatola-di-Palline-Da-Golf-pallina-da-golf-Emoji-Facce-Divertenti-Novit-bel.jpg_640x640.jpg

Right image URL: https://images-na.ssl-images-amazon.com/images/I/41Rkxvo9WVL.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left image shows a blue lid propped on a blue box of 12 yellow golf balls with emoji faces.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left image shows a blue lid propped on a blue box of 12 yellow golf balls with emoji faces.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

