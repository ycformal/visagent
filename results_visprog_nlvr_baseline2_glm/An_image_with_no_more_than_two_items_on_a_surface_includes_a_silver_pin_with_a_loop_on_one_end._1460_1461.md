Question: An image with no more than two items on a surface includes a silver pin with a loop on one end.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/86/72/80/8672803f6cc21b9888f8b0b2e0ede975.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/10/63/50/1063505c6e59be9c751a26da644c6c92.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'An image with no more than two items on a surface includes a silver pin with a loop on one end.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image with no more than two items on a surface includes a silver pin with a loop on one end.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

