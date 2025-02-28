Question: There are four skunks.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/qqUEBwgA4cU/maxresdefault.jpg

Right image URL: https://i.pinimg.com/736x/d4/aa/69/d4aa69378c84f24e27fbcd3a3f15556c--baby-skunks-cute-babies.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are four skunks.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are four skunks.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

