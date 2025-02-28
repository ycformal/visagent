Question: One image shows a diagonally-angled rectangular table with books laid flat on it, and the other image includes at least one rounded white sculptural element in a room with bookshelves on the walls.

Reference Answer: False

Left image URL: http://design-milk.com/images/2012/04/store-moma-books.jpg

Right image URL: https://i.pinimg.com/736x/93/f5/08/93f508b52cf321861e88bd60f2522124--comic-shop-book-stuff.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a diagonally-angled rectangular table with books laid flat on it, and the other image includes at least one rounded white sculptural element in a room with bookshelves on the walls.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a diagonally-angled rectangular table with books laid flat on it, and the other image includes at least one rounded white sculptural element in a room with bookshelves on the walls.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

