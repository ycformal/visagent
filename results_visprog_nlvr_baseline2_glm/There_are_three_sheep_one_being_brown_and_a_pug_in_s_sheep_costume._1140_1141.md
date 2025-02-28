Question: There are three sheep one being brown and a pug in s sheep costume.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/bd/6f/97/bd6f97dc61e687ed67e9c9dc86257801--odd-couples-funny-animals.jpg

Right image URL: http://www.pupfans.com/wp-content/uploads/sites/734/2016/07/pug-trio.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are three sheep one being brown and a pug in s sheep costume.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are three sheep one being brown and a pug in s sheep costume.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

