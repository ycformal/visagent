Question: One image shows a pair of finger-exposing gloves with a panda face on each glove front, and the other image shows one pair of fir-trimmed hand coverings.

Reference Answer: False

Left image URL: https://ae01.alicdn.com/kf/HTB1qhX1SVXXXXb2XVXXq6xXFXXX7/Amaizng-Fashion-Winter-Knitted-Faux-Fur-Fingerless-Gloves-Women-Wrist-Soft-Warm-Mitten-Free-Shipping.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1zbeAIFXXXXcsaXXXq6xXFXXXf/2017-Women-Winter-Warm-Wool-Gloves-Ladies-Rabbit-Fur-Pompom-Mittens-Fingerless-Gloves-guantes-mitones.jpg

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

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a pair of finger-exposing gloves with a panda face on each glove front, and the other image shows one pair of fir-trimmed hand coverings.' true or false?')=<b><span style='color: green;'>fake</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>fake</span></b></div><hr>

Answer: fake

