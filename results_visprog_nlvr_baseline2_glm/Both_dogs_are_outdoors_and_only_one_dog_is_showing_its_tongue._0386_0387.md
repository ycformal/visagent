Question: Both dogs are outdoors and only one dog is showing its tongue.

Reference Answer: False

Left image URL: https://cdn.shopify.com/s/files/1/1368/5523/products/corgi_forsale_minicorgi_smallcorgi_111_1024x1024.jpg?v=1479503377

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/64/3f/c3/643fc3cf5bf4242c34897e1719bcb1ba.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Both dogs are outdoors and only one dog is showing its tongue.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both dogs are outdoors and only one dog is showing its tongue.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

