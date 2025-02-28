Question: One image shows a round bowl containing broccoli florets, with an eating utensil at a diagonal over it.

Reference Answer: False

Left image URL: http://cookingontheside.com/wp-content/uploads/2009/09/Roasted_Broccoli_with_Lemon-580.jpg

Right image URL: http://resize.indiatvnews.com/en/resize/newbucket/715_-/2017/06/broccoli-weight-loss-1497597674.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a round bowl containing broccoli florets, with an eating utensil at a diagonal over it.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a round bowl containing broccoli florets, with an eating utensil at a diagonal over it.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

