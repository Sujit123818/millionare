questions=[
    ['who is tony stark','actor','hero','villain','zero',2],
    ['which is biggest animal','tiger','elephant ','dinoasaur','cat',3],
    ['what is 2','number ','alphabet','numeric','literals',1],
    ['what is the square root of 16','9','0','2','4',4],
    ['what is your name ','actor','hero','sujit','nabin',2],
    ['what is 2+3','0','hero','5','zero',3],
         ]
prizes=[10000,20000,30000,40000,50000,60000]
i=0
print(' enter the value  1 for a 2 for b 3 for c 4 for d:\n')
for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")


    a=int(input('Entet the answers:'))
    if a==question[5]:

        print('correct answers')
        print(f'you won {prizes[i]}')
        i +=  1
    else:
        print('incorrect answers')
        print('Better up next time:')
        break
if i==5:
   print('you are a  millionare')


