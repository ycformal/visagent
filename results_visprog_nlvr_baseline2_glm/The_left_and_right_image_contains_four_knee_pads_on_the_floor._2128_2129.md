Question: The left and right image contains four knee pads on the floor.

Reference Answer: False

Left image URL: https://images.sidelineswap.com/production/001/199/212/1dd8be7c97163014_small.jpeg

Right image URL: http://www.carlmerritt.com/jokes/monica2.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains four knee pads on the floor.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains four knee pads on the floor.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

