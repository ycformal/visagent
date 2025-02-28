Question: At least 2 regular mittens are stacked on top of each other.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/0e/ab/8b/0eab8bfcb9cc78d4ef82117a97a60138--knitted-gloves-knit-mittens.jpg

Right image URL: https://images4-b.ravelrycache.com/uploads/debgeroux/311398620/doreen101-160_small2.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'At least 2 regular mittens are stacked on top of each other.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA+AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+o7ieO1t5J5m2xoNzH2qSsDxZIw01IlP335+gFAHP33xK+z3Jjg0tnXJCM8uN2Bk8AHHFb3hfxdY+Jrc+Wptr1F3S2kjAug7HjqPf88V5/PDFwxUDaMjjODnr+lc2+pPoviLTdTtAFME4DDoCrEKwx7qTQK59C0UUUDCiiqmqXw0zSru+MTSi3iaXy06tgZxQBLd3UVjZz3c7bIYY2kdvRQMmvDtV+Iuv6vdeZb3L6fa5JjhgwGI7bmxkn9K3/8AhPn8TaBrek3sENtczWMxtijHDEISVOf4sdPWvLoSWgG/bgdx+BzSE2eu+CPHl5dXkenaxIkqyHZFcYw+7sGxwc+temV8x2rPDNlZAGTDBlPQ9v1xX0np9z9s062ucqTLEr/L05ANCBFmiiimMzLrXLazvktpQwBOGk7Kff8AOsnxqxW1tSD/ABN0/Cqvim1MeoiXHyzrx/vDgj8sVmahqJu9KtbeVmE0BZe/KcAHPr2/CkBj3AAiJ35ArjdcSV72CEx7R50eePVhXYqxkh4UMOcfWuV1mXfq1uB1E8W7P++vNMk+iaKBWD4m8XaZ4WtlkvXZ5pATFbxDLvjv7D3NBRvVUlv7AXYsJbq3+0SLxAzjcw/3e9edxfGaxMwW40m4ji6F0lVyPwwP51w/i+WCfxK2u6XqHmwXrCVDuKyW8igAqwPK9iP/AK1Arljxv4Wn8NawxiBOn3BJt35OPVD7jnHqPxrkhCxjZQwwuByPavdfC2p2vj3wlLZavGss8WI7gdCT/DIPQ+/qDXjmvaVNoutXmkysXeFxhyuNydVb8QR+NITKiGOO6CjOWOC2K+iPBkxn8HaS5IJ+zquR7cf0r508vZiReXCkY/CvorwVbPaeDdLikxv8gOQDnG4lsfrQho3qKKKYzM13TjqWnMif66M74/cjt+Ned3iO20soAU8g+vWvV64/xRpqQzrdqn7uVsPxnDEfpmgRyVuiuFSPkEZ5PXNclryC21jai4+dGwPr/wDWrpYbhLWK9aWRibWTLZA+794fkOKoTpFqfxE0/T4wpOYtylc8bsn9ATQI90rwT4tQ3dt458+ff9mnt0MDfwkLkMv4Hn/gVe91keI/Dlh4n0trG/Qlc7o5F4eJv7ymgbPmBwskhcvtI4J/x/zirXkRMVczAHqMD/PFb/in4ea54YEtwIze2CjP2iBfuj/aXqv15Fcik/mggHIx0IyCfagk7Lwf4mj8La8t07SPbyDy51XupPXHqOv6d62fimbeXxRY3ts6vFd2KsJFOQwDNg/ka86ikJYEqN+eQf8APNalvdQvNbLqEUl1ZQAgQrO0ZAPJCsOnPP1pDEjwDwwHqccV9C+Dbtb3whpcquHIgVGPHDL8pH5iuV8G6Z4I1bTri5tNHKLbt++a9JcA8nqSQeOtdzbXGl2ojs7aa0izzHDGyrnPoB60IaL1FFFMYVn63byXWkXEUUfmSEZVR1JzXyr/AMLy+IH/AEGo/wDwDh/+Jo/4Xl8QP+g1H/4Bw/8AxNAHq2uaD4gez1KO20W6eS6SBRt2nced38WBgfn71e8C+HtRh+IeqanfaZcW9uiFLaaZMbuAOPzavGv+F4/ED/oMx/8AgHD/APE0f8Lx+IH/AEGY/wDwDh/+JoFY+u6K+efhV8UvF3ifx/ZaXq2ppPZyxys6C2jTJVCRyqg9RX0NQMCMjBrj/EPw08O6+Hk+zfYrtuftFrhST7r90/ln3rsKKAPCNY+Det6dGZ9NvIdSVf8AlmR5UpHtklT+YrjYtOvrnU102G1kOoNJ5XkSLhg3fI7Y6n2r6pqmdKsDqg1M2kP24RmIT7fn2ntmlYVil4d8PWug+HYNJWNHUJ++4yJGP3iQex/lV2PStOikhkjsbZHgG2JliUFB6KccCrlFMYUUUUAf/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least 2 regular mittens are stacked on top of each other.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

