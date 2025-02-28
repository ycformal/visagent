Question: All of the dogs are standing.

Reference Answer: False

Left image URL: http://upload.wikimedia.org/wikipedia/commons/6/6c/1Dog-rough-collie-portrait.jpg

Right image URL: http://www.ci.chisholm.mn.us/vertical/Sites/%7B89A03091-259E-44A3-B82B-4ACB22D45D19%7D/uploads/%7B465ADE1D-55DE-4C15-BFDE-7207087E4B6D%7D.JPG

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
ANSWER0=VQA(image=IMAGE,question="Is 'All of the dogs are standing.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All of the dogs are standing.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

