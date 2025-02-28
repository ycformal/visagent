Question: The right image contains two dogs wearing life vests.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/2R7bLu7eQ7E/maxresdefault.jpg

Right image URL: https://i.pinimg.com/736x/df/8c/0d/df8c0dd6b7461ed9412952a0e2a046d5--vitamin-funny-pugs.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image contains two dogs wearing life vests.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image contains two dogs wearing life vests.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

