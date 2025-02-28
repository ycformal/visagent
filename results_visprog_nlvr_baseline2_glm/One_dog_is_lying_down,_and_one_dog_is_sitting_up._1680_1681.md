Question: One dog is lying down, and one dog is sitting up.

Reference Answer: False

Left image URL: http://www.animal-photography.com/thumbs/italian_greyhound_sitting_on_t~AP-0PDYJK-TH.jpg

Right image URL: https://img0.etsystatic.com/042/0/8863537/il_570xN.603051874_4pqn.jpg

Original program:

```
Statement: One dog is lying down, and one dog is sitting up.
Program:
ANSWER0=VQA(image=LEFT,question='How many dogs are lying down?')
ANSWER1=VQA(image=RIGHT,question='How many dogs are lying down?')
ANSWER2=VQA(image=LEFT,question='How many dogs are sitting up?')
ANSWER3=VQA(image=RIGHT,question='How many dogs are sitting up?')
ANSWER4=EVAL(expr='{ANSWER0} == 1 and {ANSWER2} == 1')
ANSWER5=EVAL(expr='{ANSWER1} == 1 and {ANSWER3} == 1')
ANSWER6=EVAL(expr='{ANSWER4} and {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One dog is lying down, and one dog is sitting up.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABKAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3cnNMJqr5jeormx4hMfjqbSJr4RxGBGhjcL+8kPVQcZGAARzySaAOuDVYjOYwazBMf7wrRtjut1NAEtFBOKTNAC0Vjv4l0tbtrZbjzHVtrmNSwU+hNSWPiDTL+RIoLtPOfO2JjhzjrxUKcW7JlOEkrtGpRRRVkhRSY5paACiiigDlvtg9a8v+Jdq9/f297bKUu7cokTBgp653E5zgZ469K8p/4Wl4y/6DLf8AfiP/AOJqrdfEDxPeTLLcamXdRgEwoPf0oA+p7K+lltVecbXwO/Xgc11GmvvsIm9c/wA6+Oh8UvGQ6ay3/fiP/wCJr6c+FOqXms/DbSb+/mM1zKJd7lQM4kYDgcdAKAOyPSuWltdZF9qUN29zdWk4ZrWSAqvlKR9wrwcg9+4x711VJik1dWGnY8os9G1WDUZ7eGzWWcKrO6kfKSMA84PT2rS0bwK7axdahe3UkV9FIhQxNlVwoI/+v/Ouzvm+yLcXa4MrBY19h/kk1BZ6xapbbrmcLITznJJ9644U6dOdmzplVnOOiNaEOsSrIwZwBuYDGTUlVLbULS7OLe4jdv7oPP5VazXYmmro5mmtxaKKKYgooooA+AKKKKACvsD4K/8AJJtE+k3/AKNevj+vsD4K/wDJJtE+k3/o16AO/qG5fy7eRw23C5z6VKzBQSTgDqa4XxLrt5qkUlloaho1fy5bljhN3oPXFROfKi4R5mJrOuyMMHIizlQO9VYNSIckqvQdqz49K1bUTJNYxC5itz5IJcAMQOWGetWrTwxrsj5NsIiR96aQAfpk/pXlTpVJyud8XTjGzZPJKG5JDMPmyBg/mK2NI8TxqoivJW28APJ95fqe49+tcldR3mm602n3c8EjeUrt5SnjPQZNWkjjZfmKsCuNv+NRH2tGV4/cKUac1Znpy4PI5FOrF8LSNJ4ftn8zzITnyHJyTHn5c/56YrXkkEcbO2cKMnFezGXNFM8+Ss7D6KYJF9aKoR8B0UUUAFfXHwhne3+D2iyJF5hHm5GcYHnPzXyPX138HLeO5+EehrICQDKwwxGD5r+lJ7aDW5uarObmUxTTmKFh90/LkfQHJ9+lRafp1k8wkurh5QgxFb7Nkca/SunFpb53eRGWIwWKgn86csKJ91RWfsluy/aaWRDA9tHGscISNeygYqZjtBwMnHA9aftHoKRkDAg960tYg858cQG9a31C2hgE0J2yyLMMlR2wM5+pqp4TltbrVM37fI52ooTCsx42t+H516QNMsh/y6wn6oDmpUtYIyCkESkdCEAxWPsby5mbe1tHlRznlWug710e4SGLOWs3VjESf7pHKn9KmhvNV1NhHNBDZ24b94yFpGcA8gcAAH1NdDt9hSgVooJbGXNfcYjKy5GevcYoqSirJPgCiiigAr7A+Cv/ACSbRPpN/wCjXr4/r7A+Cv8AySbRPpN/6NegDv6KKKACiiigAooooAKKKQ0ALRTaKAP/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One dog is lying down, and one dog is sitting up.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

