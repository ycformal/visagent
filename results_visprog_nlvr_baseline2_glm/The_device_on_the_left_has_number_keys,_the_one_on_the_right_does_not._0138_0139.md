Question: The device on the left has number keys, the one on the right does not.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/98/f0/bb/98f0bb17ce283117b40d99d5bd9476ee--old-phone-the-evolution.jpg

Right image URL: https://i.pinimg.com/736x/e1/8f/78/e18f7893c614ebab4217f45a1cc53051--unlocked-phones-cell-phone-accessories.jpg

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

