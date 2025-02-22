Question: There are two ibex in the left image.

Reference Answer: True

Left image URL: https://i.pinimg.com/originals/f0/b6/db/f0b6db75efc2fac620f9f26c32548163.jpg

Right image URL: https://i.pinimg.com/736x/7d/26/94/7d2694e39a173bc9596eef1809ca1efc--animals-photos-animal-alphabet.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many ibex are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many ibex are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many ibex are in the image?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="2 == 2")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

