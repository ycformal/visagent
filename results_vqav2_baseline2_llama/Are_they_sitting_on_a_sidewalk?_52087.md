Question: Are they sitting on a sidewalk?

Reference Answer: no

Image path: ./sampled_GQA/52087.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='sidewalk')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Are they sitting on a sidewalk?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDwJQVcZFTntUe0lgeOKlxxxQAqffFOm+/RGvIJOPapntzIwIYDPHSkK5Ql6io6uXNnNEgdgMc9DWl4b0mw1OWT7dNIiqQFVO/1pjMOP/WL9amuJGYAE+9en2/w80O92+TdOje8h/qDV7/hSRuxut9UX2BdT/QU7CPHGOQB6VLBK/3dx6eterzfALXMZgukcfRTn8mrMuPgp4ptDuCROB6hh/Q0WA882+ZKqjqaeyeWFJIINXdW0O90PUhaaiixy7d2A+eP6VTZYsZLHj/aoAiNsy481hGSMgMOSPWinSu08jSDueSzElj3JPrRSDUjCqOp/WpF2+gqvlu4z9RTg5B+7QMuoiN0AFW4bcTqVVyjjqOoqjC6v0zkVehlEbrL/d4b3FMhj5tKljtzOs0jMvDZHK+/uKpWYaK5YplScYC84OfauutGXzBE/KOvyn29K56x2RXiL5hEgbG9TSegQbZ2GmRasY0eFmJFdVaXvii3YCNVI9CB/jWbbX62GimJASynLrj7p9D/AEpdN8U3MeIBAWhPOWXkGsnI6FA6638V+JLVT9o08MB3UH+maytW+IupNbOggEbeoc5Fdhpckd9p0dzGMB15HcHuK4r4hRQR2XmFFWQH7wGDimRY8Y1vUZdU1Wa5mclycZJzWYauwwxT3YV2YK7nBHX1FWNf0ldI1iazjkMkPyvFIerIwBU/ka0JM9GTaM9aKUQZ6GigBgLU4OfQ1CGI704SMO9AE4PIOMGrkLb/AJT34rPWQmrsDFVMjYCgdTQJm1azs+nxKhPnoCB+HGawTLLFcEkYdTzxjmren6tPZktGI3j6FXX7349RWrPZQ65Zre2MLLcdHiDAk+tRKVnrsXCmmtNxNL1xMFbuT5mH+sOCfpW7aX9tYM1xEDKshPkxZwB74rjptNuLdttxAyn0Izj8qljsrvOI0mO4bQApJP0pNJjTlHQ9x+GmpTajb6wr/NHDMpBznBYHj9BWB8U5dtr5ZbaGzXY/DrRU8NeBYxfTwxXt7IbiSNpAGQYwoIz1wM/jXnvxGvYrvVUhjlSRUBJ2sDRsCdzza30e4vE3WkyMYzzklSD2pdQt9UaSMX3710QRoTICQo6Cur8JaDqOutfNavHDDBtG9gfmY9uKtat4T1qAf6RZJcAchozu4/Hml7T3rXHyO17Hnht51OPJmH0U0V0TGS0YxNY3MZHVfJaiqvLsRocnSjHrSU5F3HrirEOWTb91R+NSTO7xLvPQ4wOlQ42yYHrV+0h851wu47uB70AX/DunWtzexDUkvDbZyY7QL5j+w3cD68161Yvd22lS6fo3hfT9Ms5D/rZMtckdiZD/ABe4H0p3h3Q4NCsEYqrXkigySEZI9h6Vsrcc84P1rCU30LSNDT/F2saZZJA+j2lwq5BfOWIz04xWra/E6y85I7zSjAVPJUjK+4BA/nXOeYpPHFQz6d/axS3QL57MFiY9mJ4/ChTY7Ih+PsVrqXhrQtbstjx+e8fmqMEhlzg/ihrxTTEJhbaCXY4AHUk17/8AFzR49G+DcNjv8w211Ed5GMsS2f5mvMfhJoB1zxFHJImbazIlkPYt2FaTdo3ZMdz1fwl4bXQPC1tbsv75l82Y+rn/ADitSX7PIjLLbjOMAqcY49K3LtCY+FHHXisG5Kgkcj6civI9o+dyfU9KMVypIx7jTrMzExMQp7NjNFTM0QOGIJ+tFdSqq25HIz5XFOQ4zTaVetegecKx+bNel/Cnw1pmvam89/cg/ZHDfZMY8wY4YnPQHtXmZrX0XULvTNSgurKd4J1cAOh7E8j3oA961S3msbpopRz1UjoRVAk4yzEV6JpMUeq6bB9ujSfcgJ3qOuO3pSjwxo0l0EazBU9R5jj+tYODK5jzWK+ha4Fus/75jgJ6n2r0fwh4YuY501LUYzHt5hib72f7xHb2FdLp3h3R9KYSWOm28Mn/AD0CZb/vo81yPxb1rUdI8Op/Z929uZm2O0eASD79R+FXGnbVivc5r416lceINLTQNDtZr5oLhZLpreMuFYA4XIHXmvLfB3j3U/AUk9k2nI8XmHz0ZdsgYcEH6V9AfCWCOPwLBKqASTSu0jd2OcZJr5f1t2l1u/kclna5lLE9zvNXa61Fe2qPofw98S/DvicLDHdC1u2H+ouPkJPtng1r38JXll69D618hlm8wnJznrXsPwa8Qatd39xpd1fzT2SxFlhlO8KeOmeRXFVwUZO8XZnTTxUo6SV0dvc5Mx5H4iin6koj1GZFGFVsAUVwS5ovlb2O9cslc//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are they sitting on a sidewalk?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

