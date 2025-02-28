Question: An image shows exactly one fragrance bottle displayed on the right of an upright black box.

Reference Answer: False

Left image URL: http://i161.photobucket.com/albums/t220/latherrinserpt/tea-for-two-perfume_zpsef4207c5.jpg

Right image URL: https://images-na.ssl-images-amazon.com/images/I/418l7uGECCL._SR600%2C315_PIWhiteStrip%2CBottomLeft%2C0%2C35_SCLZZZZZZZ_.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows exactly one fragrance bottle displayed on the right of an upright black box.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAnAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD1VTXP634qm0m+ktY9OeYJEsnmliFOewwOuMn8K3VasjUr24kjKJaxl03bRLINpLKV5H45rGrJQjduxrBalrQPEA1mMMIQmcjKtkcDNXNXu5LG1MyRPIFVi2wZIwOKyPDtrfaRCtk1tCd7feEnfbk5/KrOoz31w09uEt/szjYMkhj9azU/3d5Mtpc2iOc0DW9WvNZurW+S5zGMbdoCqQef511b81yehmefUtRu4b2KWV5f3paMjaT2H5V00AmUMJ5VkbPBVcVVCcW7Jk1k97HQeHhiKf8A3h/Ktqsbw/8A6uf/AHh/KtmuhmIhOATx+NcnBr+rvqMdtJHaDMuxm52YGc4OfQH8a29f/wCQBff9cWrztTEWeHyV3LaJLux3JrjxNd05JI6KNNTTbPVqKr2P/IPtv+uS/wAqsV1p3VznYUUUUwOLQ81h3shN6yEA7fLYZ7c4JrLHjMA/8e3/AI//APWpI9RN9cCbaVLgKB9GB/rXnZtH/ZJm9B++jqJrhvOtyuf9cM49MGmSy7rmQZ5DgfoDWDpuuTajqn2S3g3SKWxz1xmqsuvyxvNdyW5EIc7sOOowv8xVcrdIFL3iz4fbEl/wBiTt9TXQwOSXbsSMVwtrrKaatzKyErO24EEcfX86uR+KntLdGkt2YSZwd2Bx1qcGveuXiD1Dw426O59mH8q3K8Kl+NcHhWQxSaLJdef8wK3ATbjj+6aZ/wANL2n/AEK83/gaP/iK9E5T2rWIXuNHu4Yxud4ioHvXmsSSG/ciJyJLaO3Ud94PpXP/APDS9p/0K83/AIGj/wCIo/4aXtP+hXm/8DR/8RXPWw6qu7ZrTquCsj3K0UpZwKwwwjUEfhU1eD/8NL2n/Qrzf+Bo/wDiKP8Ahpe0/wChXm/8DR/8RW6VlYyPeKK8H/4aXtP+hXm/8DR/8RRTA4r7e2eprdtPHFrZWkUN1p8skijbuicAEDoSCetFFTJKSs1crY1bD4hRXGoW6WlhOPnDFp3BC45PAPPT1FZtn40tbJLmz1C28yAys4dQD945wVPaiinZWsK+paj8Y+EFDtGGBPLBrfPPtwR/KsfxB4kTV4rJ7eN0gjVlQuRls4PQdO3rRRUKKi9ENtvc878UymW4tyeyH+dc/RRWhIUUUUAFFFFABRRRQB//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows exactly one fragrance bottle displayed on the right of an upright black box.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

