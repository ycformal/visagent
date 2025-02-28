Question: Both ducks are in water with one facing right and one facing left.

Reference Answer: True

Left image URL: https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Pelecanus_Philippensis.JPG/185px-Pelecanus_Philippensis.JPG

Right image URL: https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Pelecanus_erythrorhynchos_-Tulsa_Zoo%2C_Oklahoma%2C_USA-8c.jpg/170px-Pelecanus_erythrorhynchos_-Tulsa_Zoo%2C_Oklahoma%2C_USA-8c.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Both ducks are in water with one facing right and one facing left.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both ducks are in water with one facing right and one facing left.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

