Question: One image shows a pair of finger-exposing gloves with a panda face on each glove front, and the other image shows one pair of fir-trimmed hand coverings.

Reference Answer: True

Left image URL: https://ae01.alicdn.com/kf/HTB1n_1oSVXXXXXsXpXXq6xXFXXXb/Amaizng-Fashion-Winter-Knitted-Faux-Fur-Fingerless-Gloves-Women-Wrist-Soft-Warm-Mitten-Free-Shipping.jpg

Right image URL: https://i.pinimg.com/736x/98/01/85/98018585b0460aff1790366777299206--mitten-gloves-mittens.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a pair of finger-exposing gloves with a panda face on each glove front, and the other image shows one pair of fir-trimmed hand coverings.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a pair of finger-exposing gloves with a panda face on each glove front, and the other image shows one pair of fir-trimmed hand coverings.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

