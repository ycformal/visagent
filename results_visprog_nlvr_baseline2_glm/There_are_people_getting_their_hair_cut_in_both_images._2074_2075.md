Question: There are people getting their hair cut in both images.

Reference Answer: False

Left image URL: https://i.pinimg.com/originals/84/73/50/8473507442939e5177335863a74e58e4.jpg

Right image URL: https://barbershops.files.wordpress.com/2012/11/barber-shops-in-surrey-1.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are people getting their hair cut in both images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are people getting their hair cut in both images.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

