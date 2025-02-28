Question: All of the perfumes in one of the images are sitting on a tray.

Reference Answer: False

Left image URL: http://images5.fanpop.com/image/photos/25000000/Perfume-perfume-the-story-of-a-murderer-25053427-500-332.jpg

Right image URL: https://i.ytimg.com/vi/EDZAuKULjLA/maxresdefault.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'All of the perfumes in one of the images are sitting on a tray.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All of the perfumes in one of the images are sitting on a tray.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

