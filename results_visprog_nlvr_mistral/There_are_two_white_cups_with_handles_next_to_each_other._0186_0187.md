Question: There are two white cups with handles next to each other.

Reference Answer: False

Left image URL: https://i.ebayimg.com/images/g/d8cAAOSw4GVYUrLW/s-l300.jpg

Right image URL: https://img0.etsystatic.com/160/0/13290615/il_340x270.1108380758_ha22.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='How many white cups with handles are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many white cups with handles are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} == 2')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: Runtime error: can only concatenate str (not "int") to str

