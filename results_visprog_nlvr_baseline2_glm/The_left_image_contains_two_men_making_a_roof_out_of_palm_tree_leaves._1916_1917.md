Question: The left image contains two men making a roof out of palm tree leaves.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/J4vDNphqnYQ/maxresdefault.jpg

Right image URL: http://thatchinginfo.com/wp-content/uploads/2016/07/29b1.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left image contains two men making a roof out of palm tree leaves.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left image contains two men making a roof out of palm tree leaves.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

