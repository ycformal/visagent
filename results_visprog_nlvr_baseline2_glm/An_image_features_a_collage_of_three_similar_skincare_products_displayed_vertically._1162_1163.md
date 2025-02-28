Question: An image features a collage of three similar skincare products displayed vertically.

Reference Answer: False

Left image URL: https://images-na.ssl-images-amazon.com/images/I/81gZg7rKzbL._SP500_.jpg

Right image URL: http://ecx.images-amazon.com/images/I/41-tinoIg8L.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'An image features a collage of three similar skincare products displayed vertically.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image features a collage of three similar skincare products displayed vertically.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

