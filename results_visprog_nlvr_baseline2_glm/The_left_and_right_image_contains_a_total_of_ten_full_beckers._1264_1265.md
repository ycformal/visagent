Question: The left and right image contains a total of ten full beckers.

Reference Answer: True

Left image URL: https://cdn7.bigcommerce.com/s-ufhcuzfxw9/images/stencil/500x659/products/13063/14109/CE-BEISET__57187.1503517906.jpg?c=2&imbypass=on

Right image URL: https://i.ebayimg.com/00/s/ODAwWDgwMA==/z/XScAAOSw-9RZba3F/$_35.JPG?set_id=8800005007

Original program:

```
Statement: The left and right image contains a total of ten full beckers.
Program:
ANSWER0=VQA(image=LEFT,question='How many full beakers are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many full beakers are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} == 10')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains a total of ten full beckers.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains a total of ten full beckers.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

