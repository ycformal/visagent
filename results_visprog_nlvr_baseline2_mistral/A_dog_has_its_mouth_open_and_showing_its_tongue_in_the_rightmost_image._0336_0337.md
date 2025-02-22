Question: A dog has its mouth open and showing its tongue in the rightmost image.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/736x/0f/75/83/0f7583a000da5d01d232ca7c3da58ef6.jpg

Right image URL: https://i.pinimg.com/736x/8e/ce/ae/8eceaecfd4ec198c143dacbc89289380--fat-puppies-basset-puppies.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Does the dog have its mouth open and showing its tongue?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Does the dog have its mouth open and showing its tongue?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the dog have its mouth open and showing its tongue?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

