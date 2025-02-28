Question: The puppy on the right is reclining with outstretched front paws, and the dog on the left has a body part propped on something.

Reference Answer: False

Left image URL: https://static8.depositphotos.com/1003131/1021/i/950/depositphotos_10214337-stock-photo-yellow-lab-puppy-in-the.jpg

Right image URL: https://i.ytimg.com/vi/Z_q7-syQcpo/hqdefault.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The puppy on the right is reclining with outstretched front paws, and the dog on the left has a body part propped on something.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The puppy on the right is reclining with outstretched front paws, and the dog on the left has a body part propped on something.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

