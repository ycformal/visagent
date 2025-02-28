Question: The image on the left shows a single white dog being fed something.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/cL981BmPWjA/hqdefault.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/736x/c8/19/01/c81901d017a3bfdfa1ce9a0ee0d14dea--samoyed-puppies-puppys.jpg

Original program:

```
The program is designed to evaluate the given statement and determine if it is true or false based on the answers to a series of questions about the image. The statement is "An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background." The program asks a series of questions about the image, including whether there is a bare hand with the thumb on the right holding a crab, whether the crab is belly-first and head-up, and whether there is water in the background. The program then evaluates the answers to these questions to determine if the statement is true or false. The final answer is "True" if the statement is true and "False" if the statement is false.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The image on the left shows a single white dog being fed something.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA/AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDy7yUzkCuv8DaHp2seIrex1aES2jxyO67iv3VyORz1rkWZYHD5zXS+Dphc6/EgkdS0cmSnUDbUjPZY7Dwna2f2W00a2e23ZZfJD7jnrk8k1L9r8PxOsh0y1ilB4k8hAyZ6E8ZFYOsSweD/AAje6ppbo+sywBY5JHLgAHooJwOCeneuL8F+MbvxDNex+J5I59sYa2mZAHT+8uepU8daSvvcZz/iiZn8Y6zFNJ5hW5PzHuNq4rHYY3DHY81L4rkSPxjqZh5haUFCOQRtHespLlmcoO/y8+9PoJoplm8wgtwD24rQjkdI0VNsa9z6ioTpsxZAibmALYHoOK6rwt4d/wCEi1u00WIGMXDnzpmwzLGBl8fhwPrWN07JGJQ0LwtrPi2+YaVa5jjIMs8hxHGPVj/Qc11+qfC7xcERtImt9StsD5oXEZz3BVvevd49L0/T9ITS7W3SGxjTYIkGBj39/emx3VvbKscQVR7HpWvs49TRQVj5V1Hwz4m0BzfatpNzbwpKIDLIAE3kcYOefr0rJa4k81iAdrfewK+ovGOnW/izw9faasypJLCRHIRkKwO4fqP1r5eltltU3zRyZHEZzw35f1qZxSZLVi1FdMyZEcI9iucUVNaMr2sbCWFAR93ywcfjmisG9STPupS7EA1q+ErmS212ORCRJ5Mij8VxWMVLNW14YAHiGAAf8s3P/jtdT2N0dBqfmvHDbXDSyIPmIDdvQ10HhHxJos9vJoutaLDJEgIivEi2MBjox6g+hrOuBukLNyTxVKABZM5xms3qrGt1YqawLKXVrtbZHFvv+RZgN4GBwfesGfTVjJlhOAOSp/pUWpz3EXiG8YMdhk5GevAojuGn1C3WMt5bSIrBj6kDtVapGTIJLmUXIaD933+VcbT3r1b4HRfa/E+pXsjbmgtgqlueWPOPyqvL4asjIfkhCHoEJz0rvPhpp1rY/wBpNAmHOwMR+NZUppzSMUtTptf1Cayt3miTzAnRCcbz2Ge1YCeJPDMehS+J76zWC6SPybpCMyxkNgoQOoz3re1TE7+V1UD5s+lec+IvDXm6xFNbshjd1aYN2IGM475A7103szaKTOu0eazmlinsvNe1kAlV5iSSG+bGDyBg4xXC/F7wLZW+if29pNtHEkEm67iQYDBuNwHbB6+xru9KARQAAAOtZviu/WbR59LlGftXHzdCoOf6YqZSSjdkSPmtNRVVAe1SVu7OT+mO1Feot4V0tzn7LCv0zzRXN7WHYg8l/tR858pPzNWtO8RTadfrdpBG7KpXaxOORisaiuqxpc65/Ht05ybG3/76anf8J4+7P9j2f/fyT/4quPoo5UO7NS+1t72+mujBHGZW3bFJwOO2eak0zUXbVbNdi8zoOv8AtCserWmc6paD/psn/oQoa0Fc+g5pAqGPhiCT8o59Otdn4D40+/c5B8xQR3AxXCSQoHZo3Yrux8wweK9G8FQx23h5pyfnnkYtk+nArhw13UIW468uVLMqkZb1PSsWWB5WJb5h69AMVX1+y1DU9fn/ALMl8poUDsD0kP8AdrrbuzgtrJUcKZNoz7nvXbuaHOiX7PYOw4561n6zvubG1kjVSySFBu7gj/61Z2v38toUgIzH5mcg9scU9rgT6MndWkB+9jHFZ1WnBol7GeyyISpjU/Q0U5YkYfNKq4PAJzRXn2ZnY+daKKK9Y1CiiigAqzp3OpWuOvnJ/wChCq1WdPONStT/ANNk/wDQhSewHt7Stvcq55bH3siut0XV4IPDnkPI4kiZmYg9MnNce5UHKIMD5mySOfanLdDyzMPlGdjImew4Jz1rzqUuSVyFodz4ZZ9T8Rm9SVltLaP52P8AGew/z6Vq61qHl3R/eKRgkAnHQf415NPqFxBbGC3ubiFmkDkxPjJHan6h4hvLuyFu+HCYAkYnecDqa6I1kkyuZG3bNHqV08NyoZpQxADclsZGKSSWOy0S2SVkV3lbC+wGM1wqPKjbkkkRh0KtgigI8mC7u5wcbmrFSfK4k30OwW7gKglGJPJIP/1qK5bLJ8pLZHoaKzsI/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The image on the left shows a single white dog being fed something.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

