Question: One image shows one primarily yellow train headed leftward, and the other image shows on primarily red train headed rightward.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/6c/5c/e0/6c5ce08e3a64e19812da15eb2ef141fc.jpg

Right image URL: https://c2.staticflickr.com/4/3041/2681570540_0d67ae769d_z.jpg?zz=1

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows one primarily yellow train headed leftward, and the other image shows on primarily red train headed rightward.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows one primarily yellow train headed leftward, and the other image shows on primarily red train headed rightward.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

