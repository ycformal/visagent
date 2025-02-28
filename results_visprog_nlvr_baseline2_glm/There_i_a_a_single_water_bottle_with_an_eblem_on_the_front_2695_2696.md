Question: There i a a single water bottle with an eblem on the front

Reference Answer: True

Left image URL: https://rlv.zcache.com/cute_three_toed_sloth_insulated_water_bottle-r7ca722182fb64c08a6cf4f4a1cecd227_zlgl6_324.jpg?rlvnet=1

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/e5/a4/06/e5a40661f04f685a837e8ec1df0f2488.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There i a a single water bottle with an eblem on the front' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There i a a single water bottle with an eblem on the front' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

