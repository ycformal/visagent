Question: Each image includes at least one young-looking baboon, and one image shows multiple grey-faced baboons with at least one very young baboon.

Reference Answer: False

Left image URL: https://image.slidesharecdn.com/thebaboon-110427131934-phpapp01/95/the-baboon-2-728.jpg?cb=1303910491

Right image URL: http://www.baboonmatters.org.za/wp-content/uploads/2016/09/Living-with-baboons-1.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many young-looking baboons are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many young-looking baboons are in the image?')
ANSWER2=VQA(image=LEFT,question='How many grey-faced baboons are in the image?')
ANSWER3=VQA(image=RIGHT,question='How many grey-faced baboons are in the image?')
ANSWER4=VQA(image=LEFT,question='How many very young baboons are in the image?')
ANSWER5=VQA(image=RIGHT,question='How many very young baboons are in the image?')
ANSWER6=EVAL(expr='{ANSWER0} >= 1 and {ANSWER1} >= 1')
ANSWER7=EVAL(expr='{ANSWER2} >= 1 and {ANSWER4} >= 1')
ANSWER8=EVAL(expr='{ANSWER3} >= 1 and {ANSWER5} >= 1')
ANSWER9=E
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image includes at least one young-looking baboon, and one image shows multiple grey-faced baboons with at least one very young baboon.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image includes at least one young-looking baboon, and one image shows multiple grey-faced baboons with at least one very young baboon.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

