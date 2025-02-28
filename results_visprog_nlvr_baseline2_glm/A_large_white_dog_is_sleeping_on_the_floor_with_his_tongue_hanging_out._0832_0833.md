Question: A large white dog is sleeping on the floor with his tongue hanging out.

Reference Answer: False

Left image URL: http://i474.photobucket.com/albums/rr102/rmh12187/pasture10.jpg

Right image URL: http://3.bp.blogspot.com/-YCI7FFUP0Wg/TqY1E2-OkeI/AAAAAAAABuk/nkBRHovnzN8/s1600/sleeping-dog1.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'A large white dog is sleeping on the floor with his tongue hanging out.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A large white dog is sleeping on the floor with his tongue hanging out.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

