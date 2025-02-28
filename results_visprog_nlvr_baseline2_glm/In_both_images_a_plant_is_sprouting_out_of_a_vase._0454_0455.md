Question: In both images a plant is sprouting out of a vase.

Reference Answer: False

Left image URL: http://lh6.ggpht.com/-T1CQtXPQrFw/UFtxzZ_p5UI/AAAAAAAAK1Y/YtSnfcFPIeE/IMG_9157_thumb%25255B2%25255D.jpg?imgmax=800

Right image URL: http://www.craftberrybush.com/wp-content/uploads/2012/09/IMG_9161.jpg

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

