Question: There are exactly two empty containers.

Reference Answer: True

Left image URL: http://products.lab-suppliers.com/storage/featured_img/kyLnF45zkPWzoDMLgYgcgwukRhOcWfJPzn7FEUY4.jpeg

Right image URL: https://images-na.ssl-images-amazon.com/images/I/318AlK%2BIPaL._SY445_.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are exactly two empty containers.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are exactly two empty containers.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

