Question: The device on the left has number keys, the one on the right does not.

Reference Answer: False

Left image URL: http://www.techmaish.com/wp-content/uploads/2011/10/mobile-phone-insurance.jpg

Right image URL: https://i.pinimg.com/736x/f8/f6/68/f8f66813bfdcab5c89028dadc32a4421--mobile-phones-sony.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The device on the left has number keys, the one on the right does not.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The device on the left has number keys, the one on the right does not.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

