Question: There are exactly two pencil cases next to each other.

Reference Answer: False

Left image URL: https://cdn.notonthehighstreet.com/system/product_images/images/001/957/088/preview_girls-pencil-case.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB18TSBKpXXXXa7XXXXq6xXFXXXf/Korean-school-supplies-stationery-girls-school-pencil-case-kids-girl-pencil-box-bag-students-children-pen.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are exactly two pencil cases next to each other.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are exactly two pencil cases next to each other.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

