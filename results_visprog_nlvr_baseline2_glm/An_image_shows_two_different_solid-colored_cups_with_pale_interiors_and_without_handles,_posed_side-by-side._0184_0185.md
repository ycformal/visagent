Question: An image shows two different solid-colored cups with pale interiors and without handles, posed side-by-side.

Reference Answer: True

Left image URL: https://st2.depositphotos.com/1000438/6315/i/950/depositphotos_63153137-stock-photo-two-cups-of-coffee-and.jpg

Right image URL: https://i.pinimg.com/736x/54/92/65/549265722351969b8f0972a9f82b2e89--cozies-egg-cups.jpg

Original program:

```
Statement: An image shows two different solid-colored cups with pale interiors and without handles, posed side-by-side.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows two different solid-colored cups with pale interiors and without handles, posed side-by-side.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows two different solid-colored cups with pale interiors and without handles, posed side-by-side.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

