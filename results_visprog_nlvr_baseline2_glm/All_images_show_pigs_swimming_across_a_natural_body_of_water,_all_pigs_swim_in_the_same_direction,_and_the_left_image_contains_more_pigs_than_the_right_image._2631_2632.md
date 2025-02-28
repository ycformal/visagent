Question: All images show pigs swimming across a natural body of water, all pigs swim in the same direction, and the left image contains more pigs than the right image.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/92/5a/fe/925afe9ea97f38f2a11d020c1fa403b1--sardegna-italia-sardinia-italy.jpg

Right image URL: https://i.ytimg.com/vi/srPjtXWknZk/hqdefault.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'All images show pigs swimming across a natural body of water, all pigs swim in the same direction, and the left image contains more pigs than the right image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All images show pigs swimming across a natural body of water, all pigs swim in the same direction, and the left image contains more pigs than the right image.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

