Question: There are children standing by a door.

Reference Answer: False

Left image URL: http://1.bp.blogspot.com/-mbDs7Cj0M9w/U1AEsegXGEI/AAAAAAAANzM/fjCNanRsiks/s1600/Mylee's+Kindergarten+program+025.JPG

Right image URL: http://4.bp.blogspot.com/-TbN4sp75ezY/U1ACLo2F_7I/AAAAAAAANyM/tW_C1gFwKXw/s1600/Mylee's+Kindergarten+program+026.JPG

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are children standing by a door.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are children standing by a door.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

