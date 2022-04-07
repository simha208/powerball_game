from  colorama import *
from logic import *

##-------List of all conditions in the game


class Conditions(Logic):
    def __init__(self):
        super().__init__()
        self.whiteball= self.lucklnum()
        self.lotory=self.winNumbers()
        
    def successes(self):
        count = 0
        for i in self.whiteball[0:5]:
            for c in self.lotory[0:5]:
                if i == c:
                    count += 1
        if count==5 and self.whiteball[5]== self.lotory[5]:
            return("Correct White Balls and the Powerball: Jackpot $324,000,000")
        elif count==5 and self.whiteball[5] !=self.lotory[5]:
            return("5 Correct White Balls, but no Powerball: $1,000,000 ")
        elif count==4 and self.whiteball[5]==self.lotory[5]:
            return("Correct White Balls and the Powerball: $10,000 ")
        elif count==4 and self.whiteball[5]!= self.lotory[5]:
            return("4 Correct White Balls, but no Powerball: $100 ")
        elif count==3 and self.whiteball[5]== self.lotory[5]:
            return("3 Correct White Balls and the Powerball: $100")
        elif count==3 and self.whiteball[5]!=self.lotory[5]:
            return("3 Correct White Balls, but no Powerball: $7")
        elif count==2 and self.whiteball[5]==self.lotory[5]:
            return("2 Correct White Balls and the Powerball: $7 ")
        elif count==1 and self.whiteball[5]==self.lotory[5]:
            return("1 Correct White Ball and the Powerball: $4 ")
        elif count==0 and self.whiteball[5]==self.lotory[5]:
            return("No White Balls, Just the Powerball: $4 ")
        else:
            return Fore.RED + "try" + Style.RESET_ALL + Fore.YELLOW + " again!"


    def __str__(self):
        return Fore.BLUE + "lucky numbers:"+ Style.RESET_ALL +"\n"+ Fore.GREEN +str(self.whiteball[:5])+Style.RESET_ALL\
               +Fore.YELLOW +str(self.whiteball[-1])+ Style.RESET_ALL +"\n"+ Fore.BLUE +"winning numbers:"+ Style.RESET_ALL\
               + "\n" + Fore.GREEN +str(self.lotory[:5])+ Style.RESET_ALL+Fore.YELLOW +str(self.lotory[-1])+"\n"+Style.RESET_ALL \
               +Fore.BLUE + self.successes()+ Style.RESET_ALL

