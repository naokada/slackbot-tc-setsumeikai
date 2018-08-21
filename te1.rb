def aa(num)
	if (num > 0)
		return "[" + aa(num-1) + "]"
	else
		return "*"
	end

end

puts aa(5)