Question: An identical number of ducks in a wet area can be seen in both images.

Reference Answer: True

Left image URL: http://www.sibleyguides.com/wp-content/uploads/ConcordMA_IMG_4035_2014-11-05_full_w.jpg

Right image URL: http://www.jackhousenaturereserve.co.uk/wp-content/uploads/2014/11/Frozen-Lake-and-Ducks.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'An identical number of ducks in a wet area can be seen in both images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An identical number of ducks in a wet area can be seen in both images.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

