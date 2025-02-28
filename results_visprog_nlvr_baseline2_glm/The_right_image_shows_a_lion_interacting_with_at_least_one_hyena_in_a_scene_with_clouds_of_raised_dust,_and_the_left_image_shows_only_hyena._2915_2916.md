Question: The right image shows a lion interacting with at least one hyena in a scene with clouds of raised dust, and the left image shows only hyena.

Reference Answer: True

Left image URL: https://1.bp.blogspot.com/--hPm7XT98nk/WOU6X3pMrwI/AAAAAAAAhVg/V9UU83VID74VX2LOZepJIykGpYyuO_rwACLcB/s1600/Last_Tan_Blog_0002.JPG

Right image URL: https://3.bp.blogspot.com/-usXU5DCr4-k/VvOvnUl-SiI/AAAAAAAAFrs/V76PQz_4OiY7djFbK0EIJY4wPPQljswhQ/s1600/HYENA%2BMIMAZ.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The right image shows a lion interacting with at least one hyena in a scene with clouds of raised dust, and the left image shows only hyena.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image shows a lion interacting with at least one hyena in a scene with clouds of raised dust, and the left image shows only hyena.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

