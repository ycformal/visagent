Question: There is a man wearing solid silver pajamas in one image, and a man wearing patterned pajamas in the other.

Reference Answer: False

Left image URL: https://ae01.alicdn.com/kf/HTB1Hp4jQVXXXXa0XFXXq6xXFXXXJ/Luxury-Paisley-Pattern-Kimono-Robes-Men-s-Silk-Satin-Nightgown-Women-Kimono-Dressing-Gown-Bathrobe-Sleepwear.jpg_640x640.jpg

Right image URL: https://i.pinimg.com/736x/4e/7d/ea/4e7dea8925ab85cee90b17b3b461516e--mens-silk-pajamas-silk-sleepwear.jpg

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

