Question: An image shows an uncapped peachy-pink lipstick with a circle showing the lipstick color in the upper right.

Reference Answer: True

Left image URL: http://www.izzysbeautyshoppe.com/image/PicBB2Df120s502x3.png

Right image URL: https://images-na.ssl-images-amazon.com/images/I/41v-Pfy-yWL.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows an uncapped peachy-pink lipstick with a circle showing the lipstick color in the upper right.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows an uncapped peachy-pink lipstick with a circle showing the lipstick color in the upper right.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

