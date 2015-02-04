#Name: Kiet Nguyen TEST
#Email: mirose@csu.fullerton.edu

#Description: This program is designed to cipher a message, default or user defined, using the Vigenere ciphering method.
#Follow instructions as prompted and the program will create a -cipher.txt file in the directory you are running this .py file. 

global alpha
alpha = "abcdefghijklmnopqrstuvwxyz"	#alphabet


def shift(n):  							#shifts alphabet based on inputed code
  shifted = alpha[n:26] + alpha[0:n]	#splices the alphabet depending on letter that is inputed from code and recombine
  return shifted						#returns shifted alphabet

def cipher(message, filename, code):
  i = 0										#iterator for message
  j = 0										#iterator for code
  k = 0										#iterator for coded message
  l = 0										#iterator for alphabet
  ciph = ''									#empty ciphered string
  coded = ''								#empty coded message string
  
  while i < len(message):					#while iterator for message is less than the len of message it will loop
    if message[i] == ' ':				#if there is a space it will add a space to coded and iterate to next
      coded += ' '							#character in message
      i += 1
    
    else:									#if it is not a space than it will add whatever letter the iterator for
      coded += code[j]						#code to coded

      if j == (len(code)-1):				#if the iterator hits the max length-1(because numbering starts at 0)
        j = 0								#iterator is reseted
      else:
       j += 1								#if it is not at max length-1 then it will iterate to next letter in code
	   
      i += 1								#iterate to next character in message
  
  while k < len(coded):						#whie iterator for coded is less than the len of coded message
	
    if coded[k] == alpha[l]:				#checks if coded letter matches alpha
      shiftAlpha = shift(l)					#if it does it will shift it 
      l = 0									#reset iterator for alphabet
	  
      if message[k] == alpha[l]: 		#if kth character does match lth character in alphabet
        ciph += shiftAlpha[l]				#shifted alphabet to ciph string
		
      else:
        while message[k] != alpha[l]: #while kth letter does not match lth letter in alpha
          l += 1					  		#iterates through alphabet
          if message[k] == alpha[l]:  #once message's letter matches alphabet's letter
            ciph += shiftAlpha[l]      		#add letter from shifted alphabet to ciph string
			
      k += 1								#iterates to next letter in coded message
      l = 0									#resets iterator for alphabet
	
    elif coded[k] == ' ':					#if there is a space in the coded message
      ciph += ' '							#add space to ciph string
      k += 1								#iterate to next character
	
    else:									#if kth coded character does not match lth alphabet character
      l += 1								#iterate to next character

	  
  with open(filename + '-cipher.txt', 'w') as ciphered:	#opens "filename"-chiper.txt for writing as ciphered
    ciphered.write(ciph)							#writes the ciph string into "filename"-chiper.txt
  ciphered.closed									#closes file
	
def main():
  menu_loop = True
  message = "the eagle has landed"
  
  while menu_loop == True:				#menu runs until prompted otherwise
    print("\n\nWould you like to use a custom filename, and codeword/phrase?\n")
    print("Enter 1 if you wish to use the default.\n""Enter 2 if you wish to customize.")
    print("Enter 3 if you wish to use a customize everything.\n""Enter Q or q to quit.\n")
    ans = input ("Enter your choice: ")
    
    if ans == 'q':						#sets the letter casing
      ans = 'Q'

    if ans == '1':						#if 1 was enterd use these 
      filename = "message"
      code = "lime"
      cipher(message, filename, code)	#calls cipher
	  
      print("Ciphering completed, code is lime. Would you like to do a custom one?") # after compelteing ciphering ask to do a custom one
      ans = input("Enter Y or y to do a custom cipher, N or n to quit: ")
      if ans == 'y': 					#sets letter casing
        ans = 'Y'
      if ans == 'n':
        ans = 'N'
		  
      if ans == 'Y':					#sets it to custom ciphering
        menu_loop = True				#just to make sure
		  
      elif ans == 'N': 					#sets to Q to quit probram at the end of menu loop
        menu_loop = False
        break		
	  
    elif ans == '2':					#if 2 was entered user inputs filename and code
      filename = input("Enter the file name: ")
      code = input("Enter your own code word/pharse in lower case: " )
      cipher(message, filename, code)	#calls cipher
	  
      print("\nCiphering completed, here is the code you provided: ", code) 
      print("Would you like to do another?")  # after compelteing ciphering ask to do another
      ans = input("Enter Y or y to do another cipher, N or n to quit: ")
      if ans == 'y':  					#sets the letter casing
        ans = 'Y'
      if ans == 'n':
        ans = 'N'
  
      if ans == 'Y':					#menu repeats if Y was entered
        menu_loop = True				#just to make sure

      elif ans == 'N':					#quits menu
        menu_loop = False       		#ends menu_loop
        break
		
    elif ans == '3':
      message = input("Enter a lower-cased message: ")
      filename = input("Enter the file name: ")
      code = input("Enter your own code word/pharse in lower case: " )
      cipher(message, filename, code)	#calls cipher
	  
      print("\nCiphering completed, here is the code you provided: ", code) 
      print("Would you like to do another?")  # after compelteing ciphering ask to do another
      ans = input("Enter Y or y to do another cipher, N or n to quit: ")
      if ans == 'y':  					#sets the letter casing
        ans = 'Y'
      if ans == 'n':
        ans = 'N'
  
      if ans == 'Y':					#menu repeats if Y was entered
        menu_loop = True				#just to make sure

      elif ans == 'N':					#quits menu
        menu_loop = False       		#ends menu_loop
        break
	  
    elif ans == 'Q':
      menu_loop = False
	  
    elif ans not in ('Y', 'N', '1', '2', '3', 'Q'):		#if anything not listed was entered
      print("Your answer was invalid.")
	  

if __name__ == '__main__':
  main()
