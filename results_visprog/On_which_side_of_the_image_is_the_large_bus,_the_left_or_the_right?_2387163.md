Question: On which side of the image is the large bus, the left or the right?

Reference Answer: The bus is on the right of the image.

Image path: ./sampled_GQA/2387163.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='large bus')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='LEFT')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'left' if {ANSWER0} > 0 else 'right'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='large bus')=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCADhASwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD2Wz1JLsqjEBunNWLq1ITP3h2GOlcHaagY5FIbpXXWmti5RFkIz/OtpRa2ITK0saM3oahe37kZFaFzBEZXIcDjIzUEkckUeOoPQ00wM6a3GOBVbyjuxir7PxhhUHmKrZxVXELDE6PxmtyxuXgUhznPY1mWtxHv+fpV5biENyARUy1Gie4uHdSTwKzxcur/ACk1JdXKsmBjHtWeJcNmhIDZF5JLgsamW5fPy5NYqXGOM81saYyNneeT0pNWQImlneQLHzk1YjzCF38ipHiQfOFGRVKS4IYgjoala7D2NAuCvy85rAPhqJ783k08hAOdi9/ar8N3EkyqxI8zO0HpkVo71xnNCcobBZPcoRhsAiLYvoegHtVpHU5AxmpPMRuOtRyJ3CjJ4yKlu4yuPLlmMe75vTNMks+c54qxDaLHMZSo39AaLoELx1FO+ugWKLWyr3pUcL8oqrNNJn3qBZnV8tmrsSaMtqZlyOtUpLGRAc1Yjvjgc0952kQ0tUPQymtyDyaY1tnkGrbK/JIzVcttPXFWmIhZWXjNRNK4BGakds5qu4zQIjllYjrVYs2amZCe1R+UaYhonYHrVq3l/vHiqxh28mozIVNAGr5+D8vSpPPCkEj61jm8C1G94zDANKwGzPfoV2gCuP1U3CmR2kMaE8fWtVS5BJqpLov2+QNuJbP8THj6VpCyepLuyC2nkktU2/Ke7MasLHvUH5m9wK0E0CJnVWjIVeQAeK2VtIYlCBQAKUpLoCTOGinKt1rUtL9o2U56VhA4NSpIQetNlI7OTVRcxRqfvJ0NdNaPFdQQxyMCWTII4wRXmlvc4xzW5Zai8ZUh+nTPas5R00KTOqvNP2H5TkY6msC4iaNyCDWra6l50i72J9qtX0K3D5VQOMdKlNrRjsc1GCG5p7TFe9Wbi3MTYxzVF1NUIf8AaCRyajMpz1pEidyQozim+Wd/NMCdGOc5rRtrl4mBBrNGFqyrgoMDmkwOkgvfOjwW596hlXexI6/WsmG78rOatW915r4XrU2sMnnjP2GVdhZsEoQMkN2Ip2jzXEtr/pQUBTtBGfmPrWmsscUAyO3Ip0It9n7sKo9BxS59LWC2txiDHzA8VI0hTnPFK6oYyQQAKqSKZEIWQrj+L0qVqMveYu3cCKjJD85FUjE3H70FQc5HeluBtG5JVU4/io5QuFxbDqBVF1ycAGrVvctcKzAghWKk5qVthXI5Peq1QtzNMVOWURgjtVzyt6biMVSntiQSpp7iGG4HSq9wAwytM2sh5FPQBhxTtYCtsJ460ohzxV9Y4kTOeaqyuo6GmIUW+RyRSfZOSewpI33DvVmJyetJgZ9xBtHNZU68mty8RtjEKSQCeBmsyOFp4Y5AGw6huRimmFjJdWpIyVbmtdtPbGcVCbEn+HmqEVjP8uAKsWlxsbJqN7J1PSlEQGQRg0CNUagoA5pHvYyclwD6ViuCp9qjBY84pWAw3G08U0Ng81ZaL5uahkj21Qx8cnNXoZyCOaylyDVmNsUDOks73YynNbUuqhlXaccVxsTtV2KU8ZOaloZtvcmQ5JzTRG8nQVRjlBYCt/S2T+MjB9aWwEFuDEDleoqnMArEiuhu9rxkRoAF71gXKsScCkncZVaSlWRhznpUe3HOKQNg1QjStFadlXGc8Vrx6c0RBxz6CsK3u/LIxW9DqpKoSegxzUu40STs3l4BPFV4p3VtvJJqZ7iKXkdT1pkRjEof0NSgLCySMCOcd6fbtIZCijg9zVqOVCuCBz607zI4VIGKVx2Ks4eEDjjuRWbLesMhlDjBz6+wrVF0N3KjBrkvEcX2e5VoshJhkbegI61rTXM7MibsrosWF2bS1kWQjlixw2cU5NcYozrG/l9C+OKo2+gXd3bQz20iDcMlXOBWs2kXKeVFdsk0JHITgA9s1rLkuSuY0LBmmtld24fkAU9fLEzRFjkDOaLYF4FSJFSOMlfl6celSx742AIB+tc73NERvbJg5FUpINvKHj0rUkZmPSqkq4bpSTBmdIklVJIZM1r7c8YoZFYYIFO4jPt4CpBckirIdEqy0SeX6/Ss6dSGwM073AnkmR1IPAwd3Pasvwc0d74Q06XJyItjEkk5ViDknnPGfxqPVrn7Lol7L0YRMq4GTuYbR+prmPh/qhtZ9Q8PyFlMZF1bh+rIwCv/AOPAH/gVS9A6HoDhIQec/WqhkRm461DcTkkiqfmNu4zVJCLkjcnAqLy1JO7g0iSMOpFTKeMnFAijNbbgcd6qeS44wK2SQKjEJfkA07gc28RPIwagkXHBq0GIGe1QzYYEcVQypsBalAApGBU9aTJoAnWQjipFmINU8mnqxHvQBoJcENnNadpqBQjmufDnNTxPyKQzshqCSQkiUgf3abFMkgIIznvXPQs3rxWjayshHFTawFya1VlJWqRtzznrWxDE5h3HOGqG4jRBQmMqW1puJLHirDKIxtHaoPM2cZxSNN370CLcBJJ9KvQqCwGayYp+PSrCXAB4OKTGbbuEULVOd37E1WFzkYzUiuWHXNCQD1Z9p3ZqW3hJV9wVhjjcOlCMuPmHFSpMoRl6elFwsc1BqFxpN0LbaXVW3N2zn0roZ9TUiKZQx6MBjNZ2p6Y+oIs8P+tj4Ix1Hr9ahlN1ZW43qrBVzlB/Stmozs+pmro6ZbiMRqDhFYZFQl0dvlb6DNc3DrH2tkiAJJOOT0qyZjGeWwaydNotSTNiS4MQwTn3qpPqEYQlpApxWcbpnIyeKqTyRzXKWzkgueuRgCnGAmzZS9STCKwYn0qdgAoJPNUYrG3s0WRDjAwGLUXN9thDmNjH/fA4oavsF7bmjGqrBycmqblN/PNU4LqeZgqxsMjOD0pUW6aXmEBQeW3cUuWwXOS8a+IdN06YWEt20ZB86VU5flcKBxx1z+Vebz+KPs3iOx1rT7WWGO3JUiRs+cpOWB9AQSPat74niE6+k6yQxyiPy5GIGRjBA9+vH/1q4KSYLANhkdFcs0pQ7TxjGT24+lYSb5tDZJWPoPTr221bS7e9tn3xTLlGPXGSOffjmnNGVJxXO+Bb2GTwpZpE6EQqFcKMbSecfWurUrKm5a3jtcxKoiI5zxU28KAKdgL1OKhaRCcDrTESeaueamFyqjAYVSdfl61WZmz0osBnQrMoG5Dg1Ze1imUup2kDlT61bvY1iJMTcDoKypLpwTnijcorTQspNRAc8irBkLZ5puzc1UIi8setABB61N5RqNlZe1AEka56jip1RQeDVUSnbjoaFdhzQM14HCkA1vacIJCC2D6iuRS4961NO1EQzKWPHepaA71I7dLPETA+xNYV665PAonv4hsaKTcDz9Koy3AlbJNQkxsrytzmow+eDRIwqo8hU1Yi+F4yCKQCQ8jpVJJ3qzFccjNAFqPf68Vr2KidlUttPrWbEfNHSr0EZhw5PvikxmvJY/LsSUBh3POaqPDJCTvCsP8AZNJ9t8x/m9OKdLIjCPYT5hYd+3ekr9QdizArogKrtFRXc8DId+0EdyOlTGbcxx91ec1CzRyh2lRWUdFYZzQtwZycqWltdlo8EMck+n0rTES3ab42ABHWqepR29ndxyBQkTHlAOo7miW+ga2cQlkDf3fXFdDvJJoyWjLMdhJHvMjZTqGFSxaWk0vzxJKijguORVjSNslpvLtIgOCWq9JdRRuAB8vcispSadi0lYaLOO3jGMbVHKkZFEs8UoEe3aPYUTXcCWxIYEkcZPNYYviX+YZFQrsZtFEjUMDx7VWa5JbYoYAqW3FflAGO/wCNVhMxHySYHvXH+NfFN3okEaW6CVHLRz7WAxwGA5z1HseOO9D0VwWpieINKt9X13UNQK2hmNkt1bbjvZkRsN8g+9lR1z1bHvWf4jt7ePQ9RXbNbwsYrq13uqZ3DDRBOCMenPeuZl8U6rPCltYKlpFGpSOO1j+YLknG889TnjA5rOZCJy10XeV1JLSPuPU9+T6ZFYuVzVI6b4c66mnXU2mTbBHcN5iZIG5gMEfiMY/H1r1iy1e3k/drE65YrgivnFGeIpLGWVlbIPYMDwf5V7h8PJZ9b0sajdkJN5rIMD/W7QuW/Nufc1tCaaszGUWndHWSQNMm5FODVRLdi+dpNbcs3lZQ/hmsW8u3ilDjGMdqaYiCe4AX5VY9jxWQ+t26sVYEEdRitI6kssZjZRzVCbTfNkLiNDnuQK1jy/aJd+hE+phj1yKrTXSPk8ZrH8/3ppkOamxZfafB61NDcc9ay9x7mnJIQ1AHRRSBh0ye1RyvgkEVQhuSMc81bDm4OCPmpDIyN+cU0Fl4qWSCSHqCKj3nvTAbhhzipEcg0qtnvSlueBQItw3DqMVYS5YHk1mbn9KcpdjxSGajT7uhpjkFgTUcFrM+MqcetXo9MmcZ7CjYB1kqO4DYweDWnHpKu+VYAdqi07S3L/McYrfjtQgw3pxUNjRXtrGOBizcgdKSWQCUnA2+lTuPLA5+X0NOW2DHOOKkZVWEOeFIHqOlZusLiFMMv7s7hsOTmuhYiGIZGRnBWsqW2hu5tkUTKBydoxz65rSnLW5MlpYqWGo+ZafvGIc9WPQ1PHfqARLIFUHAOOtPXQIY4m/eSBj0O7gVBH4fuYpw4njlhPVXzn8qv3G9yUpIlv7eC7twJWBKncrDt7fSshbK1j375woXqGOTn29q1Yra5Vmja2cRqcDaOD7j9KyJrWWeaWCK2KOTuLMCCfrnpVwfS5Mu9i9DrVrbW5hiJZieoXANSS3IO0s2C3ask6FcRjMhAPbac4PvU6aOZF3+e0jDgruwaJRhvcE5dh8t3EJW+Zdo9+aUSqWUBQynqfSq48L3kzZVkVO5kb/CtC20aSKMRzSA7epXjNS+RLRjXMyZEUplO9eVfEO+I16SxFu+4LG+9wV3DBBAHQqeOe+B6V6+tusC8YUHtXknxRQDxPatGQ260Xv3DvXPUemhrBanFKs7qEiXahO0Kg7+mB14qrc26pPEHY8gjPY8j0roIUhkhhOU8uIlpMnk4BC9hkZySfbvisfUjm4j2j5hlTuI479uKylFJFJtmfBCdjFefmP413Pwz1gWniD7I4fy54XCCNWb58qckDgcKRnAxjntXHWcmx5lwNzZVdx4zjAz+OK6Pwa623jeAIxKvHJHnPX5D/hTS6ikevX18Sp9fWsGed5M5birk5MhwDUUdumWEnTHFdC0MmZju+cipEupQoBYmtIJaqu0j8aaYLYnOT+FVcmxynke9PEGO9Pw2aeCMcigoZ5OaPKx2qyirn2qUpkcDNIZTHFXLdzkYNRNA7N9witCx0+aZwqpgerHFNsC0I5boAbh7ZqpNaTIxAUnHoK2DbfZAEkcA4zxUsN7BCjZG5v71RfsUc/DaXErYSNifpUsVpLKHKbWVGKkqcjI6jNXLq5FwjRlMo3VQSMj0OO1VrS4WCAxxRrFGrsFVRgAA4/pTuwLdpp+7mTjtyK0ItNT5sAApWd9uLj7xpp1F0kLh8k9aNRG+iLFEC49sGpmnjSNcMAPQVyjaw0kzxlzlQpP45x/KkN+396p5QudVHqQjbK1eh1uPblyNwHGa89l1XbdwQ/xOHbr0AA/xqDV9c+w6Rcy9W2FEH+0wwKHFDueoNrFuXUEI6kD3FXPOiMYaEqBjpXmGj6iLzSbO4T5Q8K8ehAwf1BrXi1OdBjccDgUcnYLnYR3ShiDsYE1bEwkAWNVCj72BiuDOpss8CMWBkYgY9lJ/pXVWFwr237sYcjGTUyjYaZdlkSKP5jgn1rKm1KJSCrHg4IqhqupOCYm7d6wnuz61UYibOqOsrhgrMCe2as2U00+SwyOxNchb3Cl9znp0rYj1Xy02q+QR+VU49hXNaS33yFpJd0fdc4A96sxxWsCBgiD04rIj1QbQwXkdcnOa0ZriKeEFcHjtUtsaEnvokyI1GDUDagGHIGazL2QL90Gs1rtj601EVzYur0sMZryX4k3Ef8AbFq5Yhkth1yP4yeD/hXdvNI5IANcH8RLe5U2M5jR43R4yd3Knr09CPftU1I+6xwepyb63si2xW6lgM+YRgngjucevaqLzyzSDzGVFQcYHH5n8PzqrukI+Vduakt4jJMN/wAwwcjFYGghkKSFkbePrW74SvVXxdpsjnGZdhyD/ECB/OsC6j8qfEYwpHStfwYs0vjDSRDHudbpGIJwMDJP6A00S9j3EwK5AVuSPSmvYvjjrWlwzbvLGcdqATjn5cV0cxnYyjp7FMkEmovsTDua0ZbgIeDVc3BJzindiIodOtfs6uYNz55wa1bfTNOmtsywBcdyeazdOv0ZtpOFPtWrc3CfZ9inkdKiVy0Urq1sFGIYUznrVR444l3NErD09PemySAnuPrUPmBsqWxmmBVldVfcKemoPH0bFJJaow3bt30NRR2IlbaHwfeq0ESyTvKd24momufJjLMCeQoGe5IH9atxaFdOM74wvqWrmPGMUunTadayXAjeWQS/Kc5AYAfqT+VJtDSLz6sItVhtC+HZGcr7cY/qfwqSxn3W8bMfvDcR9Tn+tcprVzPaeIbmQQAuheFHUjPC4457E+lXvC9xc6rdw2yQuyxWhUvjjKlc89+MUlNXsHLodD54eR0Un5MZ/EZqOSRUaJSfmkYqOfRSf6Vl+GYbrU7nU5Ynadd6vgL90HcB+gA/CqfiC4lsPFGnRyy+UsKGR0PuDjjvkACnzaXC2oPq0UGq3KM7AvdwxD/dAIJ+mcfnW0cg4yc153FcNdazZlsSO9yhIPQksM16leadLaadcX8hjaCBGkZg4PA57UoSutQkjjri5ZvG1pGs3yqmMehKklfx4pPE+qRSaQ8EMiszT7HXPICn/HFYVnfwx+J49QuziJd0hxyS2w4H51mZkladpD95g2B3OTn+tQ56PzHY9O8NSSv4fsiF+5BlsDhVGeT6cD+dW/D+qHU7WaUAsFndepPGcj9DXk9tr+pWO+OGbMe3yhGwyMHIxxjmtXS/GF94esns7Y7UlYOXwCV4GcZ74FVz7BY9C1W6uf8AhNvDdgm1UdySG/2iVbP/AAEHFegQ3Bs08oOWXHQjpXlXiFku/i7pQjk/dtJa/MpBA5zXptw4c8EBu9F7tgST3MUybXRfrisK9hRT8ucVPOzqxAqnOZHXJVh+FXHQllJmZW4NTQuc8moWBB5H6Uu8jotUI0Flw3J4q/FfYXGea54ysT0NSxyOfak0BtSXPmcZzVaRlQ5x+NQxADlmJPpVhIvOdS7YWgCGMvPIEQE+tc98RLfytFtuSf8ASOcD/ZNegQWcMaCTcqg8DA5rjfihLEvh2DDHAuh0HP3WrObumiorU8c2Kkq46YH8qfbKPOwPQj6daa0qZDBXO3sB9aI5WWYYCpk9WOf0rnNRtwu5wOfxrc8BMIfGWlE959v5qR/WufkkYSDJLfUbav8Ah66W38QadLkqVuUOcf7QqkQ9j6HaRVGfaqkl6pyCB9azf7QR1+aQfTNQNcRlc7hj6108jMuZFySWMnPSoi6f3qznlB/jxUXmn++PzquRk8yFgleE4PT1qxLfPwVJNS+Q+3DoD/OoRprXLERtj61F0aFOW+Z+5FQi5kB6mrNxpE8JOSrH2NV1sZc4I2/Wq0ETR3zdMVbhuwpyQM+9QRaXI2Mtx7Vox6IpTPnHP93vSbQyaLUjt25wK8+8a6nJPrVsYyp8qJdu5QwyHLf0rqtdQaRpFzdNIyPGh2ZGPm/h/WvJRcmbYZJGbBI5PQZ4/mfzrKbS2KjqWNVuZLyeSZnHmyuXkZB1J5PFJperX+kXoureVS+x48Pk8MMH8cVFO3I4C/Q5zUY6qC2PX/61ZpltHq3wxufItb9xEilpI48qNvCqf8a5P4mXkcnjidvLzIiRKdvYeWP6muh8Dy/Z9Ddt+d87HP0AFcH4l1EXniS/uVjADynG5x6AdvpVS+FCW5kyCSCDzQxEgJdWBIIPapo9e1V4WtpruR45EO5WwSR9etQ3TzGBWyv0C/5NVS+DIxjBCj19cVKeg2i40kBcZcOQAMKM9qlNwxjKouBnJ3cHp6CmXMfljhiG5OC1SwnbbcH5j3FRcdiiGB4aNsdTjmjMbFctyB/F/n0qfyw9xsB4xUbxtj5eRk98iquI3fCqyS+JtLEZLOsy45yTgH+gr1/7QwXDhs/SvKPA9on/AAl+lsyKdsxcgrxwrEfrXtdzd28MUzvkGONnyRxwpNbU3oRI4my8RrdeLdSsFkkZYolCoRwrISHOf+BCtlrtugJFebeB9SuLjx/bT3Ewd7wSC5JVf3gKlznA/vKD+FevtHpsmS2FIPODVrXoS9DDa4bvg0wz+1assWndo3Oe5FVfsUU33CwGeCRxV2ZN0QRuG/hFWUhLkEbRUtvowk+7ccjsFNaUenxRgRcu56HOKluwyCG1RV5kBOOwp6wSjnHy/Sr0Vulv87hQ2e3OKSaYYCp+hqbjI/mZQN+BjpmuM+IUBbwyHLMNtwnIPqGrsiyMm5gc1y3xClVvCTqEwwnjP86UnoNbnjLx/NjJwfU/Wpo41SZT6N2HuKhkJ3A5wM9ziniaNWDNKuM/U9vSudmoy5Xc654p+lqRqdthyuJ05/4EKhmmRpOdwH+0OtOsz+/V9wGJAR3754pol7H0F9mtbOHy2jjdv4nK5zVWWLTTyyKSf7uR/Kppomkc5PGeeajWztQSXDH0Ndak97mFulihqDWjx4hhCkDgqOaySHz0NdJM6RKEUAqfSoGgt3wxAyRzk1rCqktTOULlvSr+a+0m1upohFNLGGdByobuAfSrTK+Mogz+deD2819YmzW01zYZkLOI5XCwkZwGweuMdu+K27PxR41htrKZZZbiO7kMcAljWQuwxx0z3657H0NcvU6LnqVwoLDzOGY4AzjcfQeprH03xH53iH+zUiUqGuFcscnEaqAQP94t+VeeXfxA1i51KwmufLVbKZZfs6RgK7A8k53EHBK5HTPrXPyalK11LcwTyW800jsxVsEBiSRnik2Cse/3eq2doyi4SPLeZxt5+RC7fkB+tWbGeK8sILuOPYZYlk9MAgH+tfP0us6pcyDz9QlkU7gdz9S64Y/jgCvWNM8WadFZ6fBHKjgfZYnJlUbQyMWzk/w7MH3IouMzPifqQ+zWumFyXkcXGCp+6u4Zz9TXmckINsih13E8/TNdHquoP4u1CG8aB4jBaGNlGCA2888445BrBmG22UD74XtWUpa6FKOmpVa3m8lAvJBYnB/KrKK3mRhgeVDEe9OKICm0Lg4yfQetKzKkobdngDH50m7lWsdUutSaLoukxRw72upXyM4wN2OPxI/KuX1AK1zKoLEh25PJI3Y/pSma7u5okk8x44CDAAmMAcnB/Lmq0kkrBj9nJA/jJOPpxjmqm72QkgvQzrCi9Tg5xSRQrITvU7WfOzruweB14zSuZBKvzoq4G/p8tIOQFe479Af4cD0qFsMnnUMS2QvGPmcKB69TzTBPEsO3dzydq5OPxqo/2cEnD57BVAH86mUsLfaqYAU8lqLDEjZWlJV/lOcc0rkgcN8pyefrVbfA3VWyBjsaFERP7uTYD65qupNjpvD+rW2ia5b6hfq7wxbgwRc9VKjj6kV1PiPx5pOo+HprfTbgrcthQmxlYqT8w/KvM5gJIFUzlskbhuB702OPEokGMHjbVwlyxsTJXZs2Draala3NpPtmjTy1KnOCwIJ+vzGvSfD+pNqlvezFCgS8lRfpkH9M4rxloTtyvLZJ61t2t9cabD5ltePmYODErONjZG1sDA3HnnJx3rSlUcGRUipI9Uj1RZNdmsA5MsUCSfqc/oVrSXUYoLy2gkcb5Q5AzgnaAa8dGv6xpWrPcfao7i7dRDJI+2RXUcjkcfiPSrSeN7t9VsNXvLGJzZ7wI0LIsm4EZyc9MmtXWi4kKm0z2k6vDGFXGC7bQcd8E/0py6jCApEhU5wMivK7/wCIFlqdxpsi2VxZi0u1muMMH3IOMDoSfb3rR1Hxtpd2lmdPugr/AGuMzCSNl2x55Jzxj1pe47j95Hohukc5MwOetK8kaAZz9a5HUvEVtZ3Gk/YLu1u47i7EbiKRW+XIHPp1re1e+GlTafGUO+8maKPjjIRiP1xUvlT0KV+oaDrVvqumNNDLws8kZ3D0Ykc/QisD4ihX8LS4KufOj7+5rE8Ja1BZeE7u6uWYIuoRqqjk5faW/TNavj1Ej8PTASlsuhAx6OB/WoWw+p5EU+fG1ev9RU0aPuUYUcjoPpTGbDrx0Of5VOjYJbgHI6/QVg2aIjvIyDw7NyQdxz61UQHcQEBI98VcvD8544yePzqqpAZjjjGaaEz2o6nJKAS7HIBqX+0Z26yMO3Ws63t2a0hkMqjdGp/NRQyY6zZ+grrVrHPqXGlZiWB/HNOM+OCwJqgrIvVifxpGmiz3/OmB5CHvB1VW/CpYr+6t3V0SSNkOVaN2Ug9MjHTqfzp4VFH3mH/Aqd5sY6uo/GsNS7jY9YZJmkbJkL+YzSIrlm565HPU8VEtxCy4c4OckkVNviOcsp/EUwpbt2j/AAxQFxQLZhj5cswIIYcClMAAyHYc4GeRiojawsxwccdmpPsYH3JWH40guiXE67VWX7x6dPzqUS3OVZ4w/cAjIIH/AOqqn2e4zlZs44Gc07deJyVRvpSsO/mXpNRMt5JcXNuhkcbjgbVz0yAOKmh1S1DANHJHiLysoRnOR83I9v161jDz7h9gRt2MBd2MD8aaJSXyQeH5+Xjj1p6Duzfi1IM0SqUBEflCTOAgPBOMH86bLpkHlq39pwSMVLGMMTtOSAM9DwM9B1ArMWSzfljtJ59MelO8uNl+WYdOgbv+dLlQ+ZotzWUkd/HEFQtyMRsH6cdV47j86iRdrIrBgfMyAwKnbxjg+1RIlxHtKSFSORg4x9KleS7llV5G86QYAZzk9PfNS4dhqZBOo84MQQpzjg889q0A6rar8nHUj8aqTGZRC00Z2+XlMHgLk/1zSveQssYji8oKo3FSSZDg8n656e1LkZSkinaqpkZmIx1GD7ikkBM8Yj+7hc/nWhb/ANmwedlpXJRVjIGOcckjJ744zjGarRWrTXOS8ahFDEuwUHHYep9B3p2YXH3iIIIMDILhc/Wo4Ila6ZCqnAH06Vp2mmvqdxBGmfLjdfMKL82Ofug9TWrq8kOiRyW+laT5V1GMXM1yrSSIB0BDAAE8np2qoU3Jb2E2rnKKjiJHBcBjtz+OKv2zRxG5WZtypECoLAHJPGM+4Bq7olxdXF+0N9JJIwJZlkPtjGOnBrUvrSxEkKNagmd9hKDHGO/6VFndoqSUbHKSNIVV/lIkJwBxgYpm5thYp8qkY5zg59K6m60K0EDNFvUxqzIAcjOKzbbw7dNYgSyJHKW3FSOnQ9RT1J0MYFdkgw4JHz8UKyfvCGALrjHpWs+gXsUc4UI+8YXa3t71TfTbyIzF7eQfJgHGc8Gi47FZUA8zbjDLgeo96sRX17CAY7y4HksGhPmE7D0JAzxxVRIwGkyo+WPP44NCoCsvzMNoGBmjmFY0re/8vT7ixLPsMqTR4Y7dw4zj/drW1bWIb62lRHaSVSoV5MkNzzjJyOQD+VcysZEyLvIDIc9PSlxIJzE0hKDnGaLgJvYPjamRjBK59KkEl0R8mR7hB/hUcg8s4DN+Zp2MuA7MeR9O9SMS6JJ3rMzE/wB5s5z7GqyyyFiMDOPSrNzFHtkdQAT7D2qEW7rDFLvGJN2AG5GPX0zz+VUhHs+jrFd6HZTFhkwIDjjkKAf1FTvZIWIDL+JrE8GtbweD4ZLiYIiySgl2xj5z61oWWs6Tc70S8RSvdzs6+mcZ710xehg0x02nsoz8pB96qNbkHGz9a2rmOIWMkiXGW2FkIAI6darNAnHz546mmmFjwpbe4fhWjpzWV8OQin6EVcgfyO24/WrYv1x8yEemDXoz4dzSC5vZX+af6lxqUn1MJ0u48743H/AaiM0qnk4PvXQm6icqTvG0g4xnNN8+EgBlLcY5UH0/+vWH9i5l/wA+WPnp9zA8+T1/SgXMg7j8q2vIs53C+Tgk9VGO5z09qifRlyQpkXHqM+5rjxOGrYWShXi4t66jjaWxlm6lOMNjHpTheTj/AJatirEuk3EaFwu5evy9fXpVRoSh2sCrdcGsLjsTx6hNHIHSR0Ycbgealt9SeFZAMYkXa2VzxVHZ3zSFcd6ANQX1u334oz+GKeHs5OqEfRqx+lGaZNjbEVsT8k7p+lSrDMR+7ut315rBDsOjEfjUiXEgP3qLhZm1i8Bx+6cY54prG5BBe3U4OflqhHqcyEAk/nn+dXI9WQ4DqPw4p3FZknnJjElu646HFHmWbHjch/EVYS5glHEpQ+5x/wDWprxTAEo0cns6j+YpiuEJtfMRluWQAjJVuRz2/DFLIJ5WEj3JlYDhnYsenT+lU5JVjYia1T9RTQ1qwGIHGefkcHilcZetri5sLgyxKm4ArkjIIPP41oz6o98kEq2oDJg583HPfiufYRuCIZJgcZwasQWMgt1YTuDjpUvQpO+5qT627eWjpKqFSs8bPuB4IBU4z3B57itGLxDZtCBNJKsmzkog+9jtnjrXNRyTp8oniYgn7zYP+eKVmuNoHkRPnuCDTtoLm1OrTWbSRhiZACuec8H09P8A9VSW+ow3UbPDvOE3YC89+w5yMVx5bnD2TD/dFML22eYpkP0NMLkhhlihaV4WCyIdpxweSP51E2ITPGxyw445FNaSIkhJiqkdH7/54qSMIrkx3MXIIBK+tTylcyG+YgljbLYAIPB7ikDg3m/cfLxxkHrih4GLLIpRtg42txjGOlTQ5iQ5sxI5PDk5wPTFLlYcyIXYMM5A4pxZS4bfx9Pr/jTmlR9xkiZX55C8E9OR2HWjfbeXEN7bycSZUAL05Hc96OVjuiKaVSrYDdOpA9vepXvHksIlaXK52BcdAg49x1qu4Ek03+knyVGAz4y30Hpx/KtrS9OhFiGuYNzFiw+Tn2x6j3rOrP2Ubs7MDg5Yyr7KLto31e3krsqR3yf2ctvIWk2uxRJMlFBPZfc9ahWaATEvaxMrHbtYce1bMdpbvLtewCLwN5weD1/KoTCoPy6PnHT5lrH60u34r/M9P/V6p/P/AOSVP/kTrxr9rbaJCrR/vPICohGN3GBj2rLXxo4jQfZIvujOHNZSySIoVdNbGMAbl4qaO0g8tT9nVCQCV9KUseopafiv8zSjwtWrNqM184zX5xRG2iOykBYefQYNVm0GVe2R7OP8K6oeppHPHJAFe1RzPG0U1TqyV/P/ADPmHGL3RyDaWUPzxS/UMKY9lCo6zL9VrqXyOeo+lQOFJ6fp0rT+3My/5/MXs4djnFtrded5JH+1irPk7n4cjJztBznjpWq0ET8HBP0BqvLYRHO2H8QtcOKxdfFSU68nJrTU0ilHYrMrbyNzBfL2bTgnkYz1+tRT24uItjKJRsULvQgg+vfFTNYqOjsM88MRSeRKD8szZz3wf5iuUq5i3mjyJueFBtX+At8x+nrWUUYdUPPp2rrvLuUJIlXPuuM/kazr60HmmV4YyX6lc8nv1q4y6CZzzDk8EU3pWhNbRqeFwDz3qq0QBPJq0IhBpe9KU96TaaYC0E59KNpowfxoEOV2XoStWoNQmh78VTwRxRyOgJFAbm/FfQXS7ZAuf0/+tTZrPyWMqcrgD3AzWGpKHIz+ArVsL8jCOePftT3JatsSMV3Fkx93kelaMR/dKO1UbpFg3uuNhGcehoivW8sfKuP97FS1YqOupXljLJvXG9ic85xzT47B2fcThewxip4USKMzSd+QOtULrUp5CVjBRf1qrWJ3ehoGGC3wZJ2B/wB8iom1O1jJ2szVhsWblsk+9N5ouPlNd9XiPHk5+tQtqMLdbVPyrN/OjNK4+VF/7Zbn/l3x9CRT1urb/psn0es3NHei4WNmOSN/uXkg/wB7FPlWaNNxkVlPcx5/lWGDj296niu5YTgMcelFxcpe8xSOtufzFOiuruGB1icom7OFfGPpUSlLhC6DDj7y+tP3KCwyOtEkmtS6dSdN3g2n5FyO+uGH+snbjn95/wDXqVbubZuD3R/4ED/7NVWJgTnj8qnVlCn7p9qn2cOyNvrmI/5+S+9lhLqWRcLcOG7qWwR/n8qmS+uUXa83IJxmPnH4DmqBCOcFRn2PSpMSj7sgx/tdaPZxXRfcH1zEf8/Jfezr/tyLgFCv4imPfxZwwx7Z5rDjucOQrsq5+9u/kGpWuYyzDzxkdS7KK0sjmNNri3JyN3HqM0z7TAp5yf8AgNYrXILnbKGGcZx/hTVuiTt+cc9ccYpcqA3vtluvzBmX/gPSo5b6DGWm255+7waxmvI1Uhj9cCqT3KbjhieOPlH8qlpDN/7XCQCGyM9SxH4U03sBb5XTJ965p7p2/hxkZJJ71Cbl2ORx7YqOVFHW/aIj/wAtUUdwxFZWpX0kUu1VjeLgq2MHPesZrmQrwfyqJpZWOWJx9KFEGWZLwStnywKgaaPJGDULMT6flUZxnrirJJyUJ4NJtU9xUH40c9jQMsBKTZUSkg9+vNKZGFMQ/bS7T6U0SnPIpROMcjmgBwQ1KqEcjqOlRpcL/EMVKlzFkZBx60AW5JPMslBq3Go8qPgdBWY8qMojVweSc/jTgw4G84FDBFieaIZRmIOcYxxVFzExOHHXFOufuh0k3eoPaqbEk9KQErBezCmFR61GaM80xjivvSbabzjvRzz1pALto203n1pfm9aAHbPalCe1NBcDrTldx6UASxBonVhxzVlEVjMSefrVUPMQcDcPYUqPOu791knqdtFxF6LoMGpgcc85qgks46W2R7A1fsb1IZt1xpbTrg4XcVGfyOaLgPVzxyfypxPJ+b9KjtryxglfzLKcRNyE3ZKn61ZGoaN/FDdKT2BB/rRzBYgtOj/7wqndfeX6miirYhyf6mT6imt9+SiikMktv4/wpL//AFn4UUUmMorSjoaKKgZXPel9frRRTENP3h9KQ96KKYDacKKKAHil70UUxBTaKKAG9zTv8aKKAHL1p46GiigY9vuVD3oopCFPemCiimMXsacOjfSiikA0U6iigBy9asR9R9aKKTA1I+n5U7vRRWYDu/5VKn3qKKAIF/1rfWom60UUAf/Z"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAASAEQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDxMyNJBuKLjzMcDnOP/rVLZQrMJ23QoEjIxIwyS3AwPr1PanrciC2WG3iMbYO6QklmbBGRxwPb8+1XoZLT+z5x9r+V3DeQ4YCJs8njO7I4zx9KLA9iG1sowu+4vbWHqQpmUk/lnFEdpbG4XfqtusSphpAjvg8n7oHPXrVz+12eziEt+0ksN0GSNnOwRhcZAxySTj2C9KzIppo/NRHTy5AVIYjkYx+dUrE2l1L76dYwOGfWcFWUHzLKZSAen6ZPuBTnsNEgcAa+srHklLN2QH0znP6U25XUNWxPIsZDKoG07QdvAqm+k3qk5ijPGOZAMUWQdTXgdorcRjVLcw4+UMkwwOv9w5/E0y8ELxRrFc2cQVs/69wefXevNQ6To8mpXL2088djHDbtK87AyJx1Bx93NNGhSzXcdqlxHukLLvfKKAOpbqQMe1KyCwscToCPtNm3Ocmdc0VVWzUKAt0ij/audmfcAr09+9FLkHyilF+zn5R99e3vVdABcy4HQ8UUUyYkcwH23GP4Qf0qeNF/uj8qKKC2M8tNrHYufXFWoY0IXKKfqKKKYhR8sx28YI6fWpYwE1G+VAFURggDjnPWiijoXEt3xLtbhzuCwIq55wMdB7UUUVuiWf/Z"></div><hr><div><b><span style='color: blue;'>BOX1</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAASAEQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDxMyNJBuKLjzMcDnOP/rVLZQrMJ23QoEjIxIwyS3AwPr1PanrciC2WG3iMbYO6QklmbBGRxwPb8+1XoZLT+z5x9r+V3DeQ4YCJs8njO7I4zx9KLA9iG1sowu+4vbWHqQpmUk/lnFEdpbG4XfqtusSphpAjvg8n7oHPXrVz+12eziEt+0ksN0GSNnOwRhcZAxySTj2C9KzIppo/NRHTy5AVIYjkYx+dUrE2l1L76dYwOGfWcFWUHzLKZSAen6ZPuBTnsNEgcAa+srHklLN2QH0znP6U25XUNWxPIsZDKoG07QdvAqm+k3qk5ijPGOZAMUWQdTXgdorcRjVLcw4+UMkwwOv9w5/E0y8ELxRrFc2cQVs/69wefXevNQ6To8mpXL2088djHDbtK87AyJx1Bx93NNGhSzXcdqlxHukLLvfKKAOpbqQMe1KyCwscToCPtNm3Ocmdc0VVWzUKAt0ij/audmfcAr09+9FLkHyilF+zn5R99e3vVdABcy4HQ8UUUyYkcwH23GP4Qf0qeNF/uj8qKKC2M8tNrHYufXFWoY0IXKKfqKKKYhR8sx28YI6fWpYwE1G+VAFURggDjnPWiijoXEt3xLtbhzuCwIq55wMdB7UUUVuiWf/Z">, <b><span style='color: darkorange;'>object</span></b>='LEFT')=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAASAEQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDgr29jsYVklV2DNtAQZOcH/Cq9vrVpcrIQSnlgHDlQTk44Gef6VPqEE9xbhLd1STPViRjgjt9arLpbx200Il3JIQ6xkkLG275j75HGeK8ahDDyheo9T9KzXFZvTxDjg4XhZdL6lpNQtGj3SXMMP+y8qk/oTSx39pNKI4bhJGPZc/Wo9moPbQpNdNJJFcB0VpCUVAuOmOWJPXsAKq2GnXlpd72kiMJ+8ATnpj09a1qU8Iotxepx4TGZ/KvBVqdotq+i2vr+Aup21o9zHPPqC27KFXa0Dvxk85Xj1468VWew0SBwBr6yseSUs3ZAfTOc/pU+rWdxdTr5QBTaBy2OQT/jWU+k3qk5ijPGOZAMV3YZL2MT5TPP+RjW9TXgdorcRjVLcw4+UMkwwOv9w5/E0y8ELxRrFc2cQVs/69wefXevNQ6To8mpXL2088djHDbtK87AyJx1Bx93NNGhSzXcdqlxHukLLvfKKAOpbqQMe1b2R5VhY4nQEfabNuc5M65oqqtmoUBbpFH+1c7M+4BXp796KXIPlOpooor5k/cgooooAwtbRTdBioJEY5I9zVaGNCFyin6iiivoML/Bifkeef8AIxq+oo+WY7eMEdPrUsYCajfKgCqIwQBxznrRRXR0PMiW74l2tw53BYEVc84GOg9qKKK3RLP/2Q=="></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAASAEQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDgr29jsYVklV2DNtAQZOcH/Cq9vrVpcrIQSnlgHDlQTk44Gef6VPqEE9xbhLd1STPViRjgjt9arLpbx200Il3JIQ6xkkLG275j75HGeK8ahDDyheo9T9KzXFZvTxDjg4XhZdL6lpNQtGj3SXMMP+y8qk/oTSx39pNKI4bhJGPZc/Wo9moPbQpNdNJJFcB0VpCUVAuOmOWJPXsAKq2GnXlpd72kiMJ+8ATnpj09a1qU8Iotxepx4TGZ/KvBVqdotq+i2vr+Aup21o9zHPPqC27KFXa0Dvxk85Xj1468VWew0SBwBr6yseSUs3ZAfTOc/pU+rWdxdTr5QBTaBy2OQT/jWU+k3qk5ijPGOZAMV3YZL2MT5TPP+RjW9TXgdorcRjVLcw4+UMkwwOv9w5/E0y8ELxRrFc2cQVs/69wefXevNQ6To8mpXL2088djHDbtK87AyJx1Bx93NNGhSzXcdqlxHukLLvfKKAOpbqQMe1b2R5VhY4nQEfabNuc5M65oqqtmoUBbpFH+1c7M+4BXp796KXIPlOpooor5k/cgooooAwtbRTdBioJEY5I9zVaGNCFyin6iiivoML/Bifkeef8AIxq+oo+WY7eMEdPrUsYCajfKgCqIwQBxznrRRXR0PMiW74l2tw53BYEVc84GOg9qKKK3RLP/2Q==">)=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'left' if ANSWER0 > 0 else 'right'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'left' if 1 > 0 else 'right'")=<b><span style='color: green;'>left</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>left</span></b></div><hr>

Answer: left
