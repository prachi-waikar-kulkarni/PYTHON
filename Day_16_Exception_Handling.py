'''
-- Anomalies handling, Error Handling especially when the error can't be anticipated.
                    -- Adv : Instead of interrupting the flow, we are informed of the error but the flow continues.

-- Syntax Errors can't be handles since aapka code hi nahi chalega.
'''
#try    : jaha hume lagta hai ki kuch gadbad ho sakti hai, tab try block me code likhenge
        # : Jaha pehla error aya wahi se it will go to the except block
#except :
#finally : This block will execute regardless there is an exception or not,
#        : We use this block to perform those actions which are import and must be performed.


#print(8/0)

#print(y)

y="Hello"
try:
    #print(y[40])
    #print("hello")
    #print(8 / 0)
    print(z)

except IndexError:
    print("Please ensure that the Index is less than the string length")
except ZeroDivisionError:
    print("Please ensure that the denominator is not zero")
except NameError:
    print("Please ensure that the variables are defined before you choose them")
except Exception as e:
    print("facing some issue",e)

finally:
    print("Program Ended")