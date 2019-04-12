def getInfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    compute(var1, var2)



def compute(var1,var2):
    try:
        var3 = int(var1) + int(var2)
        print("{} + {} = {}".format(var1,var2,var3))
    except ValueError:
        print("You did not provide a numeric value!")
    except:
        print("Program will close now.")





if __name__=="__main__":
    getInfo()
    
