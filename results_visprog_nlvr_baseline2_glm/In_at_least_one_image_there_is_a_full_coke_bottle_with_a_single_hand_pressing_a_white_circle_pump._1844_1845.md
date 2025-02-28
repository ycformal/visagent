Question: In at least one image there is a full coke bottle with a single hand pressing a white circle pump.

Reference Answer: True

Left image URL: https://images-na.ssl-images-amazon.com/images/I/51mLfvvuIIL._SY450_.jpg

Right image URL: http://gaitaobao1.alicdn.com/tfscom/i1/269792369/TB2XemjnVXXXXa7XpXXXXXXXXXX_!!269792369.jpg_310x310.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there is a full coke bottle with a single hand pressing a white circle pump.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there is a full coke bottle with a single hand pressing a white circle pump.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

