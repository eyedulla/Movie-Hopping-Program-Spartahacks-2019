#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:06:30 2019

@author: eyedulla
"""
from itertools import permutations 


def convert24(str1): 
    #time validifier
    check_lst=str1.split(":")
    if len(check_lst[0])==1:
        str1="0"+str1
    
    
    
#    print(str1) 
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2]+"AM" 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 


#num_movies=7
#init_movie_order=['vice','aquaman','mary','glass','basis','upside','spiderman']
   
def movie_sequence(init_movie_order):
    num_movies=len(init_movie_order)
    all_movie_sequence_list=[]
    l = list(permutations(range(1, num_movies+1)))
    for tup in l:
        individ_movie_sequence_list=[]
        for number in tup:
            corresponding_movie=init_movie_order[number-1]
            individ_movie_sequence_list.append(corresponding_movie)
            if len(individ_movie_sequence_list)==num_movies:
                all_movie_sequence_list.append(individ_movie_sequence_list)
    return all_movie_sequence_list
            

#init_movie_order=["aquaman","spiderman","vice","glass"]
#current_movie_sequence=movie_sequence(init_movie_order)
#print(current_movie_sequence)
#current_movie_sequence_individ=['Aquaman', 'The upside', 'Vice', 'Glass']
#[3,6,3,5]
#print(current_movie_sequence,"HERE")
#movie_dict={'The upside': [('15:30', '17:28'), ('16:30', '18:28'), ('18:15', '20:13'), ('19:15', '21:13'), ('21:00', '22:58'), ('22:00', '23:58')], 'Glass': [('19:00', '21:09'), ('22:00', '24:09'), ('20:00', '22:09'), ('21:00', '23:09'), ('21:30', '23:39')], 'Aquaman': [('15:45', '18:08'), ('17:30', '19:53'), ('20:45', '23:08')], 'Vice': [('16:30', '18:42'), ('19:30', '21:42'), ('22:30', '24:42')]}




def showtime_possib(current_movie_sequence_individ,movie_dict):
#    print(current_movie_sequence_individ)
#    print(movie_dict)
    showtime_amts_lst=[]
    for movie in current_movie_sequence_individ:
#        print(movie)
        movie_showtimes=movie_dict[movie]
#        print(movie,movie_showtimes)
        num_showtimes=len(movie_showtimes)
#        print(num_showtimes)
        showtime_amts_lst.append(num_showtimes)
#    print(showtime_amts_lst)
    lst=showtime_amts_lst


    #following is for determining the different ways you can watch movies 
    lst_len=len(showtime_amts_lst)
    if lst_len==1:
        showtime_possibilities_list=[]
        for num1 in range(lst[0]):
            showtime_possibilities_list.append(num1)
    #    print(showtime_possibilities_list)
            
    if lst_len==2:
        showtime_possibilities_list=[]
        for num1 in range(lst[0]):
            for num2 in range(lst[1]):
                time_lst=[num1,num2]
                showtime_possibilities_list.append(time_lst)
#        print(showtime_possibilities_list)
    
    if lst_len==3:
        showtime_possibilities_list=[]
        for num1 in range(lst[0]):
            for num2 in range(lst[1]):
                for num3 in range(lst[2]):
                    time_lst=[num1,num2,num3]
                    showtime_possibilities_list.append(time_lst)
#        print(showtime_possibilities_list)
        
    if lst_len==4:
        showtime_possibilities_list=[]
        for num1 in range(lst[0]):
            for num2 in range(lst[1]):
                for num3 in range(lst[2]):
                    for num4 in range(lst[3]):
                        time_lst=[num1,num2,num3,num4]
                        showtime_possibilities_list.append(time_lst)
#        print(showtime_possibilities_list)
            
    if lst_len==5:
        showtime_possibilities_list=[]
        for num1 in range(lst[0]):
            for num2 in range(lst[1]):
                for num3 in range(lst[2]):
                    for num4 in range(lst[3]):
                        for num5 in range(lst[4]):
                            time_lst=[num1,num2,num3,num4,num5]
                            showtime_possibilities_list.append(time_lst)
#        print(showtime_possibilities_list)
        
    if lst_len==6:
        showtime_possibilities_list=[]
        for num1 in range(lst[0]):
            for num2 in range(lst[1]):
                for num3 in range(lst[2]):
                    for num4 in range(lst[3]):
                        for num5 in range(lst[4]):
                            for num6 in range(lst[5]):
                                time_lst=[num1,num2,num3,num4,num5,num6]
                                showtime_possibilities_list.append(time_lst)
#        print(showtime_possibilities_list)
        
    if lst_len==7:
        showtime_possibilities_list=[]
        for num1 in range(lst[0]):
            for num2 in range(lst[1]):
                for num3 in range(lst[2]):
                    for num4 in range(lst[3]):
                        for num5 in range(lst[4]):
                            for num6 in range(lst[5]):
                                for num7 in range(lst[6]):
                                    time_lst=[num1,num2,num3,num4,num5,num6,num7]
                                    showtime_possibilities_list.append(time_lst)
#        print(showtime_possibilities_list)
        
    if lst_len==8:
        showtime_possibilities_list=[]
        for num1 in range(lst[0]):
            for num2 in range(lst[1]):
                for num3 in range(lst[2]):
                    for num4 in range(lst[3]):
                        for num5 in range(lst[4]):
                            for num6 in range(lst[5]):
                                for num7 in range(lst[6]):
                                    for num8 in range(lst[7]):
                                        time_lst=[num1,num2,num3,num4,num5,num6,num7,num8]
                                        showtime_possibilities_list.append(time_lst)
#        print(showtime_possibilities_list)
        
    if lst_len==9:
        showtime_possibilities_list=[]
        for num1 in range(lst[0]):
            for num2 in range(lst[1]):
                for num3 in range(lst[2]):
                    for num4 in range(lst[3]):
                        for num5 in range(lst[4]):
                            for num6 in range(lst[5]):
                                for num7 in range(lst[6]):
                                    for num8 in range(lst[7]):
                                        for num9 in range(lst[8]):
                                            time_lst=[num1,num2,num3,num4,num5,num6,num7,num8,num9]
                                            showtime_possibilities_list.append(time_lst)
#        print(showtime_possibilities_list)
        
    if lst_len==10:
        showtime_possibilities_list=[]
        for num1 in range(lst[0]):
            for num2 in range(lst[1]):
                for num3 in range(lst[2]):
                    for num4 in range(lst[3]):
                        for num5 in range(lst[4]):
                            for num6 in range(lst[5]):
                                for num7 in range(lst[6]):
                                    for num8 in range(lst[7]):
                                        for num9 in range(lst[8]):
                                            for num10 in range(lst[9]):
                                                time_lst=[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]
                                                showtime_possibilities_list.append(time_lst)
#        print(showtime_possibilities_list)
    
    
    #convert numbers to actual showtimes with endtimes
    final_showtime_lst=[]
    for combos in showtime_possibilities_list:
        semi_final_showtime_lst=[]
        index_value=0
        for show_order_value in combos:
            movie_name=current_movie_sequence_individ[index_value]
            show_tup=movie_dict[movie_name][show_order_value]
#            print(show_tup)
            semi_final_showtime_lst.append(show_tup)
#            print(semi_final_showtime_lst)
            if len(semi_final_showtime_lst)==len(current_movie_sequence_individ):
                final_showtime_lst.append(semi_final_showtime_lst)
            index_value+=1
    return(final_showtime_lst)

#showtime_possib(current_movie_sequence_individ,movie_dict)


#showtimes_mini_real.csv
#songdata_small.csv
#ACS_tiny.csv

#{movie:[(start time, end time),(start time, end time)]}
def file_to_lst():
    lst_final=[]
    file=input("enter file name")
    fp=open(file,mode='r', encoding='utf-8-sig')
    for line in fp:
        line=line.strip()
        line=line.strip(',')
    #    print (line)
        lst_init=line.split(",")
#        print(lst_init)
        if lst_init!=['']:
            lst_final.append(lst_init)
#    print(lst_final)
    return(lst_final)
#file=file_to_lst()


def end_time(movie_length,start_time):
    #convert movie_length to decimal
#    print(start_time,"end_time star time")
#    print()
    movie_length_lst=movie_length.split(":")
    hour=int(movie_length_lst[0])
    min_decimal=int(movie_length_lst[1])/60
    movie_length_decimal=hour+min_decimal
#    print(movie_length_decimal)
    
    #convert start time to decimal 
    start_time_lst=start_time.split(":")
    start_hour=int(start_time_lst[0])
    
    
#    print(tywstart_time_lst[1])
    
#    print(start_time_lst[1])
    start_min_decimal=int(start_time_lst[1])/60
    end_time_decimal=start_hour+start_min_decimal
#    print(end_time_decimal)
    
    #add time together
    final_decimal_length=movie_length_decimal+end_time_decimal
#    print(final_decimal_length)

    #conversion back to 24 hr time
    final_decimal_length=str(final_decimal_length)
    decimal_list=final_decimal_length.split(".")
    dec="."+decimal_list[1]
    dec=float(dec)
    dec_conversion=(dec*60)
    dec_conversion=round(dec_conversion)
    dec_conversion=str(dec_conversion)
#    print(dec_conversion)
    if len(dec_conversion)<=1:
        dec_conversion="0"+dec_conversion
#    print(dec_conversion)
    final_time=decimal_list[0]+":"+dec_conversion
#    print(final_time)
    
    #################################
    #TIME WILL GO OVER 24 HOUR CLOCK#
    #################################
    
    return final_time


#[['Glass', '7:00PM', '10:00PM', '8:00PM', '9:00PM', '9:30PM'], ['Aquaman', '3:45PM', '5:30PM', '8:45PM'], ['The upside', '3:30PM', '4:30PM', '6:15PM', '7:15PM', '9:00PM', '10:00PM'], ['Vice', '4:30PM', '7:30PM', '10:30PM'], ['Glass', '7:00PM', '10:00PM', '8:00PM', '9:00PM', '9:30PM'], ['Aquaman', '3:45PM', '5:30PM', '8:45PM'], ['The upside', '3:30PM', '4:30PM', '6:15PM', '7:15PM', '9:00PM', '10:00PM'], ['Vice', '4:30PM', '7:30PM', '10:30PM']]
def lst_to_dict(movie_lsts):
    movie_dict={}
    for items in movie_lsts:
#        print(movie_lsts)
#        print(items)
#        print(items[0])
        key=[]
        list_len=len(items)
        for num in range(2,list_len):
            start_time=items[num]
#            print(start_time,"lst_to_dict start time")
            movie_length=items[1]
#            print(items[num]) 
            
#            print(movie_length,start_time)
            #start time conversion
#            print(start_time)
            
            
#PROBLEM MIGHT BE HERE 
#            print(start_time)
            start_time=convert24(start_time)
#            print(start_time,"conver24 start time")
#            print(start_time)
            if "AM" in start_time:
                start_time=start_time[:-2]
            if "PM" in start_time:
                start_time=start_time[:-2]            
#            print(start_time,"[:-2]")
#            print(start_time)
            
            #end time
#            print(start_time)
            end_movie_time=end_time(movie_length,start_time)
#            print(start_time,end_movie_time)
            append_tup=(start_time,end_movie_time)
            key.append(append_tup)
            movie_dict[items[0]]=key
        
    return(movie_dict)       
    
   
#movie_lsts=file_to_lst()
#print(movie_lsts)
#print(lst_to_dict(movie_lsts))
    

#print(end_time("2:00","23:00"))


#init_movie_order=["aquaman","spiderman","vice","glass"]
#print(movie_sequence(init_movie_order))

def main():
    import time
    start_time_clock = time.time()
    final_final_movie_list=[]
    #opens the list and converts the file to a list
    #the list is a list of lists. The 2nd list has movie name, run time, and show times
    movie_info_lst=(file_to_lst())
#    print(movie_info_lst)
    
    
    #find possible movie going sequences. What orders can I watch the movies in?
    movie_list_order_init=[]
    for movie_lists in movie_info_lst:
        movie_list_order_init.append(movie_lists[0])
#    print(movie_list_order_init)
    possible_movie_sequences=movie_sequence(movie_list_order_init)
#    print(possible_movie_sequences)
    
    
    #CORRECT
    
    
    #create a dictionary with movie info
    #format{movie:[]}
#    print(movie_info_lst)
    #ERROR IS WITH MOVIE DICTIONARY--->Fixed
    movie_dictionary=lst_to_dict(movie_info_lst)
#    print(movie_dictionary,"HERE")
    

    #go through each possible movie sequence
    #first find the possible show viewing times combos for each movie sequence
    for individ_movie_sequence in possible_movie_sequences:
#        print(individ_movie_sequence)
        showtime_combos=showtime_possib(individ_movie_sequence,movie_dictionary)
#        print(showtime_combos)
#        print()
#        print()
#        print()
#        print()
#        print()
#        print(individ_movie_sequence,showtime_combos)
        
        
        #now find the viable movie hopping trains
        #start by correctly issolating the two time groups
        for start_end_lst in showtime_combos:
#            print("**************************************************")
            initial_movie=()
            following_movie=()
            lst_len=len(start_end_lst)
            counter=0
            state=True
            while counter<lst_len-1:
                initial_movie=start_end_lst[counter]
                following_movie=start_end_lst[counter+1]
#                print(initial_movie,following_movie)
#                
#                
#                #now subtract times to see if hop is viable
#                #convert initial end time to a decimal first
                end_time=initial_movie[1]
                end_min_decimal_conversion=(int(end_time[3:])/60)+float(end_time[:-3])
#                print(end_min_decimal_conversion)
                #convert following start tim to a decimal
                start_time=following_movie[0]
                start_min_decimal_conversion=(int(start_time[3:])/60)+float(start_time[:-3])
#                print(start_min_decimal_conversion)
                #calculate time difference
                #time difference needs to be between -.25 and .25
                time_diff=start_min_decimal_conversion-end_min_decimal_conversion
#                print(time_diff)
                counter+=1
#                print(counter)
                #i need to allow watching more than 2 movies back to back 
                
                if time_diff>.25 or time_diff<-.25:
                    state=False
                
                if time_diff<=.25 and time_diff>=-.25 and state==True:
                    
                    #finds data for the first movie that you can movie hop from
                    first_movie_index=start_end_lst.index(initial_movie)
#                    print(first_movie_index)
                    first_movie_name=individ_movie_sequence[first_movie_index]
                    start_time_first_movie=initial_movie[0]
                    
                    
                    #finds data for the second movie that you can movie hop from
                    following_movie_index=start_end_lst.index(following_movie)
#                    print(following_movie_index)
                    following_movie_name=individ_movie_sequence[following_movie_index]
                    start_time_second_movie=following_movie[0]
                    
                    
                    
#                    print(first_movie_name,counter,initial_movie,following_movie)
#                    print(individ_movie_sequence)
#                    print(start_end_lst)
                #[[movie,]]    
                    if counter==1:
                        final_final_movie_list.append([first_movie_name,start_time_first_movie,\
                                                       following_movie_name,start_time_second_movie])
                     
                    if counter>1:
                        final_final_movie_list[-1].extend([following_movie_name,start_time_second_movie])
                
#    print(final_final_movie_list)
    no_duplicate_final_list=[]
    for movie_data in final_final_movie_list:
        if movie_data not in no_duplicate_final_list:
            no_duplicate_final_list.append(movie_data)
#    print("************")
#    print(no_duplicate_final_list)
    
    #FORMATING 
    print("*******************")
    print("MOVIE HOP OPTIONS")
    print("*******************")
    print("Time is printed in 24 hour format:")
    for movie_hop_lists in no_duplicate_final_list:
        movie_hop_len=len(movie_hop_lists)
        hop_index_value=0
        print("-"*40)
        data_format="{:<20}{:<40}".format("Movie","Start Time")
        print(data_format)
        num_order=0
        
        while movie_hop_len>hop_index_value+1:
            num_order+=1
            data_format2=str(num_order)+".{:<20}{:<40}".format(movie_hop_lists[hop_index_value],movie_hop_lists[hop_index_value+1])
            print(data_format2)
#            print(movie_hop_lists[hop_index_value],movie_hop_lists[hop_index_value+1])
            hop_index_value+=2
    end=time.time()
    print()
    print ("The program took", (end) - (start_time_clock), "to run")
    


                





main()
    
        

















