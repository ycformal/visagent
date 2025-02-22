Question: There are at least 3 pairs of shoes with mismatched colors.

Reference Answer: True

Left image URL: http://img.bleacherreport.net/img/images/photos/002/828/064/ca24bca31337270a178b37f6583b2b10_crop_exact.jpg?w=644&h=430&q=75

Right image URL: https://i.pinimg.com/236x/78/cf/63/78cf63c04d7b389e106af503343ea3bf--cheap-running-shoes-women-running-shoes.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='How many pairs of shoes with mismatched colors are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many pairs of shoes with mismatched colors are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} >= 3')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: Runtime error: can only concatenate str (not "int") to str

