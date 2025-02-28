Question: Each image contains one dog, with the one on the left posed with front paws forward, and the dog on the right showing some teeth.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/91/15/0e/91150e28e52437e27fdadc88db518d5e--shiloh-shepherd-shepherd-puppies.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/17/88/8a/17888afd05bbf43c5b6ec56e07174f6f.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains one dog, with the one on the left posed with front paws forward, and the dog on the right showing some teeth.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains one dog, with the one on the left posed with front paws forward, and the dog on the right showing some teeth.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

