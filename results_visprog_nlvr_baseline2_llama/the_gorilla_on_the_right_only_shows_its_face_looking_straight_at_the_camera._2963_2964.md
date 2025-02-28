Question: the gorilla on the right only shows its face looking straight at the camera.

Reference Answer: True

Left image URL: https://c402277.ssl.cf1.rackcdn.com/photos/1102/images/story_full_width/Gorillas_7.31.2012_Our_closest_cousins_HI_105193.jpg?1345537507

Right image URL: http://images4.fanpop.com/image/photos/14700000/Gorilla-monkeys-14750686-500-375.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is the gorilla on the right only showing its face looking straight at the camera?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is the gorilla on the right only showing its face looking straight at the camera?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the gorilla on the right only showing its face looking straight at the camera?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

