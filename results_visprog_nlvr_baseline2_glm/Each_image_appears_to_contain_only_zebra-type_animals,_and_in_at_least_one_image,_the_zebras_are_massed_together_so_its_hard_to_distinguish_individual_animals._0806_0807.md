Question: Each image appears to contain only zebra-type animals, and in at least one image, the zebras are massed together so its hard to distinguish individual animals.

Reference Answer: False

Left image URL: https://store.artwolfe.com/wp-content/uploads/sites/2/2014/11/ZBOOAF1_00042-1024x675.jpg

Right image URL: https://images.fineartamerica.com/images-medium-large-5/grants-zebra-equus-burchelli-boehmi-art-wolfe.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image appears to contain only zebra-type animals, and in at least one image, the zebras are massed together so its hard to distinguish individual animals.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image appears to contain only zebra-type animals, and in at least one image, the zebras are massed together so its hard to distinguish individual animals.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

