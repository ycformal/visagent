Question: One image includes closed multi-compartment zipper cases shown in six solid-color options.

Reference Answer: False

Left image URL: https://ae01.alicdn.com/kf/HTB1QqipKpXXXXXAXFXXq6xXFXXXZ/Car-three-layers-bookshelf-iron-stationery-box-iron-pencil-box.jpg_200x200.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB15zVlIXXXXXcZXXXXq6xXFXXXr/Fashion-student-stationery-Lovely-Cartoon-Pencil-Box-metal-pencil-cases-Car-tin-pencil-case-kid-gifts.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image includes closed multi-compartment zipper cases shown in six solid-color options.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image includes closed multi-compartment zipper cases shown in six solid-color options.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

