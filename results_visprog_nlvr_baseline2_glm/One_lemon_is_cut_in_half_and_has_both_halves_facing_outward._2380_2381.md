Question: One lemon is cut in half and has both halves facing outward.

Reference Answer: True

Left image URL: https://josepomez.files.wordpress.com/2017/05/los-dos-limones-gordos-y-la-rosa-butano.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/3a/f1/7a/3af17a4ba665afa526c6e2eaa5a49f4d.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One lemon is cut in half and has both halves facing outward.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One lemon is cut in half and has both halves facing outward.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

