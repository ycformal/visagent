Question: Which company is the hat from?

Reference Answer: The hat is from adidas.

Image path: ./sampled_GQA/n274905.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Which company is the hat from?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Which company is the hat from?')=<b><span style='color: green;'>adidas</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>adidas</span></b></div><hr>

Answer: adidas
