Question: There is one kneepad worn by a human in each image.

Reference Answer: True

Left image URL: https://images-na.ssl-images-amazon.com/images/I/61rNUEN3IBL._SY450_.jpg

Right image URL: https://i.pinimg.com/236x/1f/4a/56/1f4a56b8ebb70f463cde3e7de5e5a2b4--knee-cap-knee-brace.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There is one kneepad worn by a human in each image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is one kneepad worn by a human in each image.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

