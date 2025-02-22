Question: Every shoe is pointing to the right.

Reference Answer: False

Left image URL: https://images-na.ssl-images-amazon.com/images/I/81Z0rNxAvZL._UX395_.jpg

Right image URL: https://cdn.sportsshoes.com/product/A/ADI8914/ADI8914_1000_1.jpg

Original program:

```
The program provided is a series of logical steps to determine if a given statement is true or false based on the information provided in the images. Each statement is evaluated step by step, and the final answer is determined based on the results of these evaluations.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

