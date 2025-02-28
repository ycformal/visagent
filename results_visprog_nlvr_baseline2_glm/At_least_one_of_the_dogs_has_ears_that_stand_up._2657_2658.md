Question: At least one of the dogs has ears that stand up.

Reference Answer: False

Left image URL: http://partitymeminischnauzer.homestead.com/Pande-6.jpg

Right image URL: http://partitymeminischnauzer.homestead.com/Pande-4.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'At least one of the dogs has ears that stand up.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one of the dogs has ears that stand up.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

