Question: In both images a plant is sprouting out of a vase.

Reference Answer: True

Left image URL: https://usercontent2.hubstatic.com/13306211_f520.jpg

Right image URL: https://i.pinimg.com/736x/5d/ae/bc/5daebce0e5df6945b2a8e81317de8631--recycle-art-reuse.jpg

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

