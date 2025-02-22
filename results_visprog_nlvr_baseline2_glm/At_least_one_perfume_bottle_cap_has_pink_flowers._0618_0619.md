Question: At least one perfume bottle cap has pink flowers.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/1a/7c/d6/1a7cd601b5ab57b2c05796c7dcc3fc10--nicki-minaj-pink-friday-perfume-bottles.jpg

Right image URL: https://i.pinimg.com/236x/c6/0d/bf/c60dbf2c4601e51c3400c7ae81243e3e---piece-hairstyles.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

