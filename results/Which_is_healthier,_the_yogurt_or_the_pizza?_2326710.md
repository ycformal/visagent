Question: Which is healthier, the yogurt or the pizza?

Reference Answer: The yogurt is healthier than the pizza.

Image path: ./sampled_GQA/2326710.jpg

Chain:

```
VQA(Which is healthier, the yogurt or the pizza?)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Which is healthier, the yogurt or the pizza?')
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Which is healthier, the yogurt or the pizza?')=<b><span style='color: green;'>yoplait</span></b></div><hr>

Answer: yogurt

