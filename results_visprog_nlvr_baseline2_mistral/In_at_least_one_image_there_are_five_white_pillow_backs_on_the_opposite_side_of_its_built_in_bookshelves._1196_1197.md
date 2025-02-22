Question: In at least one image there are five white pillow backs on the opposite side of its built in bookshelves.

Reference Answer: False

Left image URL: http://2.bp.blogspot.com/-EJtEOPCJtvk/UeAEUakp6bI/AAAAAAAAUFg/YbHXIVJXzxQ/s1600/Book+Sofa.png

Right image URL: https://ae01.alicdn.com/kf/HTB1XWCMJVXXXXa_aXXXq6xXFXXXT/Free-Shipping-Modern-Design-L-Shaped-Leather-and-Fabric-Corner-Sofa-with-Bookshelf-Storage-Tea-Table.jpg_640x640.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many white pillow backs are on the opposite side of its built in bookshelves?')
ANSWER1=VQA(image=RIGHT,question='How many white pillow backs are on the opposite side of its built in bookshelves?')
ANSWER2=EVAL(expr='{ANSWER0} >= 5 or {ANSWER1} >= 5')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many white pillow backs are on the opposite side of its built in bookshelves?')
ANSWER1=VQA(image=RIGHT,question='How many white pillow backs are on the opposite side of its built in bookshelves?')
ANSWER2=EVAL(expr='{ANSWER0} >= 5 or {ANSWER1} >= 5')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: True

