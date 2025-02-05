# on = False
# while True:
#     cmd = input('> ').lower()
#     if cmd == 'help':
#         print('''
#         1 - to on bulb
#         0 - to off bulb
#         quit - to exit
#         ''')
#     elif cmd == '1':
#         if on:
#             print('Bulb already on!')
#         else:
#             on = True
#             print('Bulb is on!')
#     elif cmd == '0':
#         if not on:
#             print('Bulb already off!')
#         else:
#             on = False
#             print('Bulb is off!')
#     elif cmd == 'quit':
#         break
#     else:
#         print("Sorry, I don't understand that...")
# # 
# on = False
# trial = 0
# while True:
#     cmd = input('> ').lower()
#     trial += 1
#     if cmd == 'help':
#         print('''
#         click - to On/Off bulb
#         quit - to exit
#         ''')
#     elif cmd == 'click':
#         if not on:
#             on = True
#             print('Bulb is On!')
#         elif on:
#             on = False
#             print('Bulb is Off!')
#     elif trial = 5:
#         break
#     else :
#         print("Sorry, I don't understand that...")

# on = False
# clicks = 0
# while clicks != 5:
#     cmd = input('> ').lower()
#     if cmd == 'click':
#         if not on:
#             on = True
#             print('Bulb is On!')
#         elif on:
#             on = False
#             print('Bulb is Off!')            
#         clicks +=1
        
        
# on = False
# clicks = 0
# while True:
#     cmd = input('> ').lower()
#     if cmd == 'click':
#         if not on:
#             on = True
#             print('Bulb is On!')
#         elif on:
#             on = False
#             print('Bulb is Off!')
#             
#         clicks +=1
#         if clicks == 5:
#             break            
# 

 
furniture = ['table', 'chair', 'rack', 'shelf']
print("run")
sn = [i for i in range(1, len(furniture )+1)]
for item, numbering in zip(furniture, sn):
    print(f'{numbering}. {item}')
    