Question: The fragrance bottle on the left is green with a silver cylindrical cap, and the bottle on the right is an upright rectangle with rounded edges.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/cf/85/5f/cf855fe672bc88d3286bcfadfdbbad16--room--perfume-reviews.jpg

Right image URL: https://images-na.ssl-images-amazon.com/images/I/51XhME3OAiL._SY355_.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The fragrance bottle on the left is green with a silver cylindrical cap, and the bottle on the right is an upright rectangle with rounded edges.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The fragrance bottle on the left is green with a silver cylindrical cap, and the bottle on the right is an upright rectangle with rounded edges.' true or false?')=<b><span style='color: green;'>pure</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>pure</span></b></div><hr>

Answer: pure

