Question: All of the bottles in the right image are unlabeled.

Reference Answer: True

Left image URL: http://4.bp.blogspot.com/--7Etug3DoOg/VmiZfBGX_cI/AAAAAAAAEwg/jvHfH-9TlKw/s1600/Olive_Oil_Some_Kind_Jam_ebay.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/236x/00/00/9c/00009cdd34713a4001c4db208552e9f2--observational-drawing-painted-bottles.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'All of the bottles in the right image are unlabeled.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All of the bottles in the right image are unlabeled.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

