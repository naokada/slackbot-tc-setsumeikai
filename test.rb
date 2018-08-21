def isImisuu(day)
    imisuu = [4, 5, 9, 13, 14, 17]

    for i in imisuu do
        if i == day
            return true
        end
    end
    return false
end
def calImisuuYear()
    imisuu = [4, 5, 9, 13, 14, 17]
    count = 0
    months = [*1..12]

    for i in months do
#        unless imisuu.include?(i)
        # unless isImisuu(i)
        #     count += 6
        # end
        count += 24 unless isImisuu(i)
    end
    return count
end

    imisuu = [4, 5, 9, 13, 14, 17]
    count = 0
#    imisuu_month = imisuu.length
		imisuu_month = 24 #修正
    imisuu_year  = calImisuuYear

    days = [*1..30]

    year1 = 2014
    year2 = 2015

    month1 = 2
    month2 = 3

    day1 = 10
    day2 = 10


    if (year2 - year1 > 1)
    	count = count + (year2 - year1 - 1) * imisuu_year
  	end

  	if (year1 != year2)
	  	tempmonth = 12 + month2 -1
	  	for k in [*(month1 + 1)..tempmonth] do
		  		if k > 12
		  			k %= 12
		  		end	

	  			unless isImisuu(k) #修正
	            count += imisuu_month
	        end
	  	end
	  end




  	if ((month2 - month1) > 1)
    	count = count + (month2 - month1 - 1) * imisuu_month
    end

  	tempday = 30 + day2#修正

#    for j in [*current..30]  do
		for j in [*day1..tempday] do #修正
			if j > 30
	  		j %= 30
	  	end	
#        unless imisuu.include?(days[(day1 + j - 1) % 30])
      unless isImisuu(j) #修正
          count += 1
      end
    end
    puts count

