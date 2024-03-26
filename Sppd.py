#!/usr/bin/env python
# coding: utf-8

# In[6]:


from experta import *


class Comapny_Price():
    duration2_3=False
    duration4_6=False
    more=False
    
    pro2_3=False
    pro4_6=False
    
    _coast=0
    #---------static methods statimethod()
    def __init__(self,coast1):
        Comapny_Price._coast+=coast1
        
    @staticmethod
    def change_duration2_3():
        per=(Comapny_Price._coast*25)/100
        Comapny_Price._coast=Comapny_Price._coast+per
        Comapny_Price.duration2_3=True
        
        
    @staticmethod
    def change_duration4_6():
        per=(Comapny_Price._coast*15)/100
        Comapny_Price._coast=Comapny_Price._coast+per
       
        
    @staticmethod    
    def change_pro2_3():
        Comapny_Price._coast+=4000*2
        Comapny_Price.pro2_3=True
        
    @staticmethod    
    def change_pro4_6():
        Comapny_Price._coast+= 7500*4
        Comapny_Price.pro4_6=True
        
    @staticmethod    
    def change_duration_more_6():
        Comapny_Price._coast+= 7500*5
        Comapny_Price.more=True
    




class Sppd(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="Q")
    @Rule(Fact(action='Q'), NOT(Fact(Q_Freelance=W())))
    def IsItApplicatio(self):
        self.declare(Fact(Q_Freelance=input("Are you a Freelancer ? ")))
        #Freelancer
    @Rule(Fact(Q_Freelance='y'), NOT(Fact(WebApplication=W())))
    def IsItWebapp(self):
        self.declare(Fact(WebApplication=input("Do you want to set a price for a Webapplication ? ")))
    @Rule(Fact(WebApplication='n'), NOT(Fact(Q_mobileApplication=W())))
    def mobileapp(self):
        self.declare(Fact(Q_mobileApplication=input("Do you want to set  price for a MobileApplication ? "))) 
        #0-3 features
    @Rule(Fact(Q_mobileApplication='y'), NOT(Fact(F0_3=W())))
    def F0_3(self):
        self.declare(Fact(F0_3=input(" Does the application contains 0-3 Features Like Essential features like profile making, search, notifications, and messages, Fewer screens ? ")))
    @Rule(Fact(Q_mobileApplication='n'))
    def out_1(self):
        print( "\n Sorry, but this app only for web and mobile applications")
        
    @Rule(Fact(F0_3='y'), NOT(Fact(dt2_3=W())))
    def dt2_3(self):
        self.declare(Fact(dt2_3=input("Does the Development time btw 2-3 months ? ")))
    @Rule(Fact(dt2_3='y'))
    def ma0_3fdt2_3(self):
        print( "\nAs an average 7$ for an hour this app will cost 364$-546$")
    @Rule(Fact(dt2_3='n'), NOT(Fact(dt3_6=W())))
    def dt3_6(self):
        self.declare(Fact(dt3_6=input("Does the Development time btw 3-6 months ? ")))
    @Rule(Fact(dt3_6='y'))
    def ma0_3fdt3_6(self):
        print( "\nAs an average 5$ for an hour this app will cost 260$-390$")
    @Rule(Fact(dt3_6='n'), NOT(Fact(dt9_m=W())))
    def dt9_m(self):
        self.declare(Fact(dt9_m=input("Does the Development time  9 or more months ? ")))
    @Rule(Fact(dt9_m='y'))
    def ma0_3fdt9_m(self):
        print( "\nAs an average 2$ for an hour this app will cost 200$ or less")
    @Rule(Fact(dt9_m='n'))
    def ma0_3fdt9_mn(self):
        print( "\n 2$ in an hour ")
        
        #4-5 features
        
    @Rule(Fact(F0_3='n'), NOT(Fact(F4_5=W())))
    def F4_5(self):
        self.declare(Fact(F4_5=input("Does the application contains 4-5 Features Like more than the previous and :Essential features, in addition to in-app purchases and payment portalsAllows API integrationMore screens than the basic versionCustom UIReal-time messaging and other features ? ")))
    @Rule(Fact(F4_5='y'), NOT(Fact(dt3_6_2=W())))
    def dt3_6_2(self):
        self.declare(Fact(dt3_6_2=input("Does the Development time btw 3-6 months ? ")))
    @Rule(Fact(dt3_6_2='y'))
    def ma4_5fdt36(self):
        print( "\n As an average 7$ for an hour this app will cost 546$-1,100$")
    @Rule(Fact(dt3_6_2='n'), NOT(Fact(dt9_m_2=W())))
    def dt9_m_2(self):
        self.declare(Fact(dt9_m_2=input("Does the Development time 9 or more  months ? ")))
    @Rule(Fact(dt9_m_2='y'))
    def ma4_5fdt9_m(self):
        print( "\nAs an average 5$ for an hour this app will cost 468$-less")  
        #5-more features
    @Rule(Fact(F4_5='n'), NOT(Fact(F5_m=W())))
    def F5_m(self):
        self.declare(Fact(F5_m=input("Does the application contains more than 5 Features Like 0the previous and :Multi-functional appsAdvanced features like real-time synchronizationUI animationMedia processing")))
    @Rule(Fact(F5_m='y'), NOT(Fact(dt9_m_3=W())))
    def dt9_m_3(self):
        self.declare(Fact(dt9_m_3=input("Does the Development time 9 or more  months ? ")))
    @Rule(Fact(dt9_m_3='y'), NOT(Fact(dtm_3=W())))
    def ma4_5fdt3_6(self):
        print( "\nAs an average 7$ for an hour this app will cost 1,800$")
    @Rule(Fact(dt9_m_3='n'))
    def dtm_3(self):
        print( "\n 7$ for an hour and 6h work a day in month your salary 182$")
        #high performance requierments
    @Rule(Fact(F5_m='n'), NOT(Fact(hp=W())))
    def hp(self):
        self.declare(Fact(hp=input("does it need high performance requierments ? ")))
    @Rule(Fact(hp='y'))
    def hp1(self):
        print( "\n Native app price btw  1000$-3000$ depending on features")
        #high resources
    @Rule(Fact(hp='n'), NOT(Fact(hr=W())))
    def hr(self):
        self.declare(Fact(hr=input("does it need high resources ? ")))
    @Rule(Fact(hr='y'))
    def hr1(self):
        print( "\n Hybrid app price btw  2000$-6000$ depending on features ")
        #freelancerlvl
    @Rule(Fact(hr='n'), NOT(Fact(bf=W())))
    def bf(self):
        self.declare(Fact(bf=input("Are you a beginner ? ")))
    @Rule(Fact(bf='y'))
    def bf1(self):
        print( "\n your hourly rate is btw 3$-7$ ")
    @Rule(Fact(bf='n'), NOT(Fact(iff=W())))
    def iff(self):
        self.declare(Fact(iff=input("Are you an intermediate ? ")))
    @Rule(Fact(iff='y'))
    def iff1(self):
        print( "\n your hourly rate is btw 15$-30$ ")
    @Rule(Fact(iff='n'))
    def iff2(self):
        print( "\n You can set your hourly rate  as it common in some regions with high experience \n E-Europe 30-50$ \n USA-120$-150$ /n SYRIA 3$-15$" )
    
    #freelance_web_side
    
    @Rule(Fact(WebApplication='y'), NOT(Fact(Q_server_domain=W())))
    def server_and_domain(self):
        self.declare(Fact(Q_server_domain=input("Setup on server and map to domain? "))) 
    @Rule(Fact(Q_server_domain='y'), NOT(Fact(Q_page_num5_10m=W())))
    def page_num5_10m(self):
        self.declare(Fact(Q_page_num5_10=input("Contains 5-10 and more pages ? "))) 
    @Rule(Fact(Q_page_num5_10='y'), NOT(Fact(Cookies=W())))
    def Cookies(self):
        self.declare(Fact(Cookies=input("Contains Cookies and privacy policy ? "))) 
    @Rule(Fact(Cookies='y'), NOT(Fact(ux1=W())))
    def ux1(self):
        self.declare(Fact(ux1=input("Does it have UI/UX ? "))) 
    @Rule(Fact(Cookies='n'), NOT(Fact(ux2=W())))
    def ux2(self):
        self.declare(Fact(ux2=input("Does it have UI/UX ? "))) 
        
    @Rule(Fact(ux1='n'), NOT(Fact(animation33=W())))
    def animation33(self):
        self.declare(Fact(animation33=input("Does it have Animation ? "))) 
    @Rule(Fact(animation33='n'))
    def animation33_ans(self):
        print( "\n The price would be $400-1500 depending on number of pages ")
    @Rule(Fact(animation33='y'))
    def animation33_ansn(self):
        print( "\n The price would be $400-1500 depending on number of pages ")
        
    @Rule(Fact(ux2='y'), NOT(Fact(interapp2=W())))
    def interapp2(self):
        self.declare(Fact(interapp2=input("Is it an integrated web app  ? "))) 
    @Rule(Fact(ux2='n'), NOT(Fact(animation2=W())))
    def animation2(self):
        self.declare(Fact(animation2=input(" Does it have Animation  ? "))) 
    @Rule(Fact(animation2='n'))
    def animation2ans(self):
        print( "\n The price would be $ 500-1000  depending on number of pages")
    @Rule(Fact(animation2='y'))
    def animation2anss(self):
        print( "\n The price would be $ 500-1000 depending on number of pages ")
    @Rule(Fact(interapp2='y'))
    def interwedapp2(self):
        print( "\n The price would be $500-1500 depending on number of pages")
    @Rule(Fact(interapp2='n'))
    def interwedapp22(self):
        print( "\n The price would be $500-1000 depending on number of pages ")
    @Rule(Fact(ux1='y'), NOT(Fact(interapp1=W())))
    def interapp1(self):
        self.declare(Fact(interapp1=input("Is it an integrated web app  ? "))) 
    @Rule(Fact(interapp1='y'))
    def interwedapp(self):
        print( "\n The price would be $500-2000  depending on number of pages")
    @Rule(Fact(interapp1='n'))
    def interwedapp1(self):
        print( "\n The price would be $500-1500  depending on number of pages ")
    @Rule(Fact(Q_page_num5_10='n'), NOT(Fact(q_p1_5=W())))
    def q_p1_5(self):
        self.declare(Fact(q_p1_5=input("Contains 1-5 pages  ? "))) 
    @Rule(Fact(Q_server_domain='n'), NOT(Fact(page_num1_5=W())))
    def page_num1_5(self):
        self.declare(Fact(page_num1_5=input("Contains 1-5 pages  ? "))) 
    @Rule(Fact(page_num1_5='y'), NOT(Fact(animation1_5ns=W())))
    def animation1_5ns(self):
        self.declare(Fact(animation1_5ns=input("Does it need Animation ? "))) 
    @Rule(Fact(page_num1_5='n'), NOT(Fact(beginner=W())))
    def beginner(self):
        self.declare(Fact(beginner=input("Are you a beginner? "))) 
    @Rule(Fact(beginner='y'))
    def beginnery(self):
        print( "\n your hourly rate is btw 3$-7$ ")
    @Rule(Fact(beginner='n'), NOT(Fact(intermediate=W())))
    def intermediate(self):
        self.declare(Fact(intermediate=input("Are you an intermediate ? "))) 
    @Rule(Fact(intermediate='y'))
    def intermediatey(self):
        print( "\n your hourly rate is Between 15$-30$ ")
    @Rule(Fact(intermediate='n'))
    def intermediaten(self):
        print( "\n You can set your hourly rate  as it common in some regions with high experience \n E-Europe 30-50$ \n USA-120$-150$ /n SYRIA 3$-15$")
    @Rule(Fact(animation1_5ns='y'))
    def animation1_5nsend(self):
        print( "\n The project price for web page costs 50$-80$ for each page ")
    @Rule(Fact(animation1_5ns='n'), NOT(Fact(txt_img=W())))
    def txt_img(self):
        self.declare(Fact(txt_img=input("Does it have image ,text and no complicatied data ? "))) 
    @Rule(Fact(txt_img='y'))
    def txt_img_ans(self):
        print( "\n The project price for web page costs 10$-30$ for each page")
    @Rule(Fact(txt_img='n'))
    def txt_img_ansn(self):
        print( "\n The project price for web page costs 5$-10$ for each page")
        
      
    @Rule(Fact(q_p1_5='n'))
    def q_p1_5ans(self):
        print("No other soultions try again !!!")
    @Rule(Fact(q_p1_5='y'), NOT(Fact(cookeiss1_5p=W())))
    def cookeiss1_5p(self):
        self.declare(Fact(cookeiss1_5p=input("Contains Cookies and privacy policy  ? "))) 
    @Rule(Fact(cookeiss1_5p='y'), NOT(Fact(ux1_5pn=W())))
    def ux1_5p(self):
        self.declare(Fact(ux1_5pn=input("Does it have UI/UX ? "))) 
    @Rule(Fact(ux1_5pn='y'), NOT(Fact(dbms1_5p=W())))
    def dbms1_5p(self):
        self.declare(Fact(dbms1_5p=input("Does it need DBMS ? ")))
    @Rule(Fact(dbms1_5p='y'), NOT(Fact(integrated1_5p=W())))
    def integrated1_5p(self):
        self.declare(Fact(integrated1_5p=input("Is it an integrated web app  ? ")))
    @Rule(Fact(integrated1_5p='n'))
    def integrated1_5pnans(self):
        print("The price would be 1000$-3000$ depending on number of pages")
    @Rule(Fact(integrated1_5p='y'))
    def integrated1_5pyans(self):
        print("The price would be 1000$-5000$ depending on number of pages")
    @Rule(Fact(dbms1_5p='n'))
    def dbms1_5pnoans(self):
        print("The price would be 500$-2000$ depending on number of pages")  
    @Rule(Fact(ux1_5pn='n'), NOT(Fact(animation1_5pp=W())))
    def animation1_5pp(self):
        self.declare(Fact(animation1_5pp=input("Does it have Animation ? "))) 
    @Rule(Fact(animation1_5pp='y'), NOT(Fact(integrated1_5p2=W())))
    def integrated1_5p2(self):
        self.declare(Fact(integrated1_5p2=input("Is it an integrated web app  ? "))) 
    @Rule(Fact(integrated1_5p2='y'))
    def integrated1_5p2ans(self):
        print("The price would be $500-$1000 ? ")
    @Rule(Fact(animation1_5pp='n'), NOT(Fact(integrated1_5p3=W())))
    def integrated1_5p3(self):
        self.declare(Fact(integrated1_5p3=input("Is it an integrated web app  ? ")))
    @Rule(Fact(integrated1_5p3='y'))
    def integrated1_5p33(self):
        print("The price would be 500-1000 ")
        
    @Rule(Fact(integrated1_5p3='n'))
    def integrated1_5p3ansn(self):
        print("The price would be 500$-1000$ depending on number of pages")  
    @Rule(Fact(cookeiss1_5p='n'), NOT(Fact(uxco=W())))
    def uxco(self):
        self.declare(Fact(uxco=input("Does it have UI/UX  ? "))) 
    @Rule(Fact(uxco='y'), NOT(Fact(interco=W())))
    def interco(self):
        self.declare(Fact(interco=input("Is it an integrated web app   ? "))) 
    @Rule(Fact(interco='y'))
    def intercoansy(self):
        print("The price would be $500-1000   ? ") 
    @Rule(Fact(interco='n'))
    def intercon(self):
        print("The price would be $200-600")
    @Rule(Fact(uxco='n'), NOT(Fact(anemationco=W())))
    def anemationco(self):
        self.declare(Fact(anemationco=input("Does it have Animation   ? "))) 
    @Rule(Fact(anemationco='n'), NOT(Fact(interconoain=W())))
    def interconoain(self):
        self.declare(Fact(interconoain=input("Is it an integrated web app    ? "))) 
    @Rule(Fact(interconoain='n'))
    def interconoainna(self):
        print("The price would be 200-800  ")
    @Rule(Fact(anemationco='y'), NOT(Fact(interconoainy=W())))
    def interconoainy(self):
        self.declare(Fact(interconoainy=input("Is it an integrated web app    ? "))) 
    @Rule(Fact(interconoainy='y'))
    def interconoainyyana(self):
        print("The price would be $500-1000 ")
        
        #end of freelancer tree 
        
         #-- company path
    @Rule(Fact(Q_Freelance='n'), NOT(Fact(company_start=W())))
    def company_start(self):
        self.declare(Fact(company_start=input("Are you a Start-up company ? ")))
        
    @Rule(Fact(company_start='y'), NOT(Fact(Q_SRS=W())))
    def Q_SRS(self):
        self.declare(Fact(Q_SRS=input(" Does the Customer Needs SRS  ? ")))
        
    @Rule(Fact(company_start='n'))
    def exi_t(self):
        print(" Sorry,but this application only for pricing freelance and start-up companies  ? ")
    
    @Rule(Fact(Q_SRS='y'), NOT(Fact(Q_BRS=W())))
    def Q_BRS1(self):
        Comapny_Price(100)
        self.declare(Fact(Q_BRS=input(" Does the Customer Needs BRS  ? ")))
        
    @Rule(Fact(Q_SRS='n'), NOT(Fact(Q_BRS=W())))
    def Q_BRS2(self):
        self.declare(Fact(Q_BRS=input(" Does the Customer Needs BRS  ? ")))
                                      
    @Rule(Fact(Q_BRS='y'), NOT(Fact(Q_isWeb=W())))
    def Q_isWeb1(self):
        Comapny_Price(50)
        self.declare(Fact(Q_isWeb=input(" Is it A Wep ? ")))
                                      
    @Rule(Fact(Q_BRS='n'), NOT(Fact(Q_isWeb=W())))
    def Q_isWeb2(self):
        self.declare(Fact(Q_isWeb=input(" Is it A Wep ? ")))
                                      
    @Rule(Fact(Q_isWeb='y'), NOT(Fact(Q_isWebApplication=W())))
    def Q_isWebApplication1(self):
        self.declare(Fact(Q_isWebApplication=input(" Is it A Wep-Application  ? ")))
                                      
    @Rule(Fact(Q_isWeb='n'), NOT(Fact(Q_isMobileApplication=W())))
    def Q_isMobileApplication2(self):
        #-- todo mobile app
        self.declare(Fact(Q_isMobileApplication=input(" Is it A Mobile Application ? ")))
                     
    @Rule(Fact(Q_isMobileApplication='n'))
    def exi_t(self):
        print("! sorry this app only for mobile and web apps !")
                     
    @Rule(Fact(Q_isWebApplication='n'))
    def exi_t(self):
        print("! sorry this app only for mobile and web apps !")

    @Rule(Fact(Q_isWebApplication='y'), NOT(Fact(Q_buyHosting=W())))
    def Q_buyHosting(self):
        self.declare(Fact(Q_buyHosting=input(" Do You need to buy to the customer Hosting Service  ? ")))
                     
    @Rule(Fact(Q_buyHosting='y'), NOT(Fact(Q_buyDomain=W())))
    def Q_buyDomain1(self):
        Comapny_Price(200)
        self.declare(Fact(Q_buyDomain=input(" Do You need to buy to the customer Domain  ? ")))     
                     
    @Rule(Fact(Q_buyHosting='n'), NOT(Fact(Q_buyDomain=W())))
    def Q_buyDomain2(self):
        self.declare(Fact(Q_buyDomain=input(" Do You need to buy to the customer Domain  ? ")))       
                     
    @Rule(Fact(Q_buyDomain='y'), NOT(Fact(Q_eCommerceWep=W())))
    def Q_eCommerceWep1(self):
        Comapny_Price(15)
        self.declare(Fact(Q_eCommerceWep=input(" is it a Type of E-Commercre  ? ")))      
                     
    @Rule(Fact(Q_buyDomain='n'), NOT(Fact(Q_eCommerceWep=W())))
    def Q_eCommerceWep2(self):
        self.declare(Fact(Q_eCommerceWep=input(" is it a Type of E-Commercre  ? "))) 
                     
    @Rule(Fact(Q_eCommerceWep='n'), NOT(Fact(Q_serviceProvider=W())))
    def Q_serviceProvider(self):
        self.declare(Fact(Q_serviceProvider=input(" is it a Type of Service Provider ? "))) 
                     #--todo
                     
    @Rule(Fact(Q_eCommerceWep='y'), NOT(Fact(Q_multiFinder=W())))
    def Q_multiFinder(self):
        self.declare(Fact(Q_multiFinder=input(" is it Multif-Finder  ? "))) 
        
    @Rule(Fact(Q_multiFinder='y'), NOT(Fact(Q_desUIUX=W())))
    def Q_desUIUX1(self):
        Comapny_Price(100)
        self.declare(Fact(Q_desUIUX=input(" Do you have to Design UI/UX  ? "))) 
                   
    @Rule(Fact(Q_multiFinder='n'), NOT(Fact(Q_desUIUX=W())))
    def Q_desUIUX2(self):
        self.declare(Fact(Q_desUIUX=input(" Do you have to Design UI/UX  ? "))) 

    @Rule(Fact(Q_desUIUX='y'), NOT(Fact(Q_doesItNeed2_3Prog=W())))
    def Q_doesItNeed2_3Prog1(self):
        Comapny_Price(75)
        self.declare(Fact(Q_doesItNeed2_3Prog=input(" Does It Need 2--3 programres  ? "))) 
                   
    @Rule(Fact(Q_desUIUX='n'), NOT(Fact(Q_doesItNeed2_3Prog=W())))
    def Q_doesItNeed2_3Prog2(self):
        self.declare(Fact(Q_doesItNeed2_3Prog=input(" Does It Need 2--3 programres  ?"))) 
         
         #staticmethod(Comapny_Price.change_duration2_3)
    #----------------------------------------------------- 2-3 pro
    
    @Rule(Fact(Q_doesItNeed2_3Prog='y'), NOT(Fact(Q_hasAnimation=W())))
    def Q_hasAnimation98(self):
        staticmethod(Comapny_Price.change_pro2_3())
        self.declare(Fact(Q_hasAnimation=input(" Does It has Animation ? "))) 
        
    @Rule(Fact(Q_hasAnimation='y'), NOT(Fact(Q_hasShippingIntegration=W())))
    def Q_hasShippingIntegration2(self):
        Comapny_Price(100)
        self.declare(Fact(Q_hasShippingIntegration=input(" Has Shipping Integration  ? "))) 
        
    @Rule(Fact(Q_hasAnimation='n'), NOT(Fact(Q_hasShippingIntegration=W())))
    def Q_hasShippingIntegration3(self):
        self.declare(Fact(Q_hasShippingIntegration=input(" Has Shipping Integration  ? "))) 
    
    @Rule(Fact(Q_hasShippingIntegration='y'),NOT(Fact(Q_devTime2_3m=W())))
    def Q_devTime2_3m1(self):
       Comapny_Price(200)
       self.declare(Fact(Q_devTime2_3m=input(" Does Development time between 2-3 months  ? "))) 
       
    @Rule(Fact(Q_hasShippingIntegration='n'),NOT(Fact(Q_devTime2_3m=W())))
    def Q_devTime2_3m2(self):
       self.declare(Fact(Q_devTime2_3m=input(" Does Development time between 2-3 months  ? "))) 
       
    @Rule(Fact(Q_doesItNeed2_3Prog='y'),Fact(Q_devTime2_3m='y'))
    def e_exit90(self):
        staticmethod(Comapny_Price.change_duration2_3())
        print("THE COAST IS : ", Comapny_Price._coast, "$")
    
    @Rule(Fact(Q_devTime2_3m='n'),NOT(Fact(Q_devTime3_6m=W())))
    def Q_devTime3_6m33(self):
        self.declare(Fact(Q_devTime3_6m=input(" Does Development time between 4-6 months  ? "))) 
        
    @Rule(Fact(Q_doesItNeed2_3Prog='y'),Fact(Q_devTime3_6m='y'))
    def e_exit3(self):
        staticmethod(Comapny_Price.change_duration4_6())
        print("THE COAST IS : ", Comapny_Price._coast, "$")
        
        
    @Rule(Fact(Q_doesItNeed2_3Prog='y'),Fact(Q_devTime3_6m='n'))
    def e_exit91(self):
        staticmethod(Comapny_Price.change_duration_more_6())
        print("THE COAST IS : ", Comapny_Price._coast, "$")
   
   #------------------------------------------------------------------------ end 2-3 pro
    
    #------------------------------------------------------------------ 4-6 pro    
        #--- more than 3 progs branch           
    @Rule(Fact(Q_doesItNeed2_3Prog='n'), NOT(Fact(Q_doesItNeed4_6Prog=W())))
    def Q_doesItNeed4_6Prog(self):
        self.declare(Fact(Q_doesItNeed4_6Prog=input(" Does It Need 4--6 programres  ?")))
        
    @Rule(Fact(Q_doesItNeed4_6Prog='y'), NOT(Fact(Q_hasAnimation=W())))
    def Q_hasAnimation6(self):
        staticmethod(Comapny_Price.change_pro4_6())
        self.declare(Fact(Q_hasAnimation=input(" Does It has Animation ? "))) 
        
    @Rule(Fact(Q_hasAnimation='n'), NOT(Fact(Q_hasShippingIntegration=W())))
    def Q_hasShippingIntegration33(self):
        self.declare(Fact(Q_hasShippingIntegration=input(" Has Shipping Integration  ? "))) 
    
    @Rule(Fact(Q_hasAnimation='y'), NOT(Fact(Q_hasShippingIntegration=W())))
    def Q_hasShippingIntegration33(self):
        Comapny_Price(100)
        self.declare(Fact(Q_hasShippingIntegration=input(" Has Shipping Integration  ? "))) 
        
    @Rule(Fact(Q_hasShippingIntegration='y'),NOT(Fact(Q_devTime2_3m=W())))
    def Q_devTime2_3m13(self):
        Comapny_Price(200)
        self.declare(Fact(Q_devTime2_3m=input(" Does Development time between 2-3 months  ? "))) 
       
    @Rule(Fact(Q_hasShippingIntegration='n'),NOT(Fact(Q_devTime2_3m=W())))
    def Q_devTime2_3m23(self):
       self.declare(Fact(Q_devTime2_3m=input(" Does Development time between 2-3 months  ? "))) 
       
    @Rule(Fact(Q_doesItNeed4_6Prog='y'),Fact(Q_devTime2_3m='y'))
    def e_exit903(self):
        staticmethod(Comapny_Price.change_duration2_3())
        print("THE COAST IS : ", Comapny_Price._coast, "$")
    
    @Rule(Fact(Q_devTime2_3m='n'),NOT(Fact(Q_devTime3_6m=W())))
    def Q_devTime3_6m333(self):
        self.declare(Fact(Q_devTime3_6m=input(" Does Development time between 3-6 months  ? "))) 
        
    @Rule(Fact(Q_doesItNeed4_6Prog='y'),Fact(Q_devTime3_6m='y'))
    def e_exit33(self):
        staticmethod(Comapny_Price.change_duration4_6())
        print("THE COAST IS : ", Comapny_Price._coast, "$")
        
        
    @Rule(Fact(Q_doesItNeed4_6Prog='y'),Fact(Q_devTime3_6m='n'))
    def e_exit913(self):
        staticmethod(Comapny_Price.change_duration_more_6())
        print("THE COAST IS : ", Comapny_Price._coast, "$")

        
#------------------------------------------------------------------ end 4-6 pro

#------------------------------------------------------------------- service provider
    @Rule(Fact(Q_serviceProvider='y'),NOT(Fact(Q_buildFullSystem=W())))
    def Q_buildFullSystem1(self):
        self.declare(Fact(Q_buildFullSystem=input(" Do You Have to build Full System ? "))) 
        
    @Rule(Fact(Q_buildFullSystem='y'),NOT(Fact(Q_designUIUX=W())))
    def Q_designUIUX1(self):
        Comapny_Price(500)
        self.declare(Fact(Q_designUIUX=input(" Do You Have to Design UI/UX ? "))) 
        
    @Rule(Fact(Q_buildFullSystem='n'),NOT(Fact(Q_designUIUX=W())))
    def Q_designUIUX2(self):
        self.declare(Fact(Q_designUIUX=input(" Do You Have to Design UI/UX ? "))) 
        
    @Rule(Fact(Q_designUIUX='y'),NOT(Fact(Q_buildFeatures=W())))
    def Q_buildFeatures1(self):
        Comapny_Price(75)
        self.declare(Fact(Q_buildFeatures=input(" Do You Have to Build Extar Feauters ? "))) 
        
    @Rule(Fact(Q_designUIUX='n'),NOT(Fact(Q_buildFeatures=W())))
    def Q_buildFeatures2(self):
        self.declare(Fact(Q_buildFeatures=input(" Do You Have to Build Extar Feauters ? "))) 
        
    @Rule(Fact(Q_buildFeatures='y'),NOT(Fact(Q_need23pro=W())))
    def Q_need23pro1(self):
        Comapny_Price(50)
        self.declare(Fact(Q_need23pro=input(" Does it needs 2-3 programmers ? "))) 
    
    @Rule(Fact(Q_need23pro='y'),NOT(Fact(Q_hasnAnimation2=W())))
    def Q_hasnAnimation28(self):
        staticmethod(Comapny_Price.change_pro2_3())
        self.declare(Fact(Q_hasnAnimation2=input(" Does it has animation ? "))) 
    
    
    @Rule(Fact(Q_hasnAnimation2='y'),NOT(Fact(Q_devTime2_3m=W())))
    def Q_devTime2_3m81(self):
        Comapny_Price(100)
        self.declare(Fact(Q_devTime2_3m=input(" Does it needs 2-3 months ? "))) 
    
    @Rule(Fact(Q_hasnAnimation2='n'),NOT(Fact(Q_devTime2_3m=W())))
    def Q_devTime2_3m819(self):
        self.declare(Fact(Q_devTime2_3m=input(" Does it needs 2-3 months ? "))) 
        
    @Rule(Fact(Q_need23pro='y'),Fact(Q_devTime2_3m='y'))
    def e_exits1(self):
        staticmethod(Comapny_Price.change_duration2_3())
        print("THE COAST IS : ", Comapny_Price._coast, "$")

    
    
    @Rule(Fact(Q_devTime2_3m='n'),NOT(Fact(Q_devTime3_6m=W())))
    def Q_devTime3_6m3381(self):
        self.declare(Fact(Q_devTime3_6m=input(" Does Development time between 3-6 months  ? "))) 
        
    @Rule(Fact(Q_need23pro='y'),Fact(Q_devTime3_6m='y'))
    def e_exit382(self):
        staticmethod(Comapny_Price.change_duration4_6())
        print("THE COAST IS : ", Comapny_Price._coast, "$")

        
        
    @Rule(Fact(Q_need23pro='y'),Fact(Q_devTime3_6m='n'))
    def e_exit9184(self):
        staticmethod(Comapny_Price.change_duration_more_6())
        print("THE COAST IS : ", Comapny_Price._coast, "$")
    
    @Rule(Fact(Q_need23pro='n'),NOT(Fact(Q_need46pro=W())))
    def Q_need46pro1(self):
        self.declare(Fact(Q_need46pro=input(" Does it needs 4-6 programmers? "))) 
        
    @Rule(Fact(Q_need46pro='y'),NOT(Fact(Q_devTime2_3m=W())))
    def Q_devTime2_3m8081(self):
        staticmethod(Comapny_Price.change_pro4_6())
        self.declare(Fact(Q_devTime2_3m=input(" Does it needs 2-3 months ? "))) 
    
    @Rule(Fact(Q_need46pro='y'),Fact(Q_devTime2_3m='y'))
    def e_exits181(self):
        staticmethod(Comapny_Price.change_duration2_3())
        print("THE COAST IS : ", Comapny_Price._coast, "$")
    
    
    @Rule(Fact(Q_devTime2_3m='n'),NOT(Fact(Q_devTime3_6m=W())))
    def Q_devTime3_6m338181(self):
        self.declare(Fact(Q_devTime3_6m=input(" Does Development time between 4-6 months  ? "))) 
        
    @Rule(Fact(Q_need46pro='y'),Fact(Q_devTime3_6m='y'))
    def e_exit38281(self):
        staticmethod(Comapny_Price.change_duration4_6())
        print("THE COAST IS : ", Comapny_Price._coast, "$")
        
        
    @Rule(Fact(Q_need46pro='y'),Fact(Q_devTime3_6m='n'))
    def e_exit918481(self):
        staticmethod(Comapny_Price.change_duration_more_6())
        print("THE COAST IS : ", Comapny_Price._coast, "$")
    
    @Rule(Fact(Q_need46pro='n'))
    def error404(self):
        print("this system is only for small companies")
    
        
    
    @Rule(Fact(Q_serviceProvider='n'))
    def e_exit404(self):
        print("this SYSTEM is only for E-Commerce or Service Providers Web applications")



#---------------------------------------------------------------------- end service provider
#***StartMobileApp
    #2-3 programeers
    @Rule(Fact(Q_isMobileApplication='y'), NOT(Fact(programerrs23=W())))
    def programerrs23(self):
        self.declare(Fact(programerrs23=input("does it need 2_3 Programmers")))
    @Rule(Fact(programerrs23='y'),NOT(Fact(app3features=W())))
    def app3features(self):
        staticmethod(Comapny_Price.change_pro2_3())
        self.declare(Fact(app3features=input(" Does the application contains 0-3 Features Like Essential features like profile making, search, notifications, and messages, Fewer screens ? ")))
    @Rule(Fact(Q_mobileApplication='n'))
    def out_1(self):
        print( "\n Sorry, but this app only for web and mobile applications")
    @Rule(Fact(app3features='y'),NOT(Fact(app3months=W())))
    def app3months(self):
        self.declare(Fact(app3months=input("Does the Development time btw 2-3 months")))  
    @Rule(Fact(app3features='n'),NOT(Fact(app5fetuers=W())))
    def app5fetuers(self):
        self.declare(Fact(app5fetuers=input("Does the application contains 4-5 Features Like more than the previous and : Essential features, in addition to in-app purchases and payment portals Allows API integration More screens than the basic version Custom UI Real-time messaging and other features")))
    @Rule(Fact(app3months='y'))
    def app3mmmonths(self):
        staticmethod(Comapny_Price.change_duration2_3())
        print("\n The Coast is : ", Comapny_Price._coast, "$")
    @Rule(Fact(app3months='n'),NOT(Fact(app6months=W())))
    def app6months(self):
        self.declare(Fact(app6months=input('Does the Development time btw 3-6 months')))
    @Rule(Fact(app6months='y'))
    def secout(self):
        staticmethod(Comapny_Price.change_duration4_6())
        print("\n The Coast is : ", Comapny_Price._coast, "$")
    @Rule(Fact(app6months='n'))
    def secccout(self):
        staticmethod(Comapny_Price.change_duration_more_6())
        print("\n The Coast is : ", Comapny_Price._coast, "$")
    @Rule(Fact(app5fetuers='y'),NOT(Fact(app24months=W()))) 
    def app24months(self):
        self.declare(Fact(app24months=input("Does the Development time btw 2-3 months"))) 
          
    @Rule(Fact(app5fetuers='n'))
    def app5fetuersss(self):
        print("\n sorry this app is for small companies ")
     
    @Rule(Fact(app24months='y'))
    def app24mmmonths(self):
        staticmethod(Comapny_Price.change_duration2_3())
        print("\n  The Coast is : ", Comapny_Price._coast, "$")
    @Rule(Fact(app24months='n'),NOT(Fact(app46months=W())))
    def app46months(self):
        self.declare(Fact(app46months=input('Does the Development time btw 3-6 months')))
    @Rule(Fact(app46months='y'))
    def secout(self):
        staticmethod(Comapny_Price.change_duration4_6())
        print("\n  The Coast is : ", Comapny_Price._coast, "$")
    @Rule(Fact(app46months='n'))
    def seccout(self):
        staticmethod(Comapny_Price.change_duration_more_6())
        print("\n The Coast is : ", Comapny_Price._coast, "$")        
        
    #4-5Programers
    @Rule(Fact(programerrs23='n'),NOT(Fact(programerrs45=W())))
    def programerrs45(self):
        self.declare(Fact(app3features=input(" does it need 4_5 Programmers ")))    
    @Rule(Fact(programerrs45='n'))
    def sswout(self):
        print("\n sorry this app is for small companies")    
    @Rule(Fact(programerrs45='y'),NOT(Fact(ap3features=W())))
    def ap3features(self):
        staticmethod(Comapny_Price.change_pro4_6())
        self.declare(Fact(ap3features=input(" Does the application contains 0-3 Features Like Essential features like profile making, search, notifications, and messages, Fewer screens ? ")))
    @Rule(Fact(ap3features='y'),NOT(Fact(appp3months=W()))) 
    def appp3months(self):
        self.declare(Fact(appp3months=input("Does the Development time btw 2-3 months")))  
    @Rule(Fact(ap3features='n'),NOT(Fact(ap5fetuers=W())))
    def ap5fetuers(self):
        self.declare(Fact(ap5fetuers=input("Does the application contains 4-5 Features Like more than the previous and : Essential features, in addition to in-app purchases and payment portals Allows API integration More screens than the basic version Custom UI Real-time messaging and other features")))
    @Rule(Fact(appp3months='y'))
    def appp3mmmonths(self):
        staticmethod(Comapny_Price.change_duration2_3())
        print("\n The Coast is : ", Comapny_Price._coast, "$")
    @Rule(Fact(appp3months='n'),NOT(Fact(appp6months=W())))
    def appp6months(self):
        self.declare(Fact(appp6months=input('Does the Development time btw 3-6 months')))
    @Rule(Fact(appp6months='y'))
    def apppouttz(self):
        staticmethod(Comapny_Price.change_duration4_6())
        print("\n  The Coast is : ", Comapny_Price._coast, "$")
        
    @Rule(Fact(appp6months='n'))
    def apppouttw(self):
        staticmethod(Comapny_Price.change_duration_more_6())
        print("\n The Coast is : ", Comapny_Price._coast, "$")
        
    @Rule(Fact(ap5fetuers='y'),NOT(Fact(appp24months=W()))) 
    def appp24months(self):
        self.declare(Fact(appp24months=input("Does the Development time btw 2-3 months"))) 
    @Rule(Fact(ap5fetuers='n'))
    def apppoouttw(self):
        print("\n sorry this app is for small companies")
     
    @Rule(Fact(appp24months='y'))
    def appp24mmmonths(self):
        staticmethod(Comapny_Price.change_duration2_3())
        print("\n The Coast is : ", Comapny_Price._coast, "$")
    @Rule(Fact(appp24months='n'),NOT(Fact(appp46months=W())))
    def appp46months(self):
        self.declare(Fact(appp46months=input('Does the Development time btw 3-6 months')))
    @Rule(Fact(appp46months='y'))
    def apppoutto(self):
        staticmethod(Comapny_Price.change_duration4_6())
        print("\n The Coast is : ", Comapny_Price._coast, "$")
    @Rule(Fact(appp46months='n'))
    def apppoutt(self):
        print("\n As an average 20$ for an hour this app will cost 20000$-40000$")    

#**FinishMobileApp
       
   
engine = Sppd()
engine.reset() # Prepare the engine for the execution.
engine.run() # Run it!




