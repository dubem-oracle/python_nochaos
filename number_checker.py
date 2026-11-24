number_one = 1
number_two = 0
number_three = 0

for (number_one = 1; number_one < 10; number_one++ ): 
    for ( number_two = 0; number_two < 10; number_two++ ): 
        for ( number_three = 0; number_three < 10; number_three++ ):
            square = ( number_one * number_one ) + ( number_two * number_two ) + ( number_three * number_three )
            number = ( number_one * 100) + ( number_two * 10 ) + ( number_three )
            if ( square == number ):
            print(number);
            
