Question: There is a man wearing solid silver pajamas in one image, and a man wearing patterned pajamas in the other.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/236x/04/81/e3/0481e305ad981b78be25ce913181df20--tom-ford-men-silk-pajamas.jpg

Right image URL: https://i.pinimg.com/736x/26/b2/4f/26b24fafd53f091e575c08677c3413e5--mens-silk-pajamas-pajama-set.jpg

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

