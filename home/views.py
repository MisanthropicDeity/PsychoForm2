from django.shortcuts import render
from django.http import HttpResponseRedirect
from random import choice,sample
#from numpy import delete,where,array
from . models import submission,feedback



# for i in range(0,8):
#     if i <4:
#         quest.append(choice(question[i]))
#     else:
#         quest.append(choice(question[7-i]))
#     # print (quest[i])
#     # print (question)
    
#     if i!=7:
#         (x,y) = where(question==quest[i])
#         # print(x,y)
#         question = delete(question ,x ,axis=0)
#         question = delete(question ,y , axis=1)
        
#     # print (question)
a1='An intelligence agent gets the information that certain communal groups are planning to hold violent demonstrations in a populated area in the city. These are about to break out in an hour. If nothing is done to stop these demonstrations, hundreds of people will die.  He wants to prevent violence. He believes that the best course of action is to immediately notify all the nearby police stations, who can then reach in time to prevent the demonstrators from vandalizing property and hurting others, instead of going to his boss first. He, however, chooses to go to his boss to ask for advice. By the time he is ordered by the supervisor to notify the police stations, it is too late and riots break out in the city. Hundreds of lives are lost and property destroyed.'
b1 = """An intelligence agent gets the information that certain communal groups are planning to hold violent demonstrations in a populated area in the city. These are about to break out in an hour. If nothing is done to stop these demonstrations, hundreds of people will die.  
He wants to prevent violence. 
He believes that the best course of action is to seek advice from his boss, who is experienced in dealing with these situations, about what to do, instead of himself notifying the authorities.
He chooses to go to his boss to ask for advice.
By the time he is ordered by the supervisor to notify the police stations, it is too late and riots break out in the city. Hundreds of lives are lost and property destroyed.
"""
c1 = """
An intelligence agent gets the information that certain communal groups are planning to hold violent demonstrations in a populated area in the city. These are about to break out in an hour. If nothing is done to stop these demonstrations, hundreds of people will die.  
He wants to prevent violence. 
He believes that the best course of action is to immediately notify all the nearby police stations, who can then reach in time to prevent the demonstrators from vandalizing property and hurting others. 
He, however, chooses to go to his boss to ask for advice.
By the time his supervisor orders action, another agent verifies that the information was incorrect and there were no demonstrations. 
"""
d1="""An intelligence agent gets the information that certain communal groups are planning to hold violent demonstrations in a populated area in the city. These are about to break out in an hour. If nothing is done to stop these demonstrations, hundreds of people will die.  
He wants to prevent violence. 
He believes that the best course of action is to seek advice from his boss, who is experienced in dealing with these situations, about what to do, instead of himself notifying the authorities.
He chooses to go to his boss to ask for advice.
By the time his supervisor orders action, another agent discovers that the information was not correct and there were no demonstrations.
"""

e1="""An intelligence agent gets the information that certain communal groups are planning to hold violent demonstrations in a populated area in the city. These are about to break out in an hour. If nothing is done to stop these demonstrations, hundreds of people will die.  
He doesn’t care about preventing violence. He only wants to do his job properly. 
He believes that the best course of action is to immediately notify all the nearby police stations, who can then reach in time to prevent the riots, instead of going to his boss first. 
He, however, chooses to go to his boss to ask for advice.
By the time he is ordered by the supervisor to notify the police stations, it is too late and riots break out in the city. Hundreds of lives are lost and property destroyed.
"""
f1="""An intelligence agent gets the information that certain communal groups are planning to hold violent demonstrations in a populated area in the city. These are about to break out in an hour. If nothing is done to stop these demonstrations, hundreds of people will die.  
He doesn’t care about preventing violence. He only wants to do his job properly. 
He believes that the best course of action is to seek advice from his boss, who is experienced in dealing with these situations, about what to do, instead of himself notifying the authorities.
He, however, chooses to go to his boss to ask for advice.
By the time he is ordered by the supervisor to notify the police stations, it is too late and riots break out in the city. Hundreds of lives are lost and property destroyed.
"""
g1 ="""
An intelligence agent gets the information that certain communal groups are planning to hold violent demonstrations in a populated area in the city. These are about to break out in an hour. If nothing is done to stop these demonstrations, hundreds of people will die.  
He doesn’t care about preventing violence. He only wants to do his job properly. 
He believes that the best course of action is to immediately notify all the nearby police stations, who can then reach in time to prevent the riots, instead of going to his boss first.
He, however chooses to go to his boss to ask for advice.
By the time his supervisor orders action, another agent verifies that the information was incorrect and there were no demonstration
"""
h1="""An intelligence agent gets the information that certain communal groups are planning to hold violent demonstrations in a populated area in the city. These are about to break out in an hour. If nothing is done to stop these demonstrations, hundreds of people will die.  
He doesn’t care about preventing violence. He only wants to do his job properly. 
He believes that the best course of action is to seek advice from his boss, who is experienced in dealing with these situations, about what to do, instead of himself notifying the authorities.
He chooses to go to his boss to ask for advice.
By the time his supervisor orders action, another agent verifies that the information was incorrect and there were no demonstrations.
"""
a2="""
An engineer of a waterworks company, which delivers recycled water to the town, notices a problem in the filtering system due to which the filtered water contains harmful toxins that could be very harmful for people’s health. It is very important that the water is not delivered to the towns. He wants to prevent a potential health disaster. 
He believes the best course of action is to inform the supply team first  to immediately de-link the pipelines from main water supply of the city to prevent potential disaster instead of fixing the filter first. 
He informs the technical about the problem so that the filtering system could be fixed as soon as possible. The supply team is informed too late. The contaminated water gets delivered to the town and hundreds of people get seriously ill.
"""
b2="""An engineer of a waterworks company which delivers recycled water to the town notices a problem in the filtering system due to which the filtered water contains harmful toxins that could be very harmful for people’s health. It is very important that the water is not delivered to the towns.
He wants to prevent a potential health disaster.
He believes the best course of action is to fix the filter first instead of informing the supply team to de-link the pipelines from main water supply of the city.
He informs the technical team about the problem so that the filtering system could be fixed as soon as possible. The contaminated water gets delivered to the t
own and hundreds of people get seriously ill.
"""
c2="""An engineer of a waterworks company which delivers recycled water to the town notices a problem in the filtering system due to which the filtered water contains harmful toxins that could be very harmful for people’s health. It is very important that the water is not delivered to the towns.
He wants to prevent a potential health disaster.
He believes the best course of action is to inform the supply team first to immediately de-link the pipelines from main water supply of the city to mitigate potential disaster.
He informs the technical  about the problem so that the filtering system could be fixed as soon a
s possible. 
Another maintenance employee manages to cut the supply and the contaminated water gets contained instead of being delivered to the city. 
"""
d2="""An engineer of a waterworks company which delivers recycled water to the town notices a problem in the filtering system due to which the filtered water contains harmful toxins that could be very harmful for people’s health. It is very important that the water is not delivered to the towns.
He wants to prevent a potential health disaster.
He believes the best course of action is to fix the filter first instead of informing the supply team to de-link the pipelines from main water supply of the city.
He informs the technical team, before informing the supply team, about the problem so that the filtering system could be fixed as soon as possible. 
Another maintenance employee manages to cut the supply and the contaminated water gets contained instead of being delivered to the city."""

e2="""An engineer of a waterworks company which delivers recycled water to the town notices a problem in the filtering system due to which the filtered water contains harmful toxins that could be very harmful for people’s health. It is very important that the water is not delivered to the towns.
He only wants to do his job, which is to fix the filtering machine.
He believes the best course of action is to inform the supply team first to immediately de-link the pipelines from main water supply of the city to mitigate potential disaster.
He instead informs the technical team about the problem so that the filtering system could be fixed as soon as possible. The supply team is informed later. The contaminated water gets delivered to the town and hundreds of people get seriously ill."""

f2="""An engineer of a waterworks company which delivers recycled water to the town notices a problem in the filtering system due to which the filtered water contains harmful toxins that could be very harmful for people’s health. It is very important that the water is not delivered to the towns.
He only wants to do his job which is to fix the filtering machine.
He believes the best course of action is to fix the filter first instead of informing the supply team to de-link the pipelines from main water supply of the city.
He informs the technical team about the problem so that the filtering system could be fixed as soon as possible. The supply team is informed later. The contaminated water gets delivered to the town and hundreds of people get seriously ill."""

g2="""An engineer of a waterworks company which delivers recycled water to the town notices a problem in the filtering system due to which the filtered water contains harmful toxins that could be very harmful for people’s health. It is very important that the water is not delivered to the towns.
He only wants to do his job which is to fix the filtering machine.
He believes the best course of action is to inform the supply team first to immediately de-link the pipelines from main water supply of the city to mitigate potential disaster.
He informs the technical team, before informing the supply team, about the problem so that the filtering system could be fixed as soon as possible. 
Another maintenance employee manages to cut the supply and the contaminated water gets contained instead of being delivered to the city.
"""

h2="""An engineer of a waterworks company which delivers recycled water to the town notices a problem in the filtering system due to which the filtered water contains harmful toxins that could be very harmful for people’s health. It is very important that the water is not delivered to the towns.
He only wants to do his job which is to fix the filtering machine.
He believes the best course of action is to fix the filter first instead of informing the supply team to de-link the pipelines from main water supply of the city.
He informs the technical team, before informing the supply team, about the problem so that the filtering system could be fixed as soon as possible. 
Another maintenance employee manages to cut the supply and the contaminated water gets contained instead of being delivered to the city.
"""

a3="""A hospital staffer is tasked with testing the blood samples for any potential pathogens. The hospital receives a call from a man who donated his blood in a donation camp organized by the hospital. This man notifies the hospital that he is diagnosed as HIV positive and that his blood should not be used for transfusion. The staffer is informed by the hospital to eliminate his sample. The staffer’s shift has just come to an end. 
She wants to prevent a major mishap by detecting the sample as soon as possible. She believes that the best course of action is to extend her shift as the other staffer may not be informed. She, however, ends her shift and goes home. The blood sample goes undetected into the blood bank. The blood is transfused to a pregnant woman due to which both her and her child get HIV AIDS."""

b3="""A hospital staffer is tasked with testing the blood samples for any potential pathogens. The hospital receives a call from a man who donated his blood in a donation camp organized by the hospital. This man notifies the hospital that he is diagnosed as HIV positive and that his blood should not be used for transfusion. The staffer is informed by the hospital to eliminate his sample. The staffer’s shift has just come to an end.
She wants to prevent a major mishap by detecting the sample as soon as possible.
She believes that she can sign off as the other staffer would be informed and would detect the sample.
She ends her shift and goes home. The blood sample goes undetected into the blood bank. The blood is transfused to a pregnant woman due to which both her and her child get HIV AIDS."""

c3="""A hospital staffer is tasked with testing the blood samples for any potential pathogens. The hospital receives a call from a man who donated his blood in a donation camp organized by the hospital. This man notifies the hospital that he is diagnosed as HIV positive and that his blood should not be used for transfusion. The staffer is informed by the hospital to eliminate his sample. The staffer’s shift has just come to an end.
She wants to prevent a major mishap by detecting the sample as soon as possible.
She believes that the best course of action is to extend her shift as the other staffer may not be informed.
She, however, ends her shift and goes home. 
However, before the blood could be transfused to someone, the infection gets detected and the blood is rejected. """

d3="""A hospital staffer is tasked with testing the blood samples for any potential pathogens. The hospital receives a call from a man who donated his blood in a donation camp organized by the hospital. This man notifies the hospital that he is diagnosed as HIV positive and that his blood should not be used for transfusion. The staffer is informed by the hospital to eliminate his sample. The staffer’s shift has just come to an end.
She wants to prevent a major mishap by detecting the sample as soon as possible.
She believes that she can sign off, as the other staffer would be informed and would detect the sample.
She ends her shift and goes home. However, before the blood could be transfused to someone, the infection gets detected and the blood is rejected."""

e3="""A hospital staffer is tasked with testing the blood samples for any potential pathogens. The hospital receives a call from a man who donated his blood in a donation camp organized by the hospital. This man notifies the hospital that he is diagnosed as HIV positive and that his blood should not be used for transfusion. The staffer is informed by the hospital to eliminate his sample. The staffer’s shift has just come to an end.
She only wants to finish her shift without any hassle. 
She believes that the best course of action is to extend her shift as the other staffer may not be informed.
She, however, ends her shift and goes home. The blood sample goes undetected into the blood bank. The blood is transfused to a pregnant woman due to which both her and her child get HIV AIDS.A hospital staffer is tasked with testing the blood samples for any potential pathogens. The hospital receives a call from a man who donated his blood in a donation camp organized by the hospital. This man notifies the hospital that he is diagnosed as HIV positive and that his blood should not be used for transfusion. The staffer is informed by the hospital to eliminate his sample. The staffer’s shift has just come to an end.
She only wants to finish her shift without any hassle.
She believes that she can sign off, as the other staffer would be informed and would detect the sample.
She ends her shift and goes home. The blood sample goes undetected into the blood bank. The blood is transfused to a pregnant woman due to which both her and her child get HIV AIDS."""

f3="""A hospital staffer is tasked with testing the blood samples for any potential pathogens. The hospital receives a call from a man who donated his blood in a donation camp organized by the hospital. This man notifies the hospital that he is diagnosed as HIV positive and that his blood should not be used for transfusion. The staffer is informed by the hospital to eliminate his sample. The staffer’s shift has just come to an end.
She only wants to finish her shift without any hassle.
She believes that she can sign off, as the other staffer would be informed and would detect the sample.
She ends her shift and goes home. The blood sample goes undetected into the blood bank. The blood is transfused to a pregnant woman due to which both her and her child get HIV AIDS."""

g3="""A hospital staffer is tasked with testing the blood samples for any potential pathogens. The hospital receives a call from a man who donated his blood in a donation camp organized by the hospital. This man notifies the hospital that he is diagnosed as HIV positive and that his blood should not be used for transfusion. The staffer is informed by the hospital to eliminate his sample. The staffer’s shift has just come to an end.
She only wants to finish her shift without any hassle.
She believes that the best course of action is to extend her shift as the other staffer may not be informed.
She, however, ends her shift and goes home.
However, before the blood could be transfused to someone, the infection gets detected and the blood is rejected.
"""

h3="""A hospital staffer is tasked with testing the blood samples for any potential pathogens. The hospital receives a call from a man who donated his blood in a donation camp organized by the hospital. This man notifies the hospital that he is diagnosed as HIV positive and that his blood should not be used for transfusion. The staffer is informed by the hospital to eliminate his sample. The staffer’s shift has just come to an end.
She only wants to finish her shift without any hassle.
She believes that she can sign off, as the other staffer would be informed and would detect the sample.
She ends her shift and goes home.
However, before the blood could be transfused to someone, the infection gets detected and the blood is rejected."""

a4="""A travel guide is leading a group of school students on a tour of a national park. He gets to know through the authorities of the park the areas that are dangerous for school students, even though they are open for adults. Hence, these areas would have access but he has to monitor students so that they do not enter them. He announces to the group of students, names and locations of all areas that they should not go to. He notices that two of the students were not there when he made the announcements. 
He wants all students to be safe. 
He believes that the best course of action is to wait for these two students and to inform them before they start the journey into the park.
He however starts the journey in the park and fails to tell those two students. They climb up a cliff in one of the dangerous areas and one of them falls off it and dies."""

b4="""A travel guide is leading a group of school students on a tour of a national park. He gets to know through the authorities of the park the areas that are dangerous for school students, even though they are open for adults. Hence, these areas would have access but he has to monitor students so that they do not enter them. He announces to the group of students, names and locations of all areas that they should not go to. He notices that two of the students were not there when he made the announcements.
He wants all students to be safe. 
He believes the best course of action is to start the journey and tell the students when he sees them rather than delaying to tell them immediately. 
He however starts the journey in the park and fails to tell those two students.
They climb up a cliff in one of the dangerous areas and one of them falls off it and dies.
"""

c4="""A travel guide is leading a group of school students on a tour of a national park. He gets to know through the authorities of the park the areas that are dangerous for school students, even though they are open for adults. Hence, these areas would have access but he has to monitor students so that they do not enter them. He announces to the group of students, names and locations of all areas that they should not go to. He notices that two of the students were not there when he made the announcements.
He wants all students to be safe. 
He believes that the best course of action is to wait for these two students and to inform them before they start the journey into the park.
He however starts the journey in the park and fails to tell those two students.
However, as the two students were entering one of the dangerous areas, their peers informed them about the restrictions.

"""

d4="""A travel guide is leading a group of school students on a tour of a national park. He gets to know through the authorities of the park the areas that are dangerous for school students, even though they are open for adults. Hence, these areas would have access but he has to monitor students so that they do not enter them. He announces to the group of students, names and locations of all areas that they should not go to. He notices that two of the students were not there when he made the announcements.
He wants all students to be safe. 
He believes the best course of action is to start the journey and tell the students when he sees them rather than delaying to tell them immediately. 
He however starts the journey in the park and fails to tell those two students.
However, as the two students were entering one of the dangerous areas, their peers informed them about the restrictions.
"""

e4="""A travel guide is leading a group of school students on a tour of a national park. He gets to know through the authorities of the park the areas that are dangerous for school students, even though they are open for adults. Hence, these areas would have access but he has to monitor students so that they do not enter them. He announces to the group of students, names and locations of all areas that they should not go to. He notices that two of the students were not there when he made the announcements.
He only wants to finish the tour as soon as possible.
He believes that the best course of action is to wait for these two students and to inform them before they start the journey into the park. 
He however starts the journey in the park and fails to tell those two students.
They climb up a cliff in one of the dangerous areas and one of them falls off it and dies.
 """

f4="""A travel guide is leading a group of school students on a tour of a national park. He gets to know through the authorities of the park the areas that are dangerous for school students, even though they are open for adults. Hence, these areas would have access but he has to monitor students so that they do not enter them. He announces to the group of students, names and locations of all areas that they should not go to. He notices that two of the students were not there when he made the announcements.
He only wants to finish the tour as soon as possible.
He believes the best course of action is to start the journey and tell the students when he sees them rather than delaying to tell them immediately. 
He however starts the journey in the park and fails to tell those two students. They climb up a cliff in one of the dangerous areas and one of them falls off it and dies.
"""

g4="""A travel guide is leading a group of school students on a tour of a national park. He gets to know through the authorities of the park the areas that are dangerous for school students, even though they are open for adults. Hence, these areas would have access but he has to monitor students so that they do not enter them. He announces to the group of students, names and locations of all areas that they should not go to. He notices that two of the students were not there when he made the announcements.
He only wants to finish the tour as soon as possible.
He believes that the best course of action is to wait for these two students and to inform them before they start the journey into the park.
He however starts the journey in the park and fails to tell those two students.
However, as the two students were entering one of the dangerous areas, their peers informed them about the restrictions.

A travel guide is leading a group of school students on a tour of a national park. He gets to know through the authorities of the park the areas that are dangerous for school students, even though they are open for adults. Hence, these areas would have access but he has to monitor students so that they do not enter them. He announces to the group of students, names and locations of all areas that they should not go to. He notices that two of the students were not there when he made the announcements.
He only wants to finish the tour as soon as possible.
He believes the best course of action is to start the journey and tell the students when he sees them rather than delaying to tell them immediately.
He however starts the journey in the park and fails to tell those two students. However, as the two students were entering one of the dangerous areas, their peers informed them about the restrictions."""

h4="""A travel guide is leading a group of school students on a tour of a national park. He gets to know through the authorities of the park the areas that are dangerous for school students, even though they are open for adults. Hence, these areas would have access but he has to monitor students so that they do not enter them. He announces to the group of students, names and locations of all areas that they should not go to. He notices that two of the students were not there when he made the announcements.
He only wants to finish the tour as soon as possible.
He believes the best course of action is to start the journey and tell the students when he sees them rather than delaying to tell them immediately.
He however starts the journey in the park and fails to tell those two students. However, as the two students were entering one of the dangerous areas, their peers informed them about the restrictions."""

a5="""A municipal officer is tasked with proper collection and disposal of biomedical wastes from different hospitals in the city. The medical waste is to be segregated from the other kind of waste before being sent to a treatment facility. The employee gets to know that some hospitals are not segregating the waste due to which it is dumped in common dumping ground near a highly populated area. 
She wants to prevent any mishap to environment and human life. She believes that the best course of action is to send strict warnings to the hospitals and if they still do not comply to stop waste collection. She, however, sends only cursory notices, which have no effect.
The hospitals continue to dump unsegregated waste unchecked, due to which diseases break out in the area, resulting in casualties.
"""

b5="""A municipal officer is tasked with proper collection and disposal of biomedical wastes from different hospitals in the city. The medical waste is to be segregated from the other kind of waste before being sent to a treatment facility. The employee gets to know that some hospitals are not segregating the waste due to which it is dumped in common dumping ground near a highly populated area.
She wants to prevent any mishap to environment and human life.
She believes the best course of action is to notify the hospitals about the situation and wait for them to act.
She sends only cursory notices, which have no effect.
The hospitals continue to dump unsegregated waste unchecked, due to which diseases break out in the area, resulting in casualties.
"""

c5="""A municipal officer is tasked with proper collection and disposal of biomedical wastes from different hospitals in the city. The medical waste is to be segregated from the other kind of waste before being sent to a treatment facility. The employee gets to know that some hospitals are not segregating the waste due to which it is dumped in common dumping ground near a highly populated area.
She wants to prevent any mishap to environment and human life.
She believes that the best course of action is to send strict warnings to the hospitals and if they still do not comply to stop waste collection.
She, however, only sends cursory notices to the hospitals, which have no effect. The hospitals, however, start segregating their waste after pressures from several environmental organizations.
"""

d5="""A municipal officer is tasked with proper collection and disposal of biomedical wastes from different hospitals in the city. The medical waste is to be segregated from the other kind of waste before being sent to a treatment facility. The employee gets to know that some hospitals are not segregating the waste due to which it is dumped in common dumping ground near a highly populated area.
She wants to prevent any mishap to environment and human life.
She believes the best course of action is to notify the hospitals about the situation and wait for them to act.
She, however, only sends cursory notices to the hospitals, which have no effect. The hospitals, however, start segregating their waste after pressures from several environmental organizations.
"""

e5="""A municipal officer is tasked with proper collection and disposal of biomedical wastes from different hospitals in the city. The medical waste is to be segregated from the other kind of waste before being sent to a treatment facility. The employee gets to know that some hospitals are not segregating the waste due to which it is dumped in common dumping ground near a highly populated area.
She does not care about environment but only wants to do what is required.
She believes that the best course of action is to send strict warnings to the hospitals and if they still do not comply to stop waste collection.
She, however, sends only cursory notices, which have no effect.
The hospitals continue to dump unsegregated waste unchecked, due to which diseases break out in the area, resulting in casualties.
"""

f5="""A municipal officer is tasked with proper collection and disposal of biomedical wastes from different hospitals in the city. The medical waste is to be segregated from the other kind of waste before being sent to a treatment facility. The employee gets to know that some hospitals are not segregating the waste due to which it is dumped in common dumping ground near a highly populated area.
She does not care about environment but only wants to do what is required.
She believes the best course of action is to notify the hospitals about the situation and wait for them to act.
She sends only cursory notices, which have no effect.
The hospitals continue to dump unsegregated waste unchecked, due to which diseases break out in the area, resulting in casualties.
"""

g5="""A municipal officer is tasked with proper collection and disposal of biomedical wastes from different hospitals in the city. The medical waste is to be segregated from the other kind of waste before being sent to a treatment facility. The employee gets to know that some hospitals are not segregating the waste due to which it is dumped in common dumping ground near a highly populated area.
She does not care about environment but only wants to do what is required.
She believes that the best course of action is to send strict warnings to the hospitals and if they still do not comply to stop waste collection.
She, however, only sends cursory notices to the hospitals, which have no effect. The hospitals, however, start segregating their waste after pressures from several environmental organizations.
"""

h5="""A municipal officer is tasked with proper collection and disposal of biomedical wastes from different hospitals in the city. The medical waste is to be segregated from the other kind of waste before being sent to a treatment facility. The employee gets to know that some hospitals are not segregating the waste due to which it is dumped in common dumping ground near a highly populated area.
She does not care about environment but only wants to do what is required.
She believes the best course of action is to notify the hospitals about the situation and wait for them to act.
She, however, only sends cursory notices to the hospitals, which have no effect. The hospitals, however, start segregating their waste after pressures from several environmental organizations.
"""

a6="""A bank employee is given a target to give a certain number of loans to customers in a particular period of time. The employee is required not just to ensure the completion of target but also take into account the credit worthiness of the customers. This requires looking through their credit reports and doing background checks. 
She wants to make sure that loans go to customers who have the ability to repay them. 
She believes that she can complete the target and do relevant checks on customers in time allotted. She, however, bypass these background checks and goes beyond her target to give loans. Some of the debtors turn out to be defaulters and the bank incurs massive losses.
"""

b6="""A bank employee is given a target to give a certain number of loans to customers in a particular period of time. The employee is required not just to ensure the completion of target but also take into account the credit worthiness of the customers. This requires looking through their credit reports and doing background checks.
She wants to make sure that loans go to customers who have the ability to repay them. 
She believes that she cannot both finish her target and do background checks in the time allotted.
She bypasses these background checks and goes beyond her target to give loans. Some of the debtors turn out to be defaulters and the bank incurs massive losses.
"""

c6="""A bank employee is given a target to give a certain number of loans to customers in a particular period of time. The employee is required not just to ensure the completion of target but also take into account the credit worthiness of the customers. This requires looking through their credit reports and doing background checks.
She wants to make sure that loans go to customers who have the ability to repay them. 
She believes that she can complete the target and do relevant checks on customers in time allotted.
She, however, bypasses these background checks and goes beyond her target to give loans. All the debtors turn out to be credit worthy and the bank makes profit.
"""

d6="""A bank employee is given a target to give a certain number of loans to customers in a particular period of time. The employee is required not just to ensure the completion of target but also take into account the credit worthiness of the customers. This requires looking through their credit reports and doing background checks.
She wants to make sure that loans go to customers who have the ability to repay them. 
She believes that she cannot both finish her target and do background checks in the time allotted.
She bypasses these background checks and goes beyond her target to give loans. All the debtors turn out to be credit worthy and the bank makes profit.
"""

e6="""A bank employee is given a target to give a certain number of loans to customers in a particular period of time. The employee is required not just to ensure the completion of target but also take into account the credit worthiness of the customers. This requires looking through their credit reports and doing background checks.
She wants to give as many loans as possible in the time allotted. 
She believes that she can complete the target and do relevant checks on customers in time allotted.
She, however bypasses these background checks and goes beyond her target to give loans. Some of the debtors turn out to be defaulters and the bank incurs massive losses.
"""

f6="""A bank employee is given a target to give a certain number of loans to customers in a particular period of time. The employee is required not just to ensure the completion of target but also take into account the credit worthiness of the customers. This requires looking through their credit reports and doing background checks.
She wants to give as many loans as possible in the time allotted.
She believes that she cannot both finish her target and do background checks in the time allotted.
She bypasses these background checks and goes beyond her target to give loans. Some of the debtors turn out to be defaulters and the bank incurs massive losses.
"""

g6="""A bank employee is given a target to give a certain number of loans to customers in a particular period of time. The employee is required not just to ensure the completion of target but also take into account the credit worthiness of the customers. This requires looking through their credit reports and doing background checks.
She wants to give as many loans as possible in the time allotted.
She believes that she can complete the target and do relevant checks on customers in time allotted.
She, however, bypasses these background checks and goes beyond her target to give loans. All the debtors turn out to be credit worthy and the bank makes profit.
"""

h6="""A bank employee is given a target to give a certain number of loans to customers in a particular period of time. The employee is required not just to ensure the completion of target but also take into account the credit worthiness of the customers. This requires looking through their credit reports and doing background checks.
She wants to give as many loans as possible in the time allotted.
She believes that she cannot both finish her target and do background checks in the time allotted.
She bypasses these background checks and goes beyond her target to give loans. All the debtors turn out to be credit worthy and the bank makes profit.
"""

a7="""An employee of a school is tasked with uploading online, the test scores of the students for a scholarship test. This scholarship is for economically weaker students and would give them opportunities to study in premier institutions to succeed in life. The scores have to be uploaded within a given deadline. It is the last day of the deadline.
The employee wants to finish uploading the scores as soon as possible. She believes that uploading the scores is more urgent and therefore should be completed first. 
She, however,  decides to work on another admin matter. The scores could not be uploaded in time and worthy students were denied chance to succeed in their life.
"""

b7="""An employee of a school is tasked with uploading online, the test scores of the students for a scholarship test. This scholarship is for economically weaker students and would give them opportunities to study in premier institutions to succeed in life. The scores have to be uploaded within a given deadline. It is the last day of the deadline.
The employee wants to finish uploading the scores as soon as possible.
She believes that there is enough time to upload the scores, and she could take up other work in the meantime. 
She decides to work on another admin matter. The scores could not be uploaded in time and worthy students were denied chance to succeed in their life.
"""

c7="""An employee of a school is tasked with uploading online, the test scores of the students for a scholarship test. This scholarship is for economically weaker students and would give them opportunities to study in premier institutions to succeed in life. The scores have to be uploaded within a given deadline. It is the last day of the deadline.
The employee wants to finish uploading the scores as soon as possible.
She believes that uploading the scores is more urgent and therefore should be completed first.
She, however,  decides to work on another admin matter. However, the deadline was extended and she was able to upload all the scores and worthy students got through. 
"""

d7="""An employee of a school is tasked with uploading online, the test scores of the students for a scholarship test. This scholarship is for economically weaker students and would give them opportunities to study in premier institutions to succeed in life. The scores have to be uploaded within a given deadline. It is the last day of the deadline.
The employee wants to finish uploading the scores as soon as possible.
She believes that there is enough time to upload the scores, and she could take up other work in the meantime. 
She, however,  decides to work on another admin matter. However, the deadline was extended and she was able to upload all the scores and worthy students got through.
"""

e7="""An employee of a school is tasked with uploading online, the test scores of the students for a scholarship test. This scholarship is for economically weaker students and would give them opportunities to study in premier institutions to succeed in life. The scores have to be uploaded within a given deadline. It is the last day of the deadline.
The employee wants to finish her pending work as soon as possible.
She believes that uploading the scores is more urgent and therefore should be completed first.
She, however, decides to work on another admin matter. The scores could not be uploaded in time and worthy students were denied chance to succeed in their life.
"""

f7="""An employee of a school is tasked with uploading online, the test scores of the students for a scholarship test. This scholarship is for economically weaker students and would give them opportunities to study in premier institutions to succeed in life. The scores have to be uploaded within a given deadline. It is the last day of the deadline.
The employee wants to finish her pending work, as soon as possible
She believes that there is enough time to upload the scores, and she could take up other work in the meantime. 
She decides to work on another admin matter. The scores could not be uploaded in time and worthy students were denied chance to succeed in their life.
"""

g7="""An employee of a school is tasked with uploading online, the test scores of the students for a scholarship test. This scholarship is for economically weaker students and would give them opportunities to study in premier institutions to succeed in life. The scores have to be uploaded within a given deadline. It is the last day of the deadline.
The employee wants to finish her pending work, as soon as possible
She believes that uploading the scores is more urgent and therefore should be completed first.
She, however,  decides to work on another admin matter. However, the deadline was extended and she was able to upload all the scores and worthy students got through.
"""

h7="""An employee of a school is tasked with uploading online, the test scores of the students for a scholarship test. This scholarship is for economically weaker students and would give them opportunities to study in premier institutions to succeed in life. The scores have to be uploaded within a given deadline. It is the last day of the deadline.
The employee wants to finish her pending work, as soon as possible
She believes that there is enough time to upload the scores, and she could take up other work in the meantime.
She, however,  decides to work on another admin matter. However, the deadline was extended and she was able to upload all the scores and worthy students got through.  
"""

a8="""A maintenance officer of a public school building is given the information that there are cracks on some walls of the school. If the situation is not immediately looked into, the walls will collapse and children’s lives will be at risk. 
He wants to ensure the safety of the children at school. 
He believes that it is best to immediately release funds to fix the wall. 
He, however, only gets the walls painted to hide the issue. Damp penetrates the wall as a result of which it collapses and two children lose their lives and others are injured.
"""

b8="""A maintenance officer of a public school building is given the information that there are damp patches on some walls of the school. If the situation is not immediately looked into, the walls will collapse and children’s lives will be at risk. 
He wants to ensure the safety of the children at school. 
He believes that the wall is not in very bad condition and can be fixed later.
He only gets the walls painted to hide the issue. Damp penetrates the wall as a result of which it collapses and two children lose their lives and others are injured.
"""

c8="""A maintenance officer of a public school building is given the information that there are damp patches on some walls of the school. If the situation is not immediately looked into, the walls will collapse and children’s lives will be at risk. 
He wants to ensure the safety of the children at school. 
He believes that it is best to immediately release funds to fix the wall. 
He, however, only gets the walls painted without fixing the leak. One of the workers notices the cracks and seals them before painting as a result of which the walls stay stable. 
"""

d8="""A maintenance officer of a public school building is given the information that there are damp patches on some walls of the school. If the situation is not immediately looked into, the walls will collapse and children’s lives will be at risk. 
He wants to ensure the safety of the children at school. 
He believes that the wall is not in very bad condition and can be fixed later.
He only gets the walls painted without fixing the leak. One of the workers notices the cracks and seals them before painting as a result of which the walls stay stable. 
"""

e8="""A maintenance officer of a public school building is given the information that there are damp patches on some walls of the school. If the situation is not immediately looked into, the walls will collapse and children’s lives will be at risk. 
He wants to save money for other construction work in the school.
He believes that it is best to immediately release funds to fix the wall.  
He, however, only gets the walls painted to hide the issue. Damp penetrates the wall as a result of which it collapses and two children lose their lives and others are injured.
"""

f8="""A maintenance officer of a public school building is given the information that there are damp patches on some walls of the school. If the situation is not immediately looked into, the walls will collapse and children’s lives will be at risk. 
He wants to save money for other construction work in the school.
He believes that the wall is not in very bad condition and can be fixed later.
He only gets the walls painted to hide the issue. Damp penetrates the wall as a result of which it collapses and two children lose their lives and others are injured.
"""

g8="""A maintenance officer of a public school building is given the information that there are damp patches on some walls of the school. If the situation is not immediately looked into, the walls will collapse and children’s lives will be at risk. 
He wants to save money for other construction work in the school.
He believes that it is best to immediately release funds to fix the wall. 
He, however, only gets the walls painted without fixing the leak. One of the workers notices the cracks and seals them before painting as a result of which the walls stay stable. 
"""

h8="""A maintenance officer of a public school building is given the information that there are damp patches on some walls of the school. If the situation is not immediately looked into, the walls will collapse and children’s lives will be at risk. 
He wants to save money for other construction work in the school.
He believes that the wall is not in very bad condition and can be fixed later.
He only gets the walls painted without fixing the leak. One of the workers notices the cracks and seals them before painting as a result of which the walls stay stable. 
"""
q1="""How wrong was this agent’s behaviour?  """    
op ="""   [(1 (not at all)-4(somewhat)-7(Very much)]"""

q2="""How wrong was this engineer’s behaviour? """   

q3="""How wrong was this staffer’s behaviour? """    

q4="""How wrong was this travel guide’s behaviour?"""    

q5="""How wrong was this officer’s behaviour? """    

q6="""How wrong was this employee’s behaviour?  """   

q7="""How wrong was this employee’s behaviour?   """

q8="""How wrong was this officer’s behaviour?   """ 

new_item = submission()
usrname = ""
email = ""
age = ""
gender = ""
quest1 = ""
quest2 = ""
quest3 = ""
quest4 = ""
quest5 = ""
quest6 = ""
quest7 = ""
quest8 = ""
#localtime = datetime.now


situat = list()

question= [q1,q2,q3,q4,q5,q6,q7,q8]


order = [] 
reference=list()

def home(request):
    for i in sample(range(8),8):
        order.append(i)
    
    l=list(range(0,8))
    
    situation = [
        [a1,b1,c1,d1,e1,f1,g1,h1],
        [a2,b2,c2,d2,e2,f2,g2,h2],
        [a3,b3,c3,d3,e3,f3,g3,h3],
        [a4,b4,c4,d4,e4,f4,g4,h4],
        [a5,b5,c5,d5,e5,f5,g5,h5],
        [a6,b6,c6,d6,e6,f6,g6,h6],
        [a7,b7,c7,d7,e7,f7,g7,h7],
        [a8,b8,c8,d8,e8,f8,g8,h8]
    ]
    for i in range(0,8):
        j = choice(l)
        temp="Situation: "+str(i)+"     Choice: "+str(j)
        reference.append(temp)
        situat.append(situation[i][j])
        l.remove(j)
    return render(request, 'home/homeview.html')

#argument_dict=dict( (name,eval(name)) for name in situat )
#argument_list=list(argument_dict.keys())

def proceed1(request):
    
    global usrname,email,age,gender 
    usrname = request.POST["usrname"]
    email = request.POST["email"]
    age = request.POST["age"]
    gender = request.POST["gender"]
    return HttpResponseRedirect('/quest1/')

def proceed2(request):
    global quest1
    quest1 = request.POST["quest1"]
    return HttpResponseRedirect('/quest2/')

def proceed3(request):
    global quest2
    quest2 = request.POST["quest2"]
    return HttpResponseRedirect('/quest3/')

def proceed4(request):
    global quest3
    quest3 = request.POST["quest3"]
    return HttpResponseRedirect('/quest4/')

def proceed5(request):
    global quest4
    quest4 = request.POST["quest4"]
    return HttpResponseRedirect('/quest5/')

def proceed6(request):
    global quest5
    quest5 = request.POST["quest5"]
    return HttpResponseRedirect('/quest6/')

def proceed7(request):
    global quest6
    quest6 = request.POST["quest6"]
    return HttpResponseRedirect('/quest7/')

def proceed8(request):
    global quest7
    quest7 = request.POST["quest7"]
    return HttpResponseRedirect('/quest8/')

def proceedf(request):
    global quest8,quest7,quest6,quest5,quest4,quest3,quest2,quest1,usrname,email,age,gender,localtime
    quest8 = request.POST["quest8"]
    new_item = submission(usrname = usrname, email= email, age = age, gender = gender,quest1 = quest1, quest2=quest2,quest3=quest3,quest4=quest4, quest5= quest5, quest6=quest6,quest7=quest7, quest8 = quest8)#time = localtime)
    new_item.save()
    return HttpResponseRedirect('/feedbck/')


def question1(request):
    return render(request, 'questions/question1.html',{'situation': situat[order[0]],'question':question[order[0]],'option' : op,'questid': reference[order[0]]})
    
def question2(request):
    return render(request, 'questions/question2.html',{'situation': situat[order[1]],'question':question[order[1]],'option' : op,'questid': reference[order[1]]})
    
def question3(request):
    return render(request, 'questions/question3.html',{'situation': situat[order[2]],'question':question[order[2]],'option' : op,'questid': reference[order[2]]})
   
def question4(request):
    return render(request, 'questions/question4.html',{'situation': situat[order[3]],'question':question[order[3]],'option' : op,'questid': reference[order[3]]})
    
def question5(request):
    return render(request, 'questions/question5.html',{'situation': situat[order[4]],'question':question[order[4]],'option' : op,'questid': reference[order[4]]})
    
def question6(request):
    return render(request, 'questions/question6.html',{'situation': situat[order[5]],'question':question[order[5]],'option' : op,'questid': reference[order[5]]})
    
def question7(request):
    return render(request, 'questions/question7.html',{'situation': situat[order[6]],'question':question[order[6]],'option' : op,'questid': reference[order[6]]})
    
def question8(request):
    return render(request, 'questions/question8.html',{'situation': situat[order[7]],'question':question[order[7]],'option' : op,'questid': reference[order[7]]})
    
def feedbck(request):
    return render(request, 'home/feedback.html',{'name':usrname})    

def fform(request):
    sub = feedback(feed = request.POST["message"])
    sub.save()
    #time = localtime )
    return HttpResponseRedirect('/')



# def home(request):
# 	return render(request, 'homeview.html')
#    new_item = submission(quest1 = request.POST["quest1"])

# Create your views here.
#now = datetime.datetime.now()
    #today = now.strftime("%A, %b, %d, %Y,")
    #sub_set = [1,2,3,4,5,6,7,8]
    #quetions = ['a','b','c','d','e','f','g','h']