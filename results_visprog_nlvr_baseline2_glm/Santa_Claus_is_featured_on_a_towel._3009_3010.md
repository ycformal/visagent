Question: Santa Claus is featured on a towel.

Reference Answer: True

Left image URL: https://i.pinimg.com/originals/0b/8c/7a/0b8c7a7afa2ebba79fec331b2f04f922.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1f50bdqmgSKJjSsphq6Ay1VXaP/Christmas-41-66CM-font-b-Cotton-b-font-Face-font-b-Towel-b-font-Hair-Bath.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Santa Claus is featured on a towel.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Santa Claus is featured on a towel.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

