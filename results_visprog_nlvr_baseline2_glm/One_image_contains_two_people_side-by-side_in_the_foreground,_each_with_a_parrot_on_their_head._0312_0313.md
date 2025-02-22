Question: One image contains two people side-by-side in the foreground, each with a parrot on their head.

Reference Answer: True

Left image URL: http://about-australia.tourstogo.com.au/images/photos/zoomed/206f3c9f.jpg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/09/f7/a3/b4/o-reilly-s-rainforest.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

