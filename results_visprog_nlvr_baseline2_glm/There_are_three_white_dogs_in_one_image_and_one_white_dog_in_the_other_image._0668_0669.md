Question: There are three white dogs in one image and one white dog in the other image.

Reference Answer: True

Left image URL: https://78.media.tumblr.com/18990ed05cb86e58bd4378defdc31346/tumblr_o0trfsU20k1r9ged7o1_500.jpg

Right image URL: https://i.pinimg.com/564x/b7/1a/72/b71a72d856499c2320e3d9504b749fde--samoyed-puppies-for-sale-samoyed-dogs.jpg

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

