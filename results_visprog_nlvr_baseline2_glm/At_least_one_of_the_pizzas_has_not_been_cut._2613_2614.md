Question: At least one of the pizzas has not been cut.

Reference Answer: False

Left image URL: https://img.grouponcdn.com/iam/byQUCktzhCgfqMfEA61h/AZ-2048x1229/v1/c700x420.jpg

Right image URL: http://img.taste.com.au/Qaei25N9/w720-h480-cfill-q80/taste/2016/11/roast-pumpkin-and-chorizo-pizzas-111258-1.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'At least one of the pizzas has not been cut.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one of the pizzas has not been cut.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

