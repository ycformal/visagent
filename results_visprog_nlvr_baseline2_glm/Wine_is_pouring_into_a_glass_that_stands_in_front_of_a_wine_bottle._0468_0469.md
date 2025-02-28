Question: Wine is pouring into a glass that stands in front of a wine bottle.

Reference Answer: True

Left image URL: https://cavegrrl.files.wordpress.com/2014/12/simi-cabernet.jpg

Right image URL: https://4.bp.blogspot.com/-WAy3Xe1EFFE/Vryc7CEqYJI/AAAAAAAAtHQ/fxA_whVe8Mc/s1600/tgi-fridays-half-price-wine-bottles-valentines-day-2016.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Wine is pouring into a glass that stands in front of a wine bottle.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Wine is pouring into a glass that stands in front of a wine bottle.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

