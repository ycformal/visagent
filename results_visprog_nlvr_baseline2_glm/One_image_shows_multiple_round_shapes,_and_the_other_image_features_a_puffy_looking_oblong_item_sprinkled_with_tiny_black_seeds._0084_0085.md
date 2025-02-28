Question: One image shows multiple round shapes, and the other image features a puffy looking oblong item sprinkled with tiny black seeds.

Reference Answer: False

Left image URL: https://www.maangchi.com/wp-content/uploads/2016/12/balloon-bread-shape.jpg

Right image URL: https://www.maangchi.com/wp-content/uploads/2016/12/gonggalppang-balloon-bread-roll-out.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows multiple round shapes, and the other image features a puffy looking oblong item sprinkled with tiny black seeds.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows multiple round shapes, and the other image features a puffy looking oblong item sprinkled with tiny black seeds.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

