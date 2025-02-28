Question: The left image includes a TV and a black rectangular, horizontal media storage unit, and the right image shows a TV mounted on a flat whitish surface that is not an actual wall.

Reference Answer: True

Left image URL: http://www.ikea.com/cz/cs/images/products/besta-tv-ulozna-sestava-se-skl-dvirky__0343542_PE536154_S4.JPG

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/29/c3/de/29c3dea7af7cf3bb033d0475b299ca58.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The left image includes a TV and a black rectangular, horizontal media storage unit, and the right image shows a TV mounted on a flat whitish surface that is not an actual wall.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left image includes a TV and a black rectangular, horizontal media storage unit, and the right image shows a TV mounted on a flat whitish surface that is not an actual wall.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

