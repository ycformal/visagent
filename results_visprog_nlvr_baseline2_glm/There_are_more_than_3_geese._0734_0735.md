Question: There are more than 3 geese.

Reference Answer: False

Left image URL: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Canada_Goose_close_up.jpg/220px-Canada_Goose_close_up.jpg

Right image URL: https://www.gannett-cdn.com/-mm-/ecf62d408cd402f0da1eeac437dcc169fcd17527/c=89-0-1835-1313&r=x408&c=540x405/local/-/media/2017/09/01/WIGroup/Milwaukee/636398685076617066-Early-goose-10.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are more than 3 geese.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are more than 3 geese.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

