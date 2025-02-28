Question: In one of the images, a dog is sleeping on their back in a belly up position.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/cd/d3/48/cdd34800176dad09ddf328e52f291d20.jpg

Right image URL: http://buzzsharer.com/wp-content/uploads/2015/07/basset-hound-sleeps-on-stairs.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In one of the images, a dog is sleeping on their back in a belly up position.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one of the images, a dog is sleeping on their back in a belly up position.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

