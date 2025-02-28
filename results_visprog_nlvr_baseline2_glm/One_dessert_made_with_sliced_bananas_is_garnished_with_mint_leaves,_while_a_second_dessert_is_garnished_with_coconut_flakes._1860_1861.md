Question: One dessert made with sliced bananas is garnished with mint leaves, while a second dessert is garnished with coconut flakes.

Reference Answer: False

Left image URL: http://www.lemonandolives.com/wp-content/uploads/2015/03/banana-and-orange-salad.jpg

Right image URL: https://cookingwithkids.org/wp-content/uploads/2014/11/pineapplebanana.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One dessert made with sliced bananas is garnished with mint leaves, while a second dessert is garnished with coconut flakes.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One dessert made with sliced bananas is garnished with mint leaves, while a second dessert is garnished with coconut flakes.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

