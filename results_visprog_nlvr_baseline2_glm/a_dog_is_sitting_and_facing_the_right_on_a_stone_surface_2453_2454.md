Question: a dog is sitting and facing the right on a stone surface

Reference Answer: True

Left image URL: http://www.cedarcreekkennels.ca/wp-content/uploads/2013/10/IMG_9636.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/21/76/fd/2176fdd5b2557b3274bd9e245670f6f1.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'a dog is sitting and facing the right on a stone surface' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'a dog is sitting and facing the right on a stone surface' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

