Question: One image features one golf ball in the middle surrounded by at least five other balls in a circle-type formation.

Reference Answer: True

Left image URL: https://images-na.ssl-images-amazon.com/images/I/61QtvXkT%2BmL._SY355_.jpg

Right image URL: https://sc01.alicdn.com/kf/HTB1G_oQMVXXXXa6aXXXq6xXFXXXU/222493353/HTB1G_oQMVXXXXa6aXXXq6xXFXXXU.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image features one golf ball in the middle surrounded by at least five other balls in a circle-type formation.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image features one golf ball in the middle surrounded by at least five other balls in a circle-type formation.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

