Question: There are three white dogs in one image and one white dog in the other image.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/59/3f/d6/593fd6110e12b0fdd56d71726f97baf3.jpg

Right image URL: https://i.ytimg.com/vi/dLJO80dE4gk/maxresdefault.jpg

Original program:

```
Statement: There are three white dogs in one image and one white dog in the other image.
Program:
ANSWER0=VQA(image=LEFT,question='How many white dogs are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many white dogs are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} == 3 and {ANSWER1} == 1')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are three white dogs in one image and one white dog in the other image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are three white dogs in one image and one white dog in the other image.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

