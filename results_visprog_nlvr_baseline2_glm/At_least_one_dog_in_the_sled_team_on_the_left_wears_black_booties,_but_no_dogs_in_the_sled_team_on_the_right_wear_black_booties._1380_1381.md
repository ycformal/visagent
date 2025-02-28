Question: At least one dog in the sled team on the left wears black booties, but no dogs in the sled team on the right wear black booties.

Reference Answer: False

Left image URL: http://www.repubblica.it/images/2013/01/25/162812880-13b39aad-f71e-4a9f-a954-1d209a6d192f.jpg

Right image URL: http://i2.cdn.turner.com/cnn/2010/images/03/06/stacks.iditarod.cnn.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'At least one dog in the sled team on the left wears black booties, but no dogs in the sled team on the right wear black booties.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAuAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD2+ikZdwxnFRNGi43OwoAmpHGUYeoIqIIjghXY+tPYbIXwckKTz9KAPKvDfw9sLOeO41ZFuboHd5IYmIfgeT+Nd1dadp+qWwt7vTYZoU+6jIMLjpjFeOJ8TNSfwrHeJdWa6o5MZLR8x/7WAcH8q4qLxvrcF3cSrrN9NPcKFkmMhTgeg7DmoXL0NFSdrydkfRGseEtP16GGGRFtng/1MkSAbfbHcV5J8RfD8Phh7WE3/nNPl/8AVFTjp1zjrVfw54/13SnhaK7kvoXcLJbXWW6n+Fuo/wA8Vp/GDUdN1XVdNe0uVncQYbacqjbjwffrmm0tyLNHmz6usd6jSh2i3DeFODt74FXNC8S6bZXk/wDaemfbYCCYhkK454yenSobzTfOsLicSIzQAK4KHqefvevT86xZrcW0yQ8h9g8xWGCvr+fH4U00waPVtfvfD+o+E7W70dosySMssHSSHC8Bh+PBHBra0m70LSPD+jR/Zbi8HkK07QIB5R6nr94/SvHNLilaR2hJOF2suOorUnm1K2J8u5lUL825ugwM9KiWj0LVranp2ufEWS81Ito1un2JEEaNMOWI6nAPA56e1Fed2ElteW5muEbeW/gbAPAOetFL2iW4OF3ofVzllHyrk0zex4MWaj/tGx/5/rT/AL/p/jR/aNj/AM/1p/3/AE/xrUzJNzjpFjjtTtx8ti64wDkHuMVD/aNj/wA/1p/3/T/GmyahYmJ/9Otfun/lunp9aAPjuOCbULm9u7aNY7fezIMYGM52j8KiUKSGC/MvBx3z3ro4b3TRo8sURxOFMcaDP5+/Ws2S1EEgypIXgjpnioUruxXLZXJbW6msIhcxvskjYMpx6V6J8NdPOu2t/pdzZ2P2qCRbgvexMXCP94LtwQc4Oc8ZrkvC2iyazrNqkqYsonDyFv48dAPb1Ner/CfSvM1nXtdLiS2mma3gYD7/AM25j9B8ooTuy5O0UjhfG2grpmvtY21nILKNfMjt7a5yu4DdhlfliTiuKbT7VVjuJrZkE8jJ59xKWLEDLHHGTnj8K9X+MOg3mseK7ddPhKSJaRj5M5dy7AdO4/rVj4g+FG0PwpbtbRwR2n2dVniklZ5nuOPunnjrnp60XsxN+40t2eR6YUa61CGznCp5R2Mina/Tj/PtWzdaRda7qckdtIybwFkZ1+QcAHp6AUmiaJJbSRSi3YvKG2QK3zyHH3Rx0rXTUriC9sXQCzExMs1sM/fHGCD2zj8aiWmqHHXRo46z8NXOyRfOUbZWXgHtxRXtXh/w7aa3ppvbueTzmkYNtQDp0oqbzeqK9xaM+ZM0ZooroMAzSjk4/pSU5OXX60AdnDp5u9QgTSrGSdY0XdgZ3Y9fTmuwsvCSjW9Cg1NtkN7MBMucbRnpn9PxrZs9GsvDWnz31oHiYxCRyhzu6nGD9axrTXLnWvEFleSYVYnjMajtz/jXKp636HRJX0PUfEfhS00cG80yEQxyQPCYwchW28GrPwotDpfg4o8mVaYuF9PlXP8AKtfWf9LsZsltqkNtPTriqPh9hp+jRqgzud3I7DnH8gK1StLQyveIzXPEWkaf4u0pLveLiVuMqNqAggEn/epPGq6nfT20FlpxuYDGxLF1URyZ4zntWH4m8KSeKtYivpr0QRRoImVEyxwSeM8d66qGNo4kiaV5AiBcv1PuTVOMbWEpO9zhrnwDPbaqmpR3qEIFdo1yGR8c7T0xnpXMeK9Pnt7nQ9TfMslyzrNMBhRknr6cbT9c167fbQrRDK5UjcvUVzviLS11nw3LpRwiMoCtkjBHSoavsUnY5HT/AB5pFhbmFNYMPzFmQWjSDJ/2u9Fcuvw3uBNcRSahHmKVkBVDyB3ooSprS/5l2qPp+R//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one dog in the sled team on the left wears black booties, but no dogs in the sled team on the right wear black booties.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

