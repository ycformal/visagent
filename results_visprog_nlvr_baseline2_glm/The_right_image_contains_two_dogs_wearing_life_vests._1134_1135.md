Question: The right image contains two dogs wearing life vests.

Reference Answer: False

Left image URL: http://www.pawbuzz.com/wp-content/uploads/sites/551/2015/04/pug-swimming.jpg

Right image URL: https://static1.squarespace.com/static/594974c0e58c62484cbd42f9/t/598cd46ad2b8579179e9977c/1502401650440/Gwen+The+Black+Pug+Swimming

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image contains two dogs wearing life vests.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image contains two dogs wearing life vests.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

