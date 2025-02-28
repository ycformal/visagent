Question: Each image includes a straight black instrument, but one image also includes a gold-colored saxophone with curved mouthpiece and bell end.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/99/1e/e7/991ee7504a5c62753c3ef72934429bd0.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/64/5c/e8/645ce8f9abed05d0d35baf30395577d2.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image includes a straight black instrument, but one image also includes a gold-colored saxophone with curved mouthpiece and bell end.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image includes a straight black instrument, but one image also includes a gold-colored saxophone with curved mouthpiece and bell end.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

