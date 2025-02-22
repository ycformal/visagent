Question: the birds beak if pointing right in the right pic

Reference Answer: True

Left image URL: http://3.bp.blogspot.com/-1kRWlVuyzUo/UCgdWx8gtcI/AAAAAAAADDg/ZS8F9kK8vSM/s1600/11-27-11viera+wetlands+anhinga+drying2.jpg

Right image URL: http://ucanr.edu/blogs/green/blogfiles/26972_original.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is the birds beak pointing right?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is the birds beak pointing right?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the birds beak pointing right?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

