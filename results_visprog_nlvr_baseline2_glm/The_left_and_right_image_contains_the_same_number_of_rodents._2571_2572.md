Question: The left and right image contains the same number of rodents.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/ZrnmAoLyANg/hqdefault.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/6e/1a/ca/6e1aca09561cbda03655b64ba836a91d.jpg

Original program:

```
The statement is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains the same number of rodents.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains the same number of rodents.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

