Question: One image shows a stack of two pillows with pointed corners, and the other image shows flat-edged pillows, with one pillow leaning against a pillow that is lying flat.

Reference Answer: False

Left image URL: https://i.pinimg.com/236x/00/c4/6b/00c46b2980ed55862ac35b7e655c01c2--down-pillows-bed-pillows.jpg

Right image URL: https://www.shophiltongardeninn.com/Sweepstakes/images/HGI-fourth_prize.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a stack of two pillows with pointed corners, and the other image shows flat-edged pillows, with one pillow leaning against a pillow that is lying flat.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a stack of two pillows with pointed corners, and the other image shows flat-edged pillows, with one pillow leaning against a pillow that is lying flat.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

