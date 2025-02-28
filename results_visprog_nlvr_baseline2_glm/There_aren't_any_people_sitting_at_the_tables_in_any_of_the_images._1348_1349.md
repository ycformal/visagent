Question: There aren't any people sitting at the tables in any of the images.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/0c/c9/21/0cc921655bc5428363d149aced6e0204--restaurant-interior-design-restaurant-ideas.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/97/d4/4a/97d44a1634d252493093870568212a25.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There aren't any people sitting at the tables in any of the images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There aren't any people sitting at the tables in any of the images.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

