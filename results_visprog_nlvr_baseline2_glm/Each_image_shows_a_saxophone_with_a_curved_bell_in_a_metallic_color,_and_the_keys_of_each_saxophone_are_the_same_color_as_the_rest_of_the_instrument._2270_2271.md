Question: Each image shows a saxophone with a curved bell in a metallic color, and the keys of each saxophone are the same color as the rest of the instrument.

Reference Answer: False

Left image URL: https://i.pinimg.com/236x/cb/74/ff/cb74ffb6a6020a0930c328ef48098cc4--soprano-saxophone-saxophones.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/236x/2f/a3/5a/2fa35ad6616ef267feff948fd8641cdd--dynamic-range-saxophones.jpg

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

