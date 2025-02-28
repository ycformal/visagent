Question: There are at most 3 sea lions in the image pair.

Reference Answer: True

Left image URL: http://www.boldtravel.com/wp-content/uploads/2015/07/Galapagos-Los-Tuneles-22-of-71-January-14.jpg

Right image URL: https://i.pinimg.com/474x/22/4f/3e/224f3e9ac517bd6e35f1de4abd17e7f2--karen-oneil-camps.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are at most 3 sea lions in the image pair.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are at most 3 sea lions in the image pair.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

