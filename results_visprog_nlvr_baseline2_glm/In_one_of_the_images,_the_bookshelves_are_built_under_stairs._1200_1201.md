Question: In one of the images, the bookshelves are built under stairs.

Reference Answer: True

Left image URL: http://www.urlag.mn/Admin/uploaded/tumblr_m4puzlsc4V1rw7sa3o1_5005717161962015-03-24-13-49[www.urlag.mn].jpg

Right image URL: https://cdn.makespace.com/blog/wp-content/uploads/2016/02/09143843/staircase-book-storage-hack-for-small-apartments.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In one of the images, the bookshelves are built under stairs.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one of the images, the bookshelves are built under stairs.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

