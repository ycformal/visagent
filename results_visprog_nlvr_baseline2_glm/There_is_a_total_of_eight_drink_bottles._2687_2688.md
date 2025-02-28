Question: There is a total of eight drink bottles.

Reference Answer: True

Left image URL: https://images-na.ssl-images-amazon.com/images/I/810gXCphFRL._SY500_.jpg

Right image URL: https://www.yourbestdigs.com/wp-content/uploads/2016/09/glass-water-bottles-lineup-2.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is a total of eight drink bottles.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a total of eight drink bottles.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

