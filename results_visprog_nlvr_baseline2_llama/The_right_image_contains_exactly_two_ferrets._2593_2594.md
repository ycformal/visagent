Question: The right image contains exactly two ferrets.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/FGuM8YkY0lE/maxresdefault.jpg

Right image URL: http://1.bp.blogspot.com/-xxTUbcQK9ao/Vi0zIXVZO5I/AAAAAAAAA9Q/63qDr4obkE0/s1600/FullSizeRender%2B%25288%2529.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many ferrets are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many ferrets are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many ferrets are in the image?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="2 == 2")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

