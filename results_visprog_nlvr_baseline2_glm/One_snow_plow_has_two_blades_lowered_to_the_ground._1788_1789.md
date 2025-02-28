Question: One snow plow has two blades lowered to the ground.

Reference Answer: True

Left image URL: https://c2.staticflickr.com/8/7317/10855262874_08d68277f7_b.jpg

Right image URL: https://i.ytimg.com/vi/l6DNGYlipF8/maxresdefault.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One snow plow has two blades lowered to the ground.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One snow plow has two blades lowered to the ground.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

