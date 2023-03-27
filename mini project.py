import math
from tkinter import *

# Program that collects data from the open circuit and short circuit test, prints the values of the equivalent circuit parameters

def Answer():
    Open_Circuit_Results, Short_Circuit_Results = getvalues()

    Cos_Theta = Open_Circuit_Results[2]/(Open_Circuit_Results[0]*Open_Circuit_Results[1])
    Theta = math.acos(Cos_Theta)
    Sin_Theta = math.sin(Theta)
    iMagnetizing_LV = Open_Circuit_Results[1]*Sin_Theta
    iCoreLoss_LV = Open_Circuit_Results[1]*Cos_Theta
    rCoreLoss_LV = Open_Circuit_Results[0]/iMagnetizing_LV
    rCoreLoss_LV = round(rCoreLoss_LV,2)
    xMagnetizing_LV = Open_Circuit_Results[0]/iCoreLoss_LV
    xMagnetizing_LV = round(xMagnetizing_LV,2)

    rEquivalent_HV = Short_Circuit_Results[2]/Short_Circuit_Results[1]**2
    rEquivalent_HV = round(rEquivalent_HV,2)
    zShortCircuit_HV = Short_Circuit_Results[0]/Short_Circuit_Results[1]
    xEquivalent_HV_square = zShortCircuit_HV**2- rEquivalent_HV**2
    xEquivalentHV = xEquivalent_HV_square**0.5
    xEquivalentHV = round(xEquivalentHV,2)
    t1=f'Resistance representing core loss reffered to LV is {xMagnetizing_LV}Ω.'
    t2=f'Magnetizing reactance reffered to LV is {rCoreLoss_LV}Ω.'
    t3=f'Equivalent resistance reffered to HV is {rEquivalent_HV}Ω.'
    t4=f'Equivalent reactance reffered to HV is {xEquivalentHV}Ω.'
    text1=Message(main,text=t1,bg='grey',fg='black',font=('algerian',10,'bold'),width=5000)
    text2=Message(main,text=t2,bg='grey',fg='black',font=('algerian',10,'bold'),width=5000)
    text3=Message(main,text=t3,bg='grey',fg='black',font=('algerian',10,'bold'),width=5000)
    text4=Message(main,text=t4,bg='grey',fg='black',font=('algerian',10,'bold'),width=5000)
    text1.grid(row=7,column=2)
    text2.grid(row=8,column=2)
    text3.grid(row=9,column=2)
    text4.grid(row=10,column=2)
##    print("###########################values are#########################")
##    print(f'Resistance representing core loss reffered to LV is {xMagnetizing_LV}Ω.')
##    print(f'Magnetizing reactance reffered to LV is {rCoreLoss_LV}Ω.')
##    print(f'Equivalent resistance reffered to HV is {rEquivalent_HV}Ω.')
##    print(f'Equivalent reactance reffered to HV is {xEquivalent_HV}Ω.')

def getvalues():
    p = []
    q = []
    Vsc = float(ValueVoltageShortCircuit.get())
    Voc = float(ValueVoltageOPenCircuit.get())
    Isc = float(ValueCurrentShortCircuit.get())
    Ioc = float(ValueCurrentOpenCircuit.get())
    Psc = float(ValuePowerShortCircuit.get())
    Poc = float(ValuePowerOpenCircuit.get())
    ShirtcircuitData = [Vsc,Isc,Psc]
    oc_data = [Voc,Ioc,Poc]
    for i in oc_data:
        p.append(i)
    for j in ShirtcircuitData:
        q.append(j)
    return p, q

main = Tk()
main['bg'] = 'black'
main.geometry('900x500')
main.title('TRANSFORMER PARAMETERS:GUI')
OpenCircuit_Test = Label(main, text='Open Circuit Test', borderwidth=6, relief=SUNKEN, font='comicsanms 12 bold', padx=25, pady=25,bg='orange')
ShortCircuit_Test = Label(main, text='Short Circuit Test', borderwidth=6, relief=SUNKEN, font='comicsanms 12 bold', padx=25, pady=25,bg='orange')
voltage = Label(main, text="Voltage (V)", font='comicsanms 12 bold', padx=25, pady=12, borderwidth=6, relief=SUNKEN,bg='orange')
current = Label(main, text="Current (A)", font='comicsanms 12 bold', padx=25, pady=12, borderwidth=6, relief=SUNKEN,bg='orange')
power = Label(main, text="Power (W)", font='comicsanms 12 bold', padx=25, pady=12, borderwidth=6, relief=SUNKEN,bg='orange')
OpenCircuit_Test.grid(row=1)
ShortCircuit_Test.grid(row=2)
voltage.grid(row=0,column=1)
current.grid(row=0,column=2)
power.grid(row=0,column=3)

ValueVoltageOPenCircuit = StringVar()
ValueVoltageShortCircuit = StringVar()
ValueCurrentOpenCircuit = StringVar()
ValueCurrentShortCircuit = StringVar()
ValuePowerOpenCircuit = StringVar()
ValuePowerShortCircuit = StringVar()

Voltage_At_Opencircuit = Entry(main, textvariable=ValueVoltageOPenCircuit, relief=SUNKEN, borderwidth=7)
Voltage_At_ShortCircuit = Entry(main, textvariable=ValueVoltageShortCircuit, relief=SUNKEN, borderwidth=7)
Current_At_Opencircuit = Entry(main, textvariable=ValueCurrentOpenCircuit, relief=SUNKEN, borderwidth=7)
Current_At_ShortCircuit = Entry(main, textvariable=ValueCurrentShortCircuit, relief=SUNKEN, borderwidth=7)
Power_At_OpenCircuit = Entry(main, textvariable=ValuePowerOpenCircuit, relief=SUNKEN, borderwidth=7)
Power_At_ShortCircuit = Entry(main, textvariable=ValuePowerShortCircuit, relief=SUNKEN, borderwidth=7)
Voltage_At_Opencircuit.grid(row=1, column=1)
Voltage_At_ShortCircuit.grid(row=2, column=1)
Current_At_Opencircuit.grid(row=1, column=2)
Current_At_ShortCircuit.grid(row=2, column=2)
Power_At_OpenCircuit.grid(row=1, column=3)
Power_At_ShortCircuit.grid(row=2, column=3)

submit = Button(main, text="SUBMIT", font=('comicsanms 14 bold'), borderwidth=6, command=Answer)
submit.grid(row=3, column=2)


main.mainloop()
