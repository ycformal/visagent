Question: One room has turquoise-blue bookshelves with square compartments, and the other room shows a head-on light-colored bookcase wall that is completely filled with books.

Reference Answer: True

Left image URL: http://www.atticmag.com/wp-content/uploads/2010/05/dec-room-dinroombookcase1-435.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/564x/70/47/a7/7047a72058d201c44eaae9e3d8b1efd9.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One room has turquoise-blue bookshelves with square compartments, and the other room shows a head-on light-colored bookcase wall that is completely filled with books.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One room has turquoise-blue bookshelves with square compartments, and the other room shows a head-on light-colored bookcase wall that is completely filled with books.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

