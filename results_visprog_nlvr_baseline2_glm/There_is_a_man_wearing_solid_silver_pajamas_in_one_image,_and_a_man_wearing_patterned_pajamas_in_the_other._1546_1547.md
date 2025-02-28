Question: There is a man wearing solid silver pajamas in one image, and a man wearing patterned pajamas in the other.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/6e/ba/e7/6ebae727488bc09f24d0de9fcead8c20--mens-silk-pajamas-silk-sleepwear.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/38/d0/ee/38d0eeedfcf1087d1e948c4f668f3c81.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There is a man wearing solid silver pajamas in one image, and a man wearing patterned pajamas in the other.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a man wearing solid silver pajamas in one image, and a man wearing patterned pajamas in the other.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

