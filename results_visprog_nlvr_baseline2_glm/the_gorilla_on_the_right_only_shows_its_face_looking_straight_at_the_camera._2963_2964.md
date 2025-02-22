Question: the gorilla on the right only shows its face looking straight at the camera.

Reference Answer: True

Left image URL: https://c402277.ssl.cf1.rackcdn.com/photos/1102/images/story_full_width/Gorillas_7.31.2012_Our_closest_cousins_HI_105193.jpg?1345537507

Right image URL: http://images4.fanpop.com/image/photos/14700000/Gorilla-monkeys-14750686-500-375.jpg

Original program:

```
The program provided is a series of steps to evaluate whether certain statements are true or false based on the content of images. Each statement is followed by a program that uses the VQA (Visual Question Answering) function to ask questions about the images and evaluate the answers. The final answer is then returned as the result of the program.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

