Question: Each image shows one red-orange dog with open eyes and a closed mouth.

Reference Answer: True

Left image URL: https://i.pinimg.com/564x/16/8a/09/168a09cf7dc3a84437409300fba16658--wirehaired-vizsla-vizsla-dog.jpg

Right image URL: http://doggies.com/blog/wp-content/uploads/2012/10/V-puppy.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows one red-orange dog with open eyes and a closed mouth.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows one red-orange dog with open eyes and a closed mouth.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

