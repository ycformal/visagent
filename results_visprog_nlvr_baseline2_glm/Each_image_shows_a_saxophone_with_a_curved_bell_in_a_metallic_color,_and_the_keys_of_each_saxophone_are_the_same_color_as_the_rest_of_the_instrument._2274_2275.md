Question: Each image shows a saxophone with a curved bell in a metallic color, and the keys of each saxophone are the same color as the rest of the instrument.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/36/04/51/360451a478b5b9459240edc0e5241d1b--alto-saxophone-saxophones.jpg

Right image URL: http://cdns3.gear4music.com/media/25/254553/1200/preview_1.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows a saxophone with a curved bell in a metallic color, and the keys of each saxophone are the same color as the rest of the instrument.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows a saxophone with a curved bell in a metallic color, and the keys of each saxophone are the same color as the rest of the instrument.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

