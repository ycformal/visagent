Question: The left and right image contains the same number bowls with cooked broccoli.

Reference Answer: True

Left image URL: https://qph.fs.quoracdn.net/main-qimg-20ff2892e6a907e1cb637071e01ccd41-c

Right image URL: http://media2.intoday.in/indiatoday/images/stories/2016October/smelly2-korneva_102516074032.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains the same number bowls with cooked broccoli.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains the same number bowls with cooked broccoli.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

