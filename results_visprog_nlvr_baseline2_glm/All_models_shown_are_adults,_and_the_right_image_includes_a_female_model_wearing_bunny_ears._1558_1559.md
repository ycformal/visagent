Question: All models shown are adults, and the right image includes a female model wearing bunny ears.

Reference Answer: True

Left image URL: https://dtpmhvbsmffsz.cloudfront.net/posts/2016/12/06/5847273599086ae018028529/m_5847273599086ae01802852a.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB17x2dJpXXXXcOXVXXq6xXFXXXF/New-font-b-Adult-b-font-Unisex-Animal-Onesie-Lovely-Footed-Gray-font-b-Rabbits-b.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

