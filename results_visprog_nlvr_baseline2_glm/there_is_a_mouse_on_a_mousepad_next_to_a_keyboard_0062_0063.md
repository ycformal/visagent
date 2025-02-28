Question: there is a mouse on a mousepad next to a keyboard

Reference Answer: False

Left image URL: http://nerdtechy.com/wp-content/uploads/2016/03/ASUS-MB-MB169B-USB-monitor-1.jpg

Right image URL: https://static1.squarespace.com/static/54791cf3e4b01fb132fd0e4f/t/55d51a93e4b0f5881c80faa9/1440029336261/Dashboard-Text+Alert+-+Placeit+-+iPhone-Laptop.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'there is a mouse on a mousepad next to a keyboard' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'there is a mouse on a mousepad next to a keyboard' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

