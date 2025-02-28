Question: Each image shows one panda grasping a bamboo stalk and chewing on part of it.

Reference Answer: False

Left image URL: https://polydidacticism.files.wordpress.com/2015/03/pan-porn.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/60/e1/ce/60e1ce085d86fb4dfc28c3bee6840de8.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows one panda grasping a bamboo stalk and chewing on part of it.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows one panda grasping a bamboo stalk and chewing on part of it.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

