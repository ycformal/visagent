Question: One image features a single left-facing sneaker with yellow laces, and the other image shows a pair of sneakers.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/47/d3/27/47d327f049081e75733a7ce9e594ef16.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/736x/2e/ae/61/2eae613bb39fe7e5f121975d654b97a4.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image features a single left-facing sneaker with yellow laces, and the other image shows a pair of sneakers.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image features a single left-facing sneaker with yellow laces, and the other image shows a pair of sneakers.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

