Question: The puppy on the right is reclining with outstretched front paws, and the dog on the left has a body part propped on something.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/44/af/96/44af9662891e57e706a20c3454f323ac--golden-lab-puppies-yellow-lab-puppies.jpg

Right image URL: https://www.thelabradorsite.com/wp-content/uploads/2012/07/yellow-labrador-puppy-696x385.jpg

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

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The puppy on the right is reclining with outstretched front paws, and the dog on the left has a body part propped on something.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

