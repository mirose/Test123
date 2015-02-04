#Name: Kiet Nguyen
#Email: mirose@csu.fullerton.edu

#Description:This program is designed to decipher a message that uses the Vigenere ciphering method.
#Follow instructions as prompted and the program will ask for -cipher.txt file in the directory you are running this .py file and the code.
#The program will then create a -clear.txt file in the directory you are running this .py file.

global alpha
alpha = "abcdefghijklmnopqrstuvwxyz"	#alphabet


def shift(n):  							#shifts alphabet based on inputed code
  shifted = alpha[n:26] + alpha[0:n]	#splices the alphabet depending on letter that is inputed from code and recombine
  return shifted						#returns shifted alphabet

def decipher(filename, code):
  i = 0										#iterator for message
  j = 0										#iterator for code
  k = 0										#iterator for coded message
  l = 0										#iterator for alphabet
  deciph = ''								#empty deciphered string
  coded = ''								#empty coded message string
  
  with open(filename + "-cipher.txt", 'r') as ciph: #opens "filename"-chiper.txt for reading as ciphered
    message = ciph.read()							#writes the ciph string into "filename"-chiper.txt
  ciph.closed										#closes file
  
  while i < len(message):					#while iterator for message is less than the len of message it will loop
    if message[i] == ' ':					#if there is a space it will add a space to coded and iterate to next
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
	  
      if message[k] == shiftAlpha[l]: 		#if kth character does match lth character in shifted alphabet
        deciph += alpha[l]					#adds lth alphabet to deciph string
		
      else:
        while message[k] != shiftAlpha[l]: 	#while kth letter does not match lth letter in shifted alpha
          l += 1					  		#iterates through shifted alphabet
          if message[k] == shiftAlpha[l]:  	#once message's letter matches shifted alphabet's letter
            deciph += alpha[l]      		#add letter from alphabet to deciph string
			
      k += 1								#iterates to next letter in coded message
      l = 0									#resets iterator for alphabet/shifted alphabet
	
    elif coded[k] == ' ':					#if there is a space in the coded message
      deciph += ' '							#add space to deciph string
      k += 1								#iterate to next character
	
    else:									#if kth coded character does not match lth alphabet character
      l += 1								#iterate to next character
  
  with open(filename + "-clear.txt", 'w') as cleared:	#opens "filename"-clear.txt for writing as cleared
    cleared.write(deciph)								#writes the deciph string into "filename"-clear.txt
  cleared.closed										#closes file
  
def main():
  menu_loop = True
  while menu_loop == True:
    print("\n\nWhat do you wish to be decipher, make sure you have the code.\n")
    filename = input("Enter the file name with out '-cipher.txt': ")  #user input
    code = input("Enter the code word/pharse in lower case: " )
    decipher(filename, code)			#deciphers the message
  
    print ("\nDeciphering completed, decipher another one?")	#prompts for another
    input_loop = True	#enable user prompt loop
	
    while input_loop == True:
      ans = input("Enter Y or y to decipher another, N or n to quit: ")
      if ans == 'y':  					#sets the letter casing
        ans = 'Y'
      if ans == 'n':
        ans = 'N'
  
      if ans == 'Y':					#menu repeats if Y was entered
        menu_loop = True				#just to make sure
        input_loop = False

      elif ans == 'N':					#quits menu
        menu_loop = False       		#ends menu_loop
        input_loop = False
		
      elif ans not in ('Y', 'N'):	#if anything not listed was entered
        print("Your answer was invalid.")
        menu_loop = True
        input_loop = True

if __name__ == '__main__':
  main()
