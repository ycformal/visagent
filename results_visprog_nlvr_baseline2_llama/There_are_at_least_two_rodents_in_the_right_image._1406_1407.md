Question: There are at least two rodents in the right image.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/97/50/bf/9750bf76fedfc893fca53fe0cbad9245--smiling-animals-baby-animals.jpg

Right image URL: https://i.pinimg.com/736x/ba/02/95/ba029580fd064f409d9fffab50a185cb--three-little-pigs-cavi.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many rodents are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many rodents are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many rodents are in the image?')=<b><span style='color: green;'>3</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 >= 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="3 >= 2")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

