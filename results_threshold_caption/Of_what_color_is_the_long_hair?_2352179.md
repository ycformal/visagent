Question: Of what color is the long hair?

Reference Answer: The hair is blond.

Image path: ./sampled_GQA/2352179.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='long hair')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Of what color is the long hair?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='long hair')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABDAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDx9dWljiMCxJtbryc16SI/GdtaQtdR28FqUUEm6kzsx2+frj2rzyz0a71CHzoINyeeI87wNpIHY9ue1dnq1xb6DcDQrWbfJbTqbi6lO5ZDjORn+HkACorOSVoq7NKKjzXbsizOl1qS79DuYAhUpILhNobaOwA575J5NYdzb6ivE2qwSl4/uCUvuTgg9T7/AE/GtjSNT+3+JdOtobdFkeU58pyAxwenOB9a5eWFrvxVd2unxMkcpkliVjtVRtLc+3B4+lY4Xnty206HTjZ+0n7Scrt7/I1LOMS3caSXUUIJJ3vnaMA9cV1mgW2if2VA1yGupJgJERRzGxxkDHv65rhfD+m6lqmuWtsFVFclnL9FQfeY/wCetehSXNvbXQNlHArRMsMZQnZ1wCxHp+tdFRyRhSUG/I6uO7B15Y45AuEDsobnOe4+lefyeFvEVzNPcxwWSRSSu6q8AOAWJHJPNQ2niSN/ilc+ZLdCExCAIAWJcYJAH1zXA32pzpqN0tvdX5gWZxGTIR8u444+lZU00xVGjqb/AEjXLW9jt575LdjloYwfLjJ9Rg9eB71u2HhzxDcq7Wd5p86BypZ4Fchu4yc5/M15i9/cTLtkluXU84di1SQXs0bIqvcomezEDGa2Mj1rStB1eae6FzfaVttm2SrFEAyMcYztOQOevqMUmnajBc2OqCIadcMjFEm+ceT2XJzgrnBzx6c15xa+ZNfRyQ6iIJJW2s/mmPav+0R271sazaR6dBCmj3tms8lsYr3ygQjIpBDtu7seuPT3pqm27or2iUbNI2JbT4gWr+VD+6Qc4gh+Uk855zRXKS22pSFHiuTOCoy8UxC5+hFFU4SWljNSi9bm3dWNh/Y1pE1hPH9kYyRTLOp+YnPzYHTIHTFYWo2LMknn29+2ohmBfI25z/ECM/rXUTW8EkYjV4I4wMFUc/MPTmovsVsDkNGD/wBdCf5ms1VajbqU6acrnGab/aWlX8F5FGyNE27IU56Ef1rodLUPrBDNci9KujhSNgyvOR64Oavz2EckRC7AezCQcH8aqW+mRWzvO1xHBIBzIX3FieDgLnFaUq9mubuiKlJuNo+Zq+DftEes3sMqt5VvGArkdSTwM/TNbmj6XBqrXdpdShEYFUPl4I+Y4b0OOPr3rN0BhbaNqTy5RxvkLqc8BOO/6Vf0XXtM1q28xUlS6SExMdhCqxXGQe2evNZ1Zucmy6ScI8pz1tJbab4wOrvBd3MkcrMyIi7GOMcN+tUE0axeRtrX+WYnb5C8ZNW5LWSyY29zHGJkADbrhRlsdetLGVL8xQ56Ai6XJ/Wo2d0aMqx+GbPzGK3OoxjGcBAP61bj0axhUZOoSEdGKrmrItVZ8kY4/huFP9actoy5Khzx3nTr+dHMxWRxes6Nc2k0v2VJ5IXfft8lsgZ7kVEhiI3yv5buu0hjgntjFd5b/aUcoUQIR1Nwv+NW7Swit7G4torWBobgh5fMlVyWHIPXgjsRW9Os46SM50k9jzi2vJrWEQylldeDzRXoF/ptvqN19ouoLCWUqAXaVdzY7k7uT7mitFimlYyeGTdzT+3W3/QqL/35kH/stNN5ZD73hcL/AMAk/wDiazftGmqoYajfkH/pmv8A8XT45NPmBaO+vyIgSwWMHA98PXHqdRba90z5g3hw89dpk/8AiaY1zo5HzeHpPr5kn/xNJcW8UTQoNWuBPLgpbsjb8HoWw2EB7Z5PpWfc6hbwQgrfXrXLfchZfvN6FhJgD1NNxa3EmmXt9qNOvlsYTZlo2/dzybxK20nChgDwAelYNvqSxyrMqgb4wPKOdrkdsDvzxSX8nlW73Ml5JcXcq7PmUhYweSqHceP51StkOnW9nMtwWuN2WiKkbR1Hzd/6V00oXhZvcwlPlnzJXsdHbz6dqUEk2r2kssiNtjIJicr6H+8B607f4VTj+x7hD6/aM5qzPK52XA1m4gSZfMWMq52g9shvY1XluLiF1/4nsnz4AzFL1/A1zSTi2mdHMppSSHLf+GkVi+m3JXHTzgD/ADpBqnhKRvLTSb8ttLYMw4A/4FUcz32zzf7fdET5m4m5FRW2ouXkz4jDLt6FZvlH/fNAixFdeEXjSRrG7BOOftA/xq5FqXhWA5S1u1wO0ykfzqpBcT4ydfST0YrJ/VasC5uC3/IXtj9d3P8A45TTV9QadtCYX/hIjP2Oc/WYf/FUVF5lz/0E7L8z/wDG6KTeug0tNSq1/qkRUvqMMozyIZlcgdzyMAe54Fc/qviq4uSYbeYEKf8AXr0H+7wMt/tnn0xXU/EHw2LfTo7rS4lhs1YC6jDY7/Kfpk8j6V59YaRf6zqMVhYwNJO/PIwiLnlmbpgVcbJXM5XbHWUkrzhIst5n/LMHBbt1PQe9ddp1hqOmQ3Eqf2ZLPNzIzzRSKABwBuyT+ma6vRfhvo+mRS/bJnv55NuZCSgXA5wAehP9KZ4q8PaRpvhu5ns7VxcZVUZXZsEnnIJxjGamUm0NJI4SRrnWtXWZbeJ1hQExqFiVse3A61fnn1W6hltpNNtfmGN0cEQZfoR0rc8G6DoWpaQ8l4fPunclozMRtXsAAea6BvB/h8MWWzdT0yJW/wAaftJSs30FGEUmu5wsV3dz2MaW1lZ3UsfBWa3DsQfQk9BzxVuOLUnSMt4ZtWYfe/0VP0+an69oh0TVY5IVdtPuCFRd/IbHzKT9OQa3NP8ADnh/VlDWs+pYA+ZjIML7ZxgmplUc5Ny3HCKiuVGG9rfOoH/CN269cj7Ip7cdGqJLW7QR7vCsWSfnxZnp+DV2A8B6SDlby+B9fNH/AMTT/wDhCNP7alfA/wDXRf8A4mgo4/fImFfwyFB5OLaUc/g1OV4R/wAwNh9IZx/WurbwVbjO3WNQAPpIv+FJH4NCgBNa1MbSeTID/SkO5ywZP+gMw/Ceiuu/4Q65zx4h1DH0FFFguWb/AE201G1eC7i82J/vKWIB/I1nReF9GiIZLMKVGARI/A9BzRRSYkX4rKCLhFYD/ro3+NXUtYXUq6blPUMSaKKAIxptjbsHhtIY3HIZUAIp6/fPtiiigAuNOtL+JYrqESxqwcKxPDDvV61RY1CINqjoo6CiihAWz1pB1xRRVCI5j8hqAkhyB7UUUDHB2x940UUUhn//2Q==">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAATACADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDRsPidoup6jFZWVrqVxPK21FECr/Nqffaj4zub1k0/T44Ig2F3FSce5rKtfFXhoqbrTPDi2jwn/WRqqE57A1tp4us4ZYVmhuFEyh1YYxz2OSKwnVcXZHRSoqUbsyNR8baz4cn+y63pENxNtDRvHN5e78gR/Ks0/GjUHysPhqE56bp3b+Qqz48jh1qyiv7a4EyxHYYgPmwe/r+FZkfxN1rQNPtdOfSrNJIYVVXuIyrOo4DY4/OrhPmWpnUp8r0RX+FFtBe2uqJcwpKsbRsu9c4JzmvVtQsbWe4ijlt4nTyQcMoPI6UUVhU3Z00PhM/UIIoFAhjWMbC3yDHI6dK8d8egPf6c7cs9qGYnuSeTRRWdL+IjWr/Bfy/M/9k="></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAATACADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDRsPidoup6jFZWVrqVxPK21FECr/Nqffaj4zub1k0/T44Ig2F3FSce5rKtfFXhoqbrTPDi2jwn/WRqqE57A1tp4us4ZYVmhuFEyh1YYxz2OSKwnVcXZHRSoqUbsyNR8baz4cn+y63pENxNtDRvHN5e78gR/Ks0/GjUHysPhqE56bp3b+Qqz48jh1qyiv7a4EyxHYYgPmwe/r+FZkfxN1rQNPtdOfSrNJIYVVXuIyrOo4DY4/OrhPmWpnUp8r0RX+FFtBe2uqJcwpKsbRsu9c4JzmvVtQsbWe4ijlt4nTyQcMoPI6UUVhU3Z00PhM/UIIoFAhjWMbC3yDHI6dK8d8egPf6c7cs9qGYnuSeTRRWdL+IjWr/Bfy/M/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Of what color is the long hair?')=<b><span style='color: green;'>black</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>black</span></b></div><hr>

Answer: black
