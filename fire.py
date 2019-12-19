from firebase import firebase

#
firebase = firebase.FirebaseApplication('https://e-trac-5d530.firebaseio.com/', None)
data =  { 'forward': False,
          'reverse': False,
          'left': False,
          'right' : True,
          'speed' : 0,
          'pwm' : 0,
          'pwm_lr':0
          }
result = firebase.put('/', "forward" , False )
result = firebase.put('/', "reverse" , False )
result = firebase.put('/', "left" , False )
result = firebase.put('/', "right" , False )
result = firebase.put('/', "speed" , 0 )
result = firebase.put('/', "mode" , "Manual" )
result = firebase.put('/', "pwm" , 0 )
result = firebase.put('/', "pwm_lr" , 0 )
print(result)
result = firebase.get('/', '')
print(result)
