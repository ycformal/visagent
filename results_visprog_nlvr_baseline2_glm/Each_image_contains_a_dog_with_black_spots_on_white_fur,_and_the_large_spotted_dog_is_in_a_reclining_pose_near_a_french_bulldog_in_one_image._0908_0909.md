Question: Each image contains a dog with black spots on white fur, and the large spotted dog is in a reclining pose near a french bulldog in one image.

Reference Answer: True

Left image URL: https://static.wixstatic.com/media/4876ea_17dcb9793e0944f09c897ded3e4f4d78.png_srz_658_997_85_22_0.50_1.20_0.00_png_srz

Right image URL: https://i.pinimg.com/236x/25/36/1b/25361bbd996bf2da3ad643f73f647f60--the-harlequin-cheer.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains a dog with black spots on white fur, and the large spotted dog is in a reclining pose near a french bulldog in one image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains a dog with black spots on white fur, and the large spotted dog is in a reclining pose near a french bulldog in one image.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

