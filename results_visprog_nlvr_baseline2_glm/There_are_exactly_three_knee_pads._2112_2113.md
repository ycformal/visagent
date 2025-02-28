Question: There are exactly three knee pads.

Reference Answer: False

Left image URL: https://images-na.ssl-images-amazon.com/images/I/41BjSVXilCL._SY355_.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1Y217cmtYBeNjSspkq6zU8VXaA/2Pcs-Adults-Children-Kids-Sport-Knee-Pads-Baby-Crawling-Safety-Knee-Support-Gym-Fitness-Crossfit-Tennis.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are exactly three knee pads.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are exactly three knee pads.' true or false?')=<b><span style='color: green;'>fake</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>fake</span></b></div><hr>

Answer: fake

