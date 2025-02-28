Question: In both images a plant is sprouting out of a vase.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/236x/58/a0/2d/58a02d155f06816e9553ab59952aadaa.jpg

Right image URL: https://i.pinimg.com/236x/a3/55/2d/a3552d902076e0324e4f96ca0f39d9b1--plastic-flowers-flowers-vase.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In both images a plant is sprouting out of a vase.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In both images a plant is sprouting out of a vase.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

