Question: A yellow helicopter is sitting in the snow.

Reference Answer: False

Left image URL: https://cache-graphicslib.viator.com/graphicslib/thumbs360x240/6251/SITours/juneau-helicopter-tour-and-dogsledding-experience-in-juneau-149231.jpg

Right image URL: http://media.royalcaribbean.com/media/royal/shared_assets/images/shore-excursions/juneau/juneau-helicopter-exploration-and-dog-sledding-adventure-JU43-mosaic.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A yellow helicopter is sitting in the snow.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A yellow helicopter is sitting in the snow.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

