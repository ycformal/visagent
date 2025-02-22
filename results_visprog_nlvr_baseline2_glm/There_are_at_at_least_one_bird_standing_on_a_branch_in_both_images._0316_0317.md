Question: There are at at least one bird standing on a branch in both images.

Reference Answer: False

Left image URL: http://en.academic.ru/pictures/enwiki/65/Ara_glaucogularis_-Cincinnati_Zoo-8.jpg

Right image URL: http://1.bp.blogspot.com/-1-x3ok_6m08/T-23BlUzp6I/AAAAAAAAJhc/UtN02JGBoSs/s1600/Splash%2Bcolour%2BBright%2Bbird%2Bshows%2Bcredible%2Bplumage%2Bdives%2Bhead%2Bfirst%2Binto%2Bbath%2B7.jpg

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

