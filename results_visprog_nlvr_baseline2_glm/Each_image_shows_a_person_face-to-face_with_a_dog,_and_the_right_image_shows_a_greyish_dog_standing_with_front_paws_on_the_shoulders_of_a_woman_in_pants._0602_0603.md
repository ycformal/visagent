Question: Each image shows a person face-to-face with a dog, and the right image shows a greyish dog standing with front paws on the shoulders of a woman in pants.

Reference Answer: True

Left image URL: http://media1.s-nbcnews.com/j/msnbc/Components/Photos/040213/040213_fido_hmed_2p.grid-6x2.jpg

Right image URL: http://puppypictures.org/main.php/d/131952-3/Giant+dog+picture+of+Irish+Wolfhound+dog.PNG

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

