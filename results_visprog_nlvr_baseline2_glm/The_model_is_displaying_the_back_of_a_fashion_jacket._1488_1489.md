Question: The model is displaying the back of a fashion jacket.

Reference Answer: False

Left image URL: http://i.ebayimg.com/00/s/MTYwMFgxMDY4/z/8BsAAOSwu4BVxMre/$_1.JPG?set_id=880000500F

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/27/33/52/2733526ea3529111c1f5ef2b0f41446c.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA0AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDuPGHjjUdI12SwtIPLaNRguwKvnkEDGfbr2rh/jVeXOofDnQrq73CWS/LYZdpA8tuMVeb9oPwo939qPh7UDcYCiUpEWAHbOc1xXxR+Kel+PdFsrGwsLy3kt7nzma4K4I2lccE8800B5YKdQBnoOa77wh8N7jVWS81gvaWWQRH0eQf+yj9amrVhTXNNlwpym7RR0Xwl0C81XSp5bkFLCORjbN0LSFdrEeqj+ddRbfD+5KTwSzBWXBjkxlW65B/Su0sktNKsILa3iWKBF2RIg4GBkCkiebEs927J5ihBEvIQ7QePzPPtXh1pxnJyZ6tJypx5Uzk4/A0sUbteahEYCny4/hPpz1FVtItoQLnTZCGPXkZKg8D6V0us36QMLMxOY1BBYf3iDgcdeMmuW0SRZNVaTBCL8i5PX5e/4KKwckpWibxcnG8i3eotiohjiS2iUM/7pvnwBxn6ntWRcXVxFKwYYcKJGx8wJI4A9uCPxFa2ryFLqQbep67iCAOh/M1jzst7qHkuBEZzsRlQnY4UgZGfQHPWuqktG2YXbkkcnq9yUtVjjkldw7LJIxHztgH5R2AFcpes0qx7LiZpOQ4J4FeoS+ErVVH9p3jYBLGa2G5cE5wfT61ka14D2Qfb9ImN1CfmIOCTnuCK6oVqaegTpTSs3c8rmk3StjnHGT3oouYnhupYpFKsrkEEYPWivRSVjyW3cq1veFfDr+I9Qkt1nEKxpvZtu44yBx+dYNdz8MJRFrd3uTcrWxz+DA/0rGtKUabcdy6MVKolLY73w/4J0fRWFwI2nuU6SzjOD7DoPrXQNOl1L5bFVSMjd83GSOnuO2f/AK9Qm4S8t32yeS/LK2cZ74IPH9eKwG1GazuJUnUhnBbzMEZJHDY9CK8apCVROUnc9aNo+7FWOzt9Vi86OdpWUhhGEJIU43Z4xUsl8Jr6TzFkIg+UDHB4xux7butceb9fIR8s8mNqxFyD1HzdPQ1NBqqWltP5rt54DBnfOGOf06fyritK2pryq+hZ1jUpn3NM6qjvukAPzDBx9RngVl6derp2oQzysQrIQzEccHj6dSPwqjd3iy3O9QXmEoRgPmUkc5z7n+Vbuk6bbXJNzdp5sijCxucpH7Y6GuihRlJiqVI046k1/ILgsMSSblD8Hk89fcf571h2t/b2utWtzKFAimVSSTnLcEntyT07Yqa91mLT70WcuxYmfKD39OOgrK1mKGaJ/s0Cr5QLAdeOhP4Yx6Dnviute4+V9TBNTXMuh2c+qQ6NfRQ3EUJsLh9juIwCpPAyR15PWqGsLN4Vn+22cm/SZWzJb5+5nqV9PcUmqaZc674StCOkkCO8p4529R361D4zDjw3YxzAlgE80/3jjBP51lDXRnVPW0jz7xFp0Wo6xLdxSCRJAGDUU108ptm4YA4+lFd8ZyikkzjlShJttHD13PwxJGs3hV1R/s+ASuepxXDV2/w1Tfqd8AdreQuG7D5x19q6MR/CZ5+H/io9UaCI2zozRqCrBmZyAvQHjsentzzXM6tHHDNhZhJEJHVcjlcHp7fh6VqnUQrXum3jlproPicvnPynofqT/wB8iuaaTzbcyHIiUbGZl5L4yCfw3D8K86EdLHpSevMSfaGityVYMT0OeQP8ik+242KkuDtMrGTkMSMn8e31qnFK1nNFI+Cg5wecUt1KfLn5WMYIOV+6P/r8fnWcqdpG6ldXIru8WKCFJBh8ZJyMY/DuSev+NX9O8WS2gYLIGTGSpWuf1KNsrj5Qo5X09s/lWarFJQVOFLZA9sV1Uaa5bnHXn71mdJqGoLqGoQSA5klcIFwFPJ55PAOO9bUcYvWNrO8IhZAkEKP1GQM5znaBj64GOlcNJGLqExHIYHKEdiKXwvPezeMtPQSt5zTojsx52KckfkKupQ54t32MYVOWSVtz6FKW8NqluCqQxxhMHp0xXDeK9V0yPTxYecJ2RTtVDux9SKZ4oubl4ypuXWBT8yjq3PrXnOoMIZmeCYbQxbaW3FgCMcdCPb2rjo0+dnozfJG5Zm1NJCjT3JL7cYVBhQOAOn+c0VzN1egzkqmM8nnvRXorD6HnyxOpnV33wrt0utV1CGQsFaGIEq2DgzICPyJoorWt8DOWl8aOh8URx22jW7RIFcLE+8dSWUk/rWDLI/2mVNx2q3A/4CTRRXHH/M7W9B4YmHaeQdw5/wBnpSSqFl9QwLEH2HFFFZVNzakRyktGwJOAM49T71l3cKpc7FyFAU4+tFFbUDLEbiKxjYbfSrGhTyW/jWwMZA85wH469aKK2l8L9GYR+JeqOt8VqIJPOjyGlVywzxkY5xXAXUhmNzK4G7huOOSeaKK5sLsdld6GFIxaRiTk5ooor1TyGf/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

