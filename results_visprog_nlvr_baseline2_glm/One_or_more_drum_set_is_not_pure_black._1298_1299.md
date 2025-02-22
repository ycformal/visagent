Question: One or more drum set is not pure black.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/7f/cd/b7/7fcdb7ca974fcf202ea1055b7d030552--drum-throne-music-instruments.jpg

Right image URL: https://i.pinimg.com/736x/1e/d8/0b/1ed80bcde852f7ce1aaf9c0b32d7d889--best-drums-snare-drum.jpg

Original program:

```
The program is not provided, so I cannot determine if the statement is true or false.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

