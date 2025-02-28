Question: The puppy on the right is reclining with outstretched front paws, and the dog on the left has a body part propped on something.

Reference Answer: False

Left image URL: https://c1.staticflickr.com/5/4002/4698302522_810f1df88f_z.jpg

Right image URL: https://i.ytimg.com/vi/COWcLmn5hqU/maxresdefault.jpg

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

